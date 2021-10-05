<template>

  <comContainer
      title="color"
      :config-heads="config_heads"
      :row.sync="ctx.row"
      class="left-info-block"
  >
    <h2>{{ctx.row.title}}</h2>
  </comContainer>
</template>
<script>

import comContainer from "./comContainer.vue";
export  default  {
  props:['ctx'],
  components:{
    comContainer,
  },
  data(){
    // var parStore = ex.vueParStore(this,{name:'leftImageInfoContainer'})
    return {
      // parStore:parStore,
    }
  },
  computed:{
    config_heads(){
      return [
        {'editor':'com-field-linetext','label':'标题','name':'title',},
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