from helpers.director.shortcut import TablePage,ModelTable,ModelFields,page_dc,director,RowFilter,director_view
from .models import Palette
from helpers.director.model_func.dictfy import sim_dict
import json

class PalettePage(TablePage):
    def get_label(self):
        return '色盘管理'
    
    def get_template(self, prefer=None):
        return 'jb_admin/table.html'
    
    class tableCls(ModelTable):
        model = Palette
        exclude = []
        pop_edit_fields=['id']
        
        def inn_filter(self, query):
            return query.filter(kind=0)
        
        def dict_head(self, head):
            if head['name'] =='colors':
                head['editor'] = 'com-table-palette'
                head['width'] = 400
            return head
        

class PaletteForm(ModelFields):
    hide_fields=['kind']
    class Meta:
        model = Palette
        exclude =[]
    
    def dict_head(self, head):
        if head['name'] =='colors':
            head.update({
                'editor':'com-field-table-list',
                'table_heads':[{'name':'color1','label':'色彩值','editor':'com-table-pop-fields-local'},
                               {'name':'show_color','label':'色彩','editor':'com-table-color-color','value_field':'color1'},
                               {'name':'order','label':'','editor':'com-table-change-order'}],
                'fields_heads':[{'name':'color1','label':'选择色彩','editor':'com-field-color','required':True}]
                })
        return head
    
    def clean_save(self):
        self.instance.kind =0
            
@director_view('palette/all')
def get_palette():
    rows = []
    for inst in Palette.objects.all():
        dc={
            'colors':json.loads(inst.colors) if inst.colors else []
        }
        rows.append(sim_dict(inst,filt_attr=dc))
    return rows

director.update({
    'palette':PalettePage.tableCls,
    'palette.edit':PaletteForm
})

page_dc.update({
    'palette':PalettePage
})