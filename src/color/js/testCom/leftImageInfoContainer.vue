<template>
  <comDragableContainer
      :com-list="ctx.com_list"
      group-name="leftImageInfo"
      title="LeftInfo"
      :com-options="com_options"
      :configHeads="config_heads"
      :row.sync="ctx.row"
      :append-ops="append_ops"
  >
  </comDragableContainer>
</template>
<script>
import leftImageInfoPannel from "./leftImageInfoPannel.vue";
import comDragableContainer from "./comDragableContainer.vue";
export  default  {
  components:{
    comDragableContainer
  },
  props:['ctx'],
  data(){
    var self = this
    // const childStore = new Vue({
    //   data:{
    //     vc:self,
    //     name:'leftImageInfoContainer'
    //   }
    // })
    var childStore = new Vue()
    childStore.vc = this
    childStore.name='leftImageInfoContainer'
    return {
      parStore:ex.vueParStore(this),
      childStore:childStore,
      // blockEditorStore:ex.vueParStore(this,{name:'blockEditorStore'}),
      com_options:[
        {'editor':'block-leftImageInfo','label':'leftImageInfo',row:{}},
      ],
      config_heads:[
        {'name':'data_src','label':'数据源','editor':'com-field-linetext'},
      ],
      append_ops:[
        {'editor':'com-btn','label':'获取数据','click_express':'debugger;var pp = ex.vueParStore(scope.vc,{name:"leftImageInfoContainer"});pp.vc.getData(scope.ps.vc.row)'},
      ]
      // com_list:[ ],
    }
  },
  methods:{
    getData(row){
      cfg.show_load()
      ex.director_call('get_today_info',{}).then(resp=>{
        row.data_resp = resp
        this.ctx.row.data_resp = resp
        cfg.hide_load()
      })
    },
    removeSelf(){
      this.parStore.vc.removeChildren(this.ctx.index)
    }
  }
}
</script>
