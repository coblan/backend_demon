<template>
  <div>
    <button @click="open_config">leftImageInfo</button>
    <div>
      {{ctx.lay_row.myfield}}
      {{parStore.vc.ctx.lay_row.data_resp[ctx.lay_row.myfield]}}
    </div>
<!--    <leftImgInfo :fa="ctx.fa" :title="ctx.title"  :info="ctx.info" :type="ctx.type"></leftImgInfo>-->
    <leftImgInfo :fa="ctx.lay_row.fa"
                 :title="ctx.lay_row.title"
                 :info="parStore.vc.ctx.lay_row.data_resp[ctx.lay_row.myfield]"
                 :type="ctx.lay_row.type"></leftImgInfo>
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
      var self =this
      var fields_ctx ={
        heads:[
          // {'editor':'com-field-linetext','label':'数据源','name':'data_src'},
          {'editor':'com-field-select','label':'字段','name':'myfield','options':ex.map(Object.keys(this.parStore.vc.ctx.lay_row.data_resp),item=>{ return {value:item,label:item}} )},
          {'editor':'com-field-linetext','label':'图表','name':'fa',},
          {'editor':'com-field-linetext','label':'标题','name':'title',},
          {'editor':'com-field-linetext','label':'类型','name':'type',},
        ],
        row:self.ctx.lay_row,
        ops:[
          {'editor':'com-btn','label':'确定','click_express':'scope.ps.vc.ctx.genVc.save_row(scope.ps.vc.row);scope.ps.vc.$emit("finish")'}
        ],
        genVc:self
      }
      cfg.pop_vue_com('com-form-one',fields_ctx,{shade:0,maxmin: true,offset:'rt',area:['500px','500px']})

    },
    save_row(row){
      ex.vueAssign(this.ctx.lay_row,row)
      // Vue.set(this.ctx.lay_row,'myfield',row.myfield)
      // Vue.set(this.ctx.lay_row,'myfield',row.myfield)
      // this.ctx.lay_row.myfield=row.myfield
    }
  }
}
</script>