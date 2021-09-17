from helpers.director.shortcut import director_view
from helpers.director.kv import get_value,set_value

@director_view('save_test_com_list')
def save_test_com_list(com_list):
    set_value('dev_com_list',com_list)
    
@director_view('get_test_com_list')
def get_test_com_list():
    return get_value('dev_com_list')