<template>

  <comContainer
      title="color"
      :config-heads="config_heads"
      :row.sync="ctx.row"
      class="left-info-block"
  >
<!--    <div>-->
<!--        {{ctx.row.myfield}}-->
<!--        {{parStore.vc.ctx.row.data_resp[ctx.row.myfield]}}-->
<!--    </div>-->
    <leftImgInfo :fa="ctx.row.fa"
                 :title="ctx.row.title"
                 :info="parStore.vc.ctx.row.data_resp[ctx.row.myfield]"
                 :type="ctx.row.type"></leftImgInfo>

  </comContainer>
</template>
<script>
import leftImgInfo from  'webcase/director/statistic/leftImgInfo.vue'
import comContainer from "./comContainer.vue";
export  default  {
  props:['ctx'],
  components:{
    leftImgInfo,
    comContainer,
  },
  data(){
    var parStore = ex.vueParStore(this,{name:'leftImageInfoContainer'})
    return {
      parStore:parStore,
    }
  },
  computed:{
    config_heads(){
      return [
        {'editor':'com-field-select','label':'字段','name':'myfield',
          'options': ex.map(Object.keys(this.parStore.vc.ctx.row.data_resp),item=>{ return {value:item,label:item}} )
        },
        {'editor':'com-field-linetext','label':'图表','name':'fa',},
        {'editor':'com-field-linetext','label':'标题','name':'title',},
        {'editor':'com-field-linetext','label':'类型','name':'type',},
      ]
    }
  },
  methods:{
  }
}
</script>
<style scoped lang="scss">
.left-info-block{
  margin: 20px;
}
</style>