from helpers.director.shortcut import director_view

ui_component = [
    {'value':'com-ui-test','label':'测试组件',}
]

@director_view('uieditor/components/all')
def get_ui_compnent():
    return ui_component