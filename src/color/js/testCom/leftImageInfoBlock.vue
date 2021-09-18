<template>
  <div>
    <button @click="open_config">leftImageInfo</button>
    <div>
      {{ctx.lay_row.data_src}}
    </div>
<!--    <leftImgInfo :fa="ctx.fa" :title="ctx.title"  :info="ctx.info" :type="ctx.type"></leftImgInfo>-->
  </div>
</template>
<script>
import leftImgInfo from  'webcase/director/statistic/leftImgInfo.vue'
export  default  {
  props:['ctx'],
  components:{
    leftImgInfo
  },
  data(){
    return {
      parStore:ex.vueParStore(this),
    }
  },
  methods:{
    open_config(){
      ex.vueAssign(this.ctx.lay_row,this.parStore.vc.ctx.lay_row)
      var fields_ctx ={
        heads:[
          {'editor':'com-field-linetext','label':'数据源','name':'data_src'},
        ],
        row:this.ctx.lay_row,
        ops:[
          {'editor':'com-btn','label':'确定','click_express':'scope.ps.vc.ctx.genVc.save_row(scope.ps.vc.row);scope.ps.vc.$emit("finish")'}
        ],
        genVc:self
      }
      cfg.pop_vue_com('com-form-one',fields_ctx,{shade:0,maxmin: true,offset:'rt',area:['500px','500px']})

    }
  }
}
</script>