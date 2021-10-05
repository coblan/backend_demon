<template>
  <div class="com-contianer">
    <button @click="open_config" v-if="edit">{{title}}</button>
    <slot></slot>
  </div>
</template>
<script>
import draggable from "vuedraggable"
import flexPannel from "./flexPannel.vue";

export  default  {
  props:{
    title:{},
    configHeads:{
      default:()=>[]
    },
    row:{
      default:()=>{}
    }
  },

  data(){
    // var parStore = ex.vueParStore(this)
    var childStore = new Vue()
    childStore.vc = this
    childStore.name='comContainer'
    return {
      childStore:childStore,
      rootStore:ex.vueParStore(this,{name:'blockEditorStore'})
      // name:this.ctx.index,
      // parStore:parStore,
    }
  },
  computed:{
    edit(){
      return this.rootStore.vc.is_prod
    }
  },
  methods:{
    open_config(){
      // this.$emit('pop-config')
      var self = this
      var fields_ctx = {
        heads:this.configHeads,
        row:this.row,
        ops:[
          {'editor':'com-btn',
            'label':'确定',
            'click_express':'var pp = ex.vueParStore(scope.vc,{name:"comContainer"}); pp.vc.save_row(scope.ps.vc.row);scope.ps.vc.$emit("finish")'}
        ],
        ops_loc:'bottom',
        genVc:self,
        title:this.title
      }
      cfg.pop_vue_com('com-form-one',fields_ctx,{shade:0,maxmin: true,offset:'rt',area:['500px','500px']})
    },
    save_row(row){
      // this.$emit('save-row',row)
      this.$emit('update:row',row)
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