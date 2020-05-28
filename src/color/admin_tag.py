from helpers.director.shortcut import TablePage,ModelTable,ModelFields,page_dc,director
from .models import Tag

class TagPage(TablePage):
    def get_label(self):
        return '标签管理'
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    class tableCls(ModelTable):
        model = Tag
        exclude =[]
        pop_edit_fields=['id']
        
        def dict_head(self, head):
            if head['name'] =='content':
                head['width']=300
            return head

class TagForm(ModelFields):
    class Meta:
        model = Tag
        exclude =[]
  

director.update({
    'tag':TagPage.tableCls,
    'tag.edit':TagForm
})

page_dc.update({
    'tag':TagPage
})