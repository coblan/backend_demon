import * as palette from './table_editor/palette'
import * as color from './table_editor/color'

import  block_editor from './block_page.vue'

Vue.component('block-editor-page',block_editor)

import  flexDiv from './testCom/flexDiv.vue'
import  colorDiv from './testCom/colorDiv.vue'
Vue.component('block-flexDiv',flexDiv)
Vue.component('block-colorDiv',colorDiv)