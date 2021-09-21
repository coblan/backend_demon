<template>
  <div>
    <draggable
        class="dragArea list-group"
        :list="com_list"
        :group="{ name: 'leftImageInfo', pull: 'clone', put: false }"
        :clone="cloneDog"
    >
      <div
          class="list-group-item"
          v-for="element in com_list"
          :key="element.editor"
      >
        {{ element.label }}
      </div>
    </draggable>
    <com-form-one :ctx="fields_ctx"></com-form-one>
  </div>
</template>
<script>
import blockSettingMix from "./blockSettingMix.js";

export  default  {
  props:['ctx'],
  data(){

    return {
      com_list:[
        {'editor':'block-leftImageInfo','label':'block-leftImageInfo',lay_row:{}},
      ],
      fields_ctx:{
        heads:[
          {'name':'data_src','label':'数据源','editor':'com-field-linetext'},
        ],
        row:this.ctx.lay_row,
        ops:[
          {'editor':'com-btn','label':'获取数据','click_express':'scope.ps.vc.$parent.getData(scope.ps.vc.row)'},
          {'editor':'com-btn','label':'删除','click_express':'scope.ps.vc.$parent.ctx.genVc.removeSelf()'},
          {'editor':'com-btn','label':'确定','click_express':'scope.ps.vc.$parent.ctx.genVc.save_row(scope.ps.vc.row);scope.ps.vc.$parent.$emit("finish")'}

        ],
      }
    }
  },
  mixins:[blockSettingMix],
  methods:{
    // cloneDog(node){
    //   this.ctx.genVc.blockEditorStore.count +=1
    //   var node1= ex.copy(node)
    //   node1.index= this.ctx.genVc.blockEditorStore.count
    //   return node1
    // },
    getData(row){
      cfg.show_load()
      ex.director_call('get_today_info',{}).then(resp=>{
        row.data_resp = resp
        cfg.hide_load()
      })
    }
  }
}
</script>
