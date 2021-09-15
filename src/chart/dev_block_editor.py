from helpers.director.shortcut import page_dc

class BlockEditorBuilder(object):
    def __init__(self, *args, **kwargs):
        pass
    
    def get_template(self):
        return 'jb_admin/live.html'
    
    def get_context(self):
        return {
            'editor':'block-editor-page',
            'editor_ctx':{
                
            }
        }
    
page_dc.update({
    'blockeditor':BlockEditorBuilder
})