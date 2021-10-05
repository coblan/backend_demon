import * as palette from './table_editor/palette'
import * as color from './table_editor/color'

import  block_editor from './block_page.vue'

Vue.component('block-editor-page',block_editor)

import  flexDiv from './testCom/flexDiv.vue'
import  colorDiv from './testCom/colorDiv.vue'
import  leftImageInfoBlock from './testCom/leftImageInfoBlock.vue'
import  leftImageInfoContainer from './testCom/leftImageInfoContainer.vue'
import h2title from "./testCom/h2title.vue";
Vue.component('block-flexDiv',flexDiv)
Vue.component('block-colorDiv',colorDiv)
Vue.component('block-leftImageInfo',leftImageInfoBlock)
Vue.component('block-leftImageInfoContainer',leftImageInfoContainer)
Vue.component('block-h2-title',h2title)
