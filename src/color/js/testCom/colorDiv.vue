<template>
  <div class="color-div" :style="mystyle">
    <button @click="config_com">color</button>
  </div>
</template>
<script>
export  default  {
  props:['ctx'],
  data(){
    if(!this.ctx.row.first){
      ex.vueAssign( this.ctx.row,{
        bg_color:'red',
        width:200,
        height:200,
        first:1,
      })
    }

    return {

    }
  },
  computed:{
    mystyle(){
      return {
          background:this.ctx.row.bg_color,
          width:`${this.ctx.row.width}px`,
          height: `${this.ctx.row.height}px`,
      }
    }
  },
  methods:{
    config_com(){
      var self = this
      var fields_ctx = {
        heads:[
          {'name':'bg_color','label':'颜色','editor':'com-field-color'},
          {'name':'width','label':'宽','editor':'com-field-int'},
          {'name':'height','label':'高','editor':'com-field-int'},
        ],
        row:this.ctx.row,
        ops:[
          {'editor':'com-btn','label':'确定','click_express':'scope.ps.vc.ctx.genVc.save_row(scope.ps.vc.row);scope.ps.vc.$emit("finish")'}
        ],
        ops_loc:'bottom',
        genVc:self
      }
      // cfg.pop_vue_com('com-local-form',fields_ctx)
      cfg.pop_vue_com('com-form-one',fields_ctx,{shade:0,maxmin: true,})
    },
    save_row(row){
      ex.vueAssign(this.ctx.row,row)
      // this.bg_color = row.bg_color
    }
  }
}
</script>
<style lang="scss" scoped>

.color-div{
  //background-color: red;
  //height: 100px;
  //width: 100px;
}
</style>