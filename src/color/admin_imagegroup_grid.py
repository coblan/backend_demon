from helpers.director.shortcut import TablePage,ModelTable,ModelFields,director,page_dc,get_request_cache,director_view,RowFilter
from .models import ImageGroup,SourceImage
from .admin_image import ImagePage
from helpers.director.model_func.dictfy import sim_dict

class ImageGroupPage(TablePage):
    def get_label(self):
        return '图片组'
    
    def get_template(self, prefer=None):
        return 'jb_admin/live.html'
    
    def get_context(self):
        ctx = super().get_context()
        self.set_named_ctx()
        out_ctx = {
            'editor': 'live_table_type', 
            'editor_label':'报表分类',
            'editor_ctx':{
                'inn_editor':'com-table-layout-picture-grid',
                **ctx,}
        }
        return out_ctx
    
    @classmethod
    def set_named_ctx(cls):
        named_ctx = get_request_cache()['named_ctx']
        if 'imagegroup_tab' not in named_ctx:
            named_ctx['imagegroup_tab'] =[
                {
                'name':'baseinfo',
                'label':'基本信息',
                'com':'com-tab-fields-v1',
                'init_express':'ex.vueAssign(scope.row,scope.vc.par_row)',
                'fields_ctx':{
                    **(ImageGroupForm().get_head_context()),
                    'after_save':'var last_ps=root_live.stack[root_live.stack.length-1].ctx.last_ps;ex.vueAssign(scope.vc.par_row,scope.row);last_ps.update_or_insert(scope.vc.par_row);cfg.toast("保存成功")'
                    }
                } ,
                {
                    'name':'image-list',
                    'label':'图片列表',
                    'com':'com-tab-table-type',
                    'inn_editor':'com-table-layout-picture-grid',
                    'table_ctx': ImageList().get_head_context(),
                    'show':'scope.par_row.pk',
                    'pre_set':'rt= {group:scope.par_row.pk}',
                    #'init_express':'debugger;ex.director_call("imagegroup.ImageList",{group:scope.par_row.pk}).then((resp)=>{scope.rows = resp.rows})'
                }
            ]
    class tableCls(ModelTable):
        model = ImageGroup
        exclude =['images']
        
        def dict_head(self, head):
            width={
                'zh':130,
                'en':130,
                'cover':200,
            }
            if head['name'] in width:
                head['width'] = width.get(head['name'])
                
            if head['name'] =='zh':
                head['editor'] = 'com-table-switch-to-tab'
                head['ctx_name'] = 'imagegroup_tab'
                head['tab_name'] = 'baseinfo'
                
            return head
        
        def get_head_context(self):
            ctx = super().get_head_context()
            ctx.update({
                'fields_ctx':ImageGroupForm().get_head_context(),
                'title_click':'scope.ps.switch_to_tab({tab_name:"baseinfo",ctx_name:"imagegroup_tab",par_row:scope.row})'
                #'title_click':'scope.ctx.fields_ctx.row=scope.row;cfg.pop_vue_com("com-form-one",scope.ctx.fields_ctx)'
            })
            return ctx
        
        def get_operation(self):
            ops = super().get_operation() 
            for op in ops:
                if op['name'] =='add_new':
                    op['tab_name'] = 'baseinfo'
                    op['ctx_name'] = 'imagegroup_tab'
            ops +=[
                {'label':'切换视图','editor':'com-op-btn','action':'if(scope.ps.vc.ctx.inn_editor=="com-table-rows"){scope.ps.vc.ctx.inn_editor="com-table-layout-picture-grid"}else{scope.ps.vc.ctx.inn_editor="com-table-rows"}'}
            ]
            return ops
        
        def dict_row(self, inst):
            return {
                'image_url':inst.cover,
                'image_title':inst.zh
            }
        
        class filters(RowFilter):
            names =['status']
        
        
class ImageGroupForm(ModelFields):
    class Meta:
        model = ImageGroup
        exclude =['images']
    
    def dict_row(self, inst):
        return {
            'image_url':inst.cover,
            'image_title':inst.zh
        }
        
class ImageList(ImagePage.tableCls):
    model = SourceImage
    exclude =[]
    pop_edit_fields=[]
    
    def get_operation(self):
        return [
            {'label':'添加图片','editor':'com-op-btn',
             'table_ctx':{**( ImagePicker().get_head_context() ),
                          'init_express':"scope.ps.search()",
                          'inn_editor':'com-table-layout-picture-grid'},
             'action':'scope.head.table_ctx.search_args={group_id:scope.ps.vc.par_row.pk};cfg.pop_vue_com("com-live-table-type",scope.head.table_ctx).then(()=>{scope.ps.search()})',
             },
            {'label':'移除图片','editor':'com-op-btn','action':'cfg.show_load();var images=ex.map(scope.ps.selected,(item)=>{return item.pk});ex.director("imagegroup.saver").remove_images({group_id:scope.ps.vc.par_row.pk,images:images}).then(()=>{scope.ps.search();cfg.hide_load(2000)})'},
        ]
    
    def dict_row(self, inst):
        return {
            'image_url':inst.url,
            'image_title':inst.tag_content
        }
        
    def inn_filter(self, query):
        return query.filter(imagegroup__id = self.search_args.get('group') )


class ImagePicker(ImagePage.tableCls):
    model = SourceImage
    exclude =[]
    pop_edit_fields=[]
    
    def dict_row(self, inst):
        return {
            'image_url':inst.url,
            'image_title':inst.tag_content
        }
    
    def inn_filter(self, query):
        return query.exclude(imagegroup__id=self.search_args.get('group_id'))
    
    def get_operation(self):
        return [
            {'label':'确定选择','editor':'com-op-btn',
             'action':'var images=ex.map(scope.ps.selected,item=>{return item.pk});ex.director_call("imagegroup/insert_image",{group_id:scope.ps.vc.ctx.search_args.group_id,images:images}).then((resp)=>{scope.ps.vc.$emit("finish")})'}
        ]
    
    class filter(RowFilter):
        names =['tag_content']
        icontains = ['tag_content']
    

class ImagegroupSaver(object):
    def remove_images(self,group_id,images):
        group = ImageGroup.objects.get(pk = group_id)
        group.images.remove(*images)
        group.save()
        
    #def insert_image(self,group_id,images):
        #group = ImageGroup.objects.get(pk = group_id)
        #group.images.add(*images)
        #group.save()
    
#@director_view('imagegroup/insert_image')
#def insert_image(group_id,images):
    #group = ImageGroup.objects.get(pk = group_id)
    #ls =list( SourceImage.objects.filter(pk__in=images) )
    #group.images.add(*ls)

#@director_view('imagegroup/list')
#def get_imagegroup_list():
    #out = [ sim_dict(x) for x in  ImageGroup.objects.filter(status = 1)]
    #return out

#@director_view('imagegroup/images')
#def get_imagegroup_images(id):
    #out = [sim_dict(x) for x in SourceImage.objects.filter(imagegroup=id)]
    #return out

director.update({
    'imagegroup_grid':ImageGroupPage.tableCls,
    'imagegroup_grid.edit':ImageGroupForm,
    'imagegroup_grid.ImageList':ImageList,
    'imagegroup_grid.imagepicker':ImagePicker,
    'imagegroup_grid.saver':ImagegroupSaver
})

page_dc.update({
    'imagegroup_grid':ImageGroupPage
})
