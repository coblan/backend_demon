from helpers.director.shortcut import TablePage,ModelTable,ModelFields,page_dc,director,get_request_cache
from . models import Page

class PagePage(TablePage):
    def get_label(self):
        return '页面管理'
    
    def get_template(self, prefer=None):
        return 'jb_admin/table_new.html'
    
    class tableCls(ModelTable):
        model = Page
        exclude =[]
        pop_edit_fields =['name']
        
        
        def get_head_context(self):
            get_request_cache()['named_ctx'].update({
                          'order-page-tabs':[
                              {'name':'uitest',
                              'label':'ui测试',
                               'editor':'com-tab-ui-editor',
                             
                               },
         
                          ]
                      })   
            ctx = super().get_head_context()
            return ctx
        
        def dict_head(self, head):
            if head['name']=='content':
                head['editor'] = 'com-table-click'
                head['click_express']="scope.ps.switch_to_tab({ctx_name:'order-page-tabs',tab_name:'uitest',par_row:scope.row})"
            return head

class PageForm(ModelFields):
    class Meta:
        model = Page
        exclude =[]
    
    def dict_head(self, head):
        if head['name'] == 'content':
            head['editor'] = 'com-field-json-edit'
        return head

director.update({
    'webpage':PagePage.tableCls,
    'webpage.edit':PageForm
})

page_dc.update({
    'webpage':PagePage
})