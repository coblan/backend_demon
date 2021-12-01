from helpers.director.shortcut import FieldsPage,director,Fields,page_dc,director_view
from helpers.director.kv import get_value,set_value

class MyJsonPage(FieldsPage):
    def get_label(self):
        return '我的json'
    
    def get_template(self, prefer=None):
        return 'jb_admin/fields.html'
    
    class fieldsCls(Fields):
        def get_heads(self):
            return [
                {'name':'content','label':'内容','editor':'com-field-blocktext'}
            ]
        
        def dict_row(self):
            return {
                'content':get_value('my-json','')
            }
        
        def save_form(self):
            set_value('my-json',self.kw.get('content'))
        
@director_view('myjson/value')
def getMyjson():
    return get_value('my-json')

director.update({
    'myjson':MyJsonPage.fieldsCls
})

page_dc.update({
    'myjson':MyJsonPage
})