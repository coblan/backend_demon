from helpers.director.shortcut import director,ModelFields,ModelTable,TablePage,page_dc,RowFilter,RowSearch,FieldsPage,field_map
from helpers.director.model_func.dictfy import to_dict
from .models import TBEmployee,TBDepartment
from django.contrib.auth.models import Group,User
#from . wxweb_engin import wxweb_page
from .admin_department import DepartmentTable
from helpers.mobile.table import ModelTableMobile
from helpers.case.jb_admin.admin_user import UserFields
from helpers.director.model_func.field_proc import BaseFieldProc
from helpers.director.middleware.request_cache import request_cache
from helpers.director.shortcut import director_view

class EmployeePage(TablePage):
    def get_label(self):
        return '员工管理'
    
    def get_template(self, prefer=None):
        return 'jb_admin/table_new.html'
    
    class tableCls(ModelTable):
        model = TBEmployee
        exclude =[]
        pop_edit_fields = ['name','user']
        
        #def getExtraHead(self):
            #return [
                #{'name':'permit_group',
                 #'label':'权限组',
                 #'editor':'com-table-array-mapper',
                 #'options':[{'value':x.pk,'label':str(x)} for x in Group.objects.all()]},
                #]
        
        def dict_head(self, head):
            width_dc = {
                'user':150,
                'permit_group':200,
                'mobile':150,
            }
            if width_dc.get(head['name']):
                head['width'] = width_dc[head['name']]
            #if head['name']=='name':
                #head['fields_ctx'].update({
                    #'init_express':'cfg.show_load();ex.director_call(scope.vc.ctx.director_name,{pk:scope.vc.par_row.pk}).then((res)=>{cfg.hide_load();ex.vueAssign(scope.row,res)})',
                #})
            
            if head['name'] == 'user':
                head['inn_editor'] = 'com-table-label-shower'
                head['fields_ctx'] ={
                    'init_express':'cfg.show_load();ex.director_call(scope.vc.ctx.director_name,{pk:scope.vc.par_row.user}).then((res)=>{cfg.hide_load();ex.vueAssign(scope.row,res.row)})',
                    'after_save':'scope.vc.par_row.user=scope.row.pk;scope.vc.par_row._user_label=scope.row._label',
                    **UserFields().get_head_context()
                }
                
            return head
        
        
        class filters(RowFilter):
            names = ['name',]
            icontains = ['name']
            fields_sort=['name','my_depart','include_children']
            def getExtraHead(self):
                return [
                    {'name':'my_depart','label':'部门','editor':'com-filter-cascasder','options':get_depart_option()},
                    {'name':'include_children','label':'包含下级','editor':'com-filter-select','options':[
                        {'value':1,'label':'包含'},{'value':0,'label':'不包含'}
                    ]}
                ]
            
            
            def get_query(self, query):
                query = super().get_query(query)
                if not self.kw.get('my_depart'):
                    return query
                if self.kw.get('include_children',1):
                    depart = TBDepartment.objects.get(pk = self.kw.get('my_depart'))
                    return query.filter(depart__path__startswith=depart.path)
                else:
                    return query.filter(depart_id=self.kw.get('my_depart'))
            
            
