from helpers.director.shortcut import page_dc,director,ModelFields,ModelTable,TablePage,director_view
from helpers.director.table.treeTable import TreeTable
from .models import TBDepartment
class DepartmentPage(TablePage):
    def get_label(self):
        return '部门管理'

    def get_template(self, prefer=None):
        return 'jb_admin/table_new.html'

    class tableCls(TreeTable):
        first_field='name'
        model = TBDepartment
        exclude = []
 
        hide_fields=['parent','path','id']
        pop_edit_fields = ['name']

class DepartForm(ModelFields):
    class Meta:
        model = TBDepartment
        exclude =[]

director.update({
    'depart3':DepartmentPage.tableCls,
    'depart3.edit':DepartForm,
})
page_dc.update({
    'depart3':DepartmentPage
})