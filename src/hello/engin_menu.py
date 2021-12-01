# encoding:utf-8

from __future__ import unicode_literals
from helpers.director.shortcut import page_dc
from helpers.director.engine import BaseEngine, page, fa, can_list, can_touch
from django.contrib.auth.models import User, Group
from helpers.func.collection.container import evalue_container

from django.utils.translation import ugettext as _
from django.conf import settings
from helpers.director.access.permit import has_permit

#from . import permit


class PcMenu(BaseEngine):
    url_name = 'enterprise'
    title = '后台演示' 
    brand = 'x' 
    mini_brand = 'XCL'
    menu_search=False
    need_staff=True
    access_from_internet=True
    @property
    def menu(self):
        crt_user = self.request.user
        menu = [
            #{'label': 'HOME', 'url': page('home'), 'icon': fa('fa-home'), 'visible': True},
            {'label': 'HOME', 'url': page('enginhome'), 'icon': fa('fa-home'), 'visible': True},
            {'label': '机构管理', 'icon': fa('fa-users'), 'visible': True,
             'submenu': [
                {'label':'人员', 'url': page('employee'), },
                {'label':'部门', 'url': page('department'), },
             ]},
            {'label':'色彩图片','icon':fa('fa-dashboard'),
             'submenu':[
                 {'label':'单色调色板','url':page('palette')},
                 {'label':'渐变调色板','url':page('gradual')},
                 {'label':'图片','url':page('image')},
                 {'label':'图片组','url':page('imagegroup_grid')}
                 ]},
            
            {'label':'构建器','url':page('blockeditor'),'icon': fa('fa-users')},
            
            {'label': '系统管理', 'icon': fa('fa-gear'), 'visible': True,
             'submenu': [
                 {'label': '微信用户', 'url': page('wxuserinfo'), 'visible': can_touch(Group, crt_user)},
                 {'label': '账号管理', 'url': page('jb_user'), 'visible': can_touch(User, crt_user)},
                 {'label': '权限分组', 'url': page('jb_group'), 'visible': can_touch(Group, crt_user)},
                   {'label': '临时数据', 'url': page('myjson'), 'visible': can_touch(Group, crt_user)},
                 
             ]},

        ]

        return menu

    def custome_ctx(self, ctx):
        if 'extra_js' not in ctx:
            ctx['extra_js'] = []
        ctx['extra_js'].append('color')

        return ctx


PcMenu.add_pages(page_dc)