class EmployeeForm(ModelFields):
    class Meta:
        model = TBEmployee
        exclude =[]
    
    def clean_save(self):
        if 'name' in self.changed_data and self.instance.user:
            self.instance.user.first_name = self.cleaned_data.get('name')
            self.instance.user.save()
        #user = User.objects.get(pk = self.kw.get('user'))
        #user.groups.clear()
        #for g in self.kw.get('permit_group',):
            #user.groups.add(g)
    
    #def getExtraHeads(self):
        #return [
            #{'name':'permit_group',
             #'label':'权限组',
             #'editor':'com-field-multi-select2',
             #'options':[{'value':x.pk,'label':str(x)} for x in Group.objects.all()],
             #'help_text':'选择适当的权限组，将赋予该监督员相应的权限。'
             #}
        #]
    
    #def clean_dict(self, dc):
        #if dc.get('depart'):
            #dc['depart'] = dc.get('depart')
        #return dc
    
    def dict_head(self, head):
        if head['name'] == 'user':
            head['editor'] ='com-field-single-select2'
        if head['name']=='depart':
            head['editor'] ='com-field-cascader'
            #ls =[]
            #dc={}
            #for dep in TBDepartment.objects.all():
                #tmp = {'value':dep.pk,'label':dep.name,'parent':dep.parent_id}
                #ls.append(tmp)
                #dc[dep.pk] = tmp
            #while True:
                #find_all=True
                #index = len(ls)
                #for dep in list(reversed(ls)):
                    #index -=1
                    #if dep.get('parent'):
                        #if 'children' not in dc[dep.get('parent')]:
                            #dc[dep.get('parent')]['children']=[]
                        #dc[dep.get('parent')]['children'].append(dep)
                        #ls.pop(index)
                        #find_all=False
                #if find_all:
                    #break
            head['options']=get_depart_option()
        return head
    
    #def dict_row(self, inst):
        ##if hasattr(inst,'user'):
            ##permit_group = [x.pk for x in inst.user.groups.all()]
        ##else:
            ##permit_group = []
        #out_depart = []
        #last_dep = inst.depart
        #while last_dep:
            #out_depart.append(last_dep.pk)
            #if last_dep.parent:
                #last_dep=last_dep.parent
            #else:
                #break
        #out_depart.reverse()    
        #return {
            ##'permit_group':permit_group,
            #'depart':out_depart
        #}

@request_cache
def get_depart_option():
    ls =[]
    dc={}
    for dep in TBDepartment.objects.all():
        tmp = {'value':dep.pk,'label':dep.name,'parent':dep.parent_id}
        ls.append(tmp)
        dc[dep.pk] = tmp
    while True:
        find_all=True
        index = len(ls)
        for dep in list(reversed(ls)):
            index -=1
            if dep.get('parent'):
                if 'children' not in dc[dep.get('parent')]:
                    dc[dep.get('parent')]['children']=[]
                dc[dep.get('parent')]['children'].append(dep)
                ls.pop(index)
                find_all=False
        if find_all:
            break
    return ls

class EmployeSearchPicker(ModelTableMobile):
    model = TBEmployee
    exclude=[]
    fields_sort=['name']
    
    def get_head_context(self):
        ctx = super().get_head_context()
        ctx['block_click'] ='scope.ps.vc.ctx.par_row.staff= scope.row.user; scope.ps.vc.ctx.par_row._staff_label=scope.row.name ; history.back()'
        #ctx['block_click'] ='alert("jj")'
        return ctx
    
    class filters(RowFilter):
        names=['name']
        icontains=['name']
        
    #def dict_head(self, head):
        #head['action'] ='(function(){ scope.ps.par_row.staff= scope.row.user; scope.ps.par_row._staff_label=scope.row.name ; history.back() })() '
        #return head
    
    #class search(RowSearch):
        #def get_query(self, query):
            #return query.filter(name__icontains = self.q)


class StaffInfoSelf(FieldsPage):
    def get_template(self, prefer=None):
        return 'mobile/fields.html'
    
    def get_label(self):
        return '员工信息'
    
    class fieldsCls(ModelFields):
        nolimit=True
        def __init__(self, *args, **kw):
            super().__init__(*args, **kw)
            self.instance = TBEmployee.objects.get(user = self.crt_user)
            
        class Meta:
            model = TBEmployee
            exclude =['user']
        
        def dict_head(self, head):
            if head['name'] == 'birthday':
                head['start'] = '1910-01-01'
                head['init_value'] = '1990-01-01'
                head['end']= '2010-01-01'
            if head['name'] == 'depart':
                head['editor'] = 'com-field-tree-select'
                head['table_ctx'] = DepartmentTable().get_head_context()
                head['title']='部门选择'
            if head['name'] == 'head':
                head['maxspan'] = 400
            return head
        
        
        def get_operations(self):
            return [
            {'label':'确定','editor':'com-op-submit','action':'''rt=scope.ps.vc.submit()
                        .then((res)=>{ cfg.showMsg("提交成功!")})'''},
            ]
            #ops = super().get_operations()
            #for op in ops:
                #op['editor'] = 'com-op-submit'
            #return ops
    
    
#wxweb_page.update({
    #'staffinfo':StaffInfoSelf,
#})  


director.update({
    'employee':EmployeePage.tableCls,
    'employee.edit':EmployeeForm,
    'employee_picker':EmployeSearchPicker,
    
    'staffinfo':StaffInfoSelf.fieldsCls
})

page_dc.update({
    'employee':EmployeePage
})