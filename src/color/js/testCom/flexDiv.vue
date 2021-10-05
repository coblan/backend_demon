<template>
<!--  <div class="flex-div">-->
    <comDragableContainer :com-list="ctx.com_list"
                          group-name="flexPannel"
                          title="flexDiv"
                          :com-options="opitons"
                          :configHeads="config_heads"
                          :row.sync="ctx.row"
                          >
<!--      @pop-config="open_config"-->
    </comDragableContainer>
<!--  </div>-->
</template>
<script>
import flexPannel from "./flexPannel.vue";
import comDragableContainer from "./comDragableContainer.vue";
export  default  {
  props:['ctx'],
  components:{
    comDragableContainer
  },
  data(){
    return {
      name:this.ctx.index,
      opitons:[
        {'editor':'block-colorDiv','label':'colorDiv',row:{}}
      ],
      config_heads:[
        {'name':'data_src','label':'数据源','editor':'com-field-linetext'},
      ]

    }
  },
  methods:{
    open_config(){
      // cfg.pop_vue_com(flexPannel,{genVc:this},{shade:0,maxmin: true,offset:'rt',area:['500px','500px']})
    }
  }
}
</script>
<style scoped lang="scss">
.flex-div{
  border: 1px solid #c9c8c8;
  .list-group{
    display: flex;
    flex-direction: row;
  }
}
</style>