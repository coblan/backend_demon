<template>
  <div>
    <comBasket :com-list="ctx.comOptions" :group-name="ctx.groupName"></comBasket>
    <com-form-one :ctx="fields_ctx"></com-form-one>
  </div>
</template>
<script>
import blockSettingMix from "./blockSettingMix.js";
import comBasket  from "./comBasket.vue";
export  default  {
  components:{
    comBasket
  },
  props:['ctx'],
  data(){
    if(this.ctx.appendOps){

    }
    return {
      childStore:new Vue(),
      fields_ctx:{
        heads:[
          {'name':'layout','label':'layout','editor':'com-field-select','options':[
              {'value':'flex-column','label':'flex-垂直'},
              {'value':'flex-row','label':'flex-水平'},

            ]}
        ].concat(this.ctx.configHeads),
        row:this.ctx.row,
        ops:[
          {'editor':'com-btn',
            'label':'确定',
            'click_express':'scope.ps.vc.ctx.genVc.save_row(scope.ps.vc.row);scope.ps.vc.$parent.$emit("finish")'}
        ].concat( this.ctx.appendOps),
        ops_loc:'bottom',
        genVc:this.ctx.genVc,
        title:this.ctx.title
      }
    }
  },
  methods:{

  }
}
</script>
