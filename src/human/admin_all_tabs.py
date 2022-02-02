from helpers.director.shortcut import page_dc

class BlockEditorBuilder(object):
    def __init__(self, *args, **kwargs):
        pass
    
    def get_template(self):
        return 'tab_admin/base.html'
    
    def get_context(self):
        return {
            'editor':'',
            'editor_ctx':{
                
            }
        }
    
page_dc.update({
    'taball':BlockEditorBuilder
})