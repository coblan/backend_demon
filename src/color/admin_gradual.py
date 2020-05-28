from .admin_palette import PalettePage,PaletteForm
from helpers.director.shortcut import page_dc,director

class GradualPage(PalettePage):
    class tableCls(PalettePage.tableCls):
        def inn_filter(self, query):
            return query.filter(kind =1)

class GradualForm(PaletteForm):
    
    def dict_head(self, head):
        if head['name'] =='colors':
            head.update({
                'editor':'com-field-table-list',
                'table_heads':[{'name':'color1','label':'色彩1','editor':'com-table-pop-fields-local'},
                               {'name':'show_color1','label':'色彩1','editor':'com-table-color-color','value_field':'color1'},
                               {'name':'color2','label':'色彩2'},
                               {'name':'show_color2','label':'色彩2','editor':'com-table-color-color','value_field':'color2'},
                               {'name':'order','label':'','editor':'com-table-change-order'}],
                'fields_heads':[{'name':'color1','label':'色彩1','editor':'com-field-color','required':True},
                                {'name':'color2','label':'色彩2','editor':'com-field-color','required':True}]
                })
        return head
    def clean_save(self):
        self.instance.kind =1

director.update({
    'gradual':GradualPage.tableCls,
    'gradual.edit':GradualForm,
})

page_dc.update({
    'gradual':GradualPage
})