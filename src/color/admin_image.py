from helpers.director.shortcut import ModelTable,TablePage,ModelFields,page_dc,director,RowFilter,director_view
from . models import SourceImage,Tag
import os
from django.conf import settings
from PIL import Image
from django.utils import timezone
from helpers.director.model_func.dictfy import sim_dict


class ImagePage(TablePage):
    def get_label(self):
        return '图片管理'
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = SourceImage
        exclude =[]
        pop_edit_fields=['id']
        
        def dict_head(self, head):
            width = {
                'url':150,
                'tag_content':200,
            }
            if head['name'] in  width:
                head['width'] = width.get(head['name'])
            if head['name'] =='status':
                head['inn_editor'] = head['editor']
                head['editor']='com-table-rich-span'
                head['class']='middle-col btn-like-col'
                head['cell_class'] = 'var dc={0:"warning",1:"success",2:"ignore"};rt=dc[scope.row.status]'
            return head
        
        class filters(RowFilter):
            names = ['tag_content','status']
            icontains = ['tag_content']
            
        
class ImageForm(ModelFields):
    #readonly = ['uploadtime','resolution','size']
    class Meta:
        model = SourceImage
        exclude =[]
    
    def dict_head(self, head):
        if head['name'] =='tag_content':
            head['editor'] = 'com-field-split-text'
            head['required']=True
            head['options'] = [{'value':x.content,'label':x.content} for x in Tag.objects.all()]
            #head['options'] = [{'value':'ss','label':'sss'},{'value':'memei','label':'妹子'}]
        if head['name'] in ['uploadtime','resolution','size']:
            head['readonly'] =True
        return head
     
    def clean_save(self):
        if self.kw.get('url') and 'url' in self.changed_data:
            filename = os.path.join(os.path.dirname(settings.BASE_DIR),self.kw.get('url')[1:])
            if os.path.exists(filename):
                img = Image.open(filename)
                self.instance.resolution = '%s X %s'%(img.width,img.height)
                self.instance.size =  os.path.getsize(filename)
                self.instance.uploadtime = timezone.now()

@director_view('image/info')
def get_imageinfo(id):
    inst = SourceImage.objects.get(pk = id)
    return sim_dict( inst)


class MyImageList(ModelTable):
    model = SourceImage
    exclude = []
    simple_dict = True
    nolimit = True
    
 
director.update({
    'image':ImagePage.tableCls,
    'image.edit':ImageForm,
    'image-list':MyImageList,
})
    
page_dc.update({
    'image':ImagePage
})