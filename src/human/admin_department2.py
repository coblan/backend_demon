from helpers.director.shortcut import page_dc,director,ModelFields,ModelTable,TablePage,director_view
from .models import TBDepartment
from helpers.director.model_func.dictfy import to_dict
from django.db.models import Count,F,OuterRef, Subquery,Exists


class DepartmentPage(TablePage):
    def get_label(self):
        return '部门管理'

    def get_template(self, prefer=None):
        return 'jb_admin/table_new.html'

    class tableCls(ModelTable):
        model = TBDepartment
        exclude = []
 
        hide_fields=['parent','path','id']
        pop_edit_fields = ['name']
        selectable = False

        #def dict_head(self, head):
            #if head['name'] == 'name':
                #head['editor'] = 'com-table-click'
                #head['width'] = 200
                #head['action'] ='scope.ps.search_args.parent = scope.row.pk;scope.ps.search()'
            #return head
            
        def dict_head(self, head):
            width = {
                'name':200
            }
            head['width'] = width.get(head['name'])
            return head
            
        def inn_filter(self, query):
            if self.kw.get('par'):
                query  =query.filter(parent_id = self.kw.get('par'))
            else:
                query = query.filter(parent__isnull = True)
            subquery = TBDepartment.objects.filter(parent=OuterRef('pk'))
            query = query.annotate(hasChildren=Exists(subquery))
            return query

        #def getParents(self):
            #ls =[]
            #par_pk = self.kw.get('parent',-1)
            #if par_pk >= 0 :
                #parent = TBDepartment.objects.get(pk = par_pk)
                #while True:
                    #ls.append({'value':parent.pk,'label':str(parent)})
                    #if parent.parent:
                        #parent = parent.parent
                    #else:
                        #break
            #ls.append({'value':-1,'label':'公司'})
            #ls.reverse()
            #return ls
        
        def dict_row(self, inst):
            return {
                'hasChildren':inst.hasChildren,               
            }
        #def get_operation(self):
            #ops = super().get_operation()
            #for op in ops:
                #if op['name'] =='add_new':
                    #op['pre_set'] ='rt={parent_id:scope.search_args.parent} '
                    #op['label'] = '添加部门'
            #ops += [
                #{'name':'cut','label':'剪切','editor':'com-op-btn','row_match':'many_row','action':'if(scope.ps.check_selected(scope.head)){scope.ps.catch_rows = scope.ps.selected;cfg.toast("剪切成功，请选择部门，再粘贴")}'},
                #{'name':'paste','label':'粘贴','editor':'com-op-btn','action':''' (function(){ if(!scope.ps.catch_rows){cfg.showMsg("请先选中并剪切一些部门"); return;}
                 #ex.director_call("department.move",{rows:scope.ps.catch_rows,parent:scope.ps.search_args.parent}).then((res)=>{
                    #scope.catch_rows=null;  res.forEach(item=>{scope.ps.update_or_insert(item)} )
                 #})   
                #})()''' }
            #]
            #return ops


@director_view('department.move')
def move_department(rows,parent):

    if parent >0:
        parent = TBDepartment.objects.get(pk = parent)
    else:
        parent =None

    row_ps_list = [x['pk'] for x in rows]
    out_rows=[]
    for dep in TBDepartment.objects.filter(pk__in=row_ps_list):
        if parent and dep.pk == parent.pk:
            raise UserWarning('不能把自己设置为上级')
        modify_parent(dep,parent)
        out_rows.append(to_dict(dep))
    return out_rows

def modify_parent(inst,parent):
    old_path = inst.path
    path_ls = []
    path_ls.append(inst.pk)
    last_parent = parent
    while last_parent:
        path_ls.append(last_parent.pk)
        if last_parent == last_parent.parent:
            last_parent.parent = None
            last_parent.save()
        last_parent = last_parent.parent
    new_path = '/'+'/'.join([str(x) for x in reversed(path_ls)])
    inst.path = new_path
    inst.parent = parent
    inst.save()
    if old_path:
        for item in TBDepartment.objects.filter(path__startswith=old_path):
            item.path = item.path.replace(old_path,new_path)
            item.save()

class DepartmentForm(ModelFields):
    hide_fields = ['parent','path']
    class Meta:
        model = TBDepartment
        exclude = []

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        if not self.instance.pk and self.kw.get('parent'):
            self.instance.parent = TBDepartment.objects.get(pk = self.kw.get('parent'))

    def after_save(self):
        if not self.instance.parent and not self.instance.path:
            self.instance.path='/%s'%self.instance.pk
            self.instance.save()
        if 'parent' in self.changed_data:
            modify_parent(self.instance,self.instance.parent)

    def del_form(self):
        path = self.instance.path
        super().del_form()
        TBDepartment.objects.filter(path__startswith=path).delete()



class DepartmentTable(DepartmentPage.tableCls):
    include=['name']
    pop_edit_field = None
    def getExtraHead(self):
        return [
            {'name':'nextlevel','editor':'com-table-span','action':'scope.ps.search_args.parent = scope.row.pk;scope.ps.search()','class':'clickable table-op','css':'.table-op{font-size:.25rem;width:1.3rem;flex-grow:0;}'},
            {'name':'select','editor':'com-table-span','action':'scope.ps.par_row.depart=scope.row.pk;Vue.set(scope.ps.par_row,"_depart_label",scope.row.name);history.back()','class':'clickable table-op'}
        ]

    def dict_row(self, inst):
        return {
            'nextlevel':'下级',
            'select':'选择'
        }





director.update({
    'department2':DepartmentPage.tableCls,
    'department2.edit':DepartmentForm,
    'mobile_department_table':DepartmentTable,

})

page_dc.update({
    'department2':DepartmentPage
})