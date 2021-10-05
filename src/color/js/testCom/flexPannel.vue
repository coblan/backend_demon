<template>
  <div>
    <comBasket :com-list="com_list" group-name="flexPannel"></comBasket>
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
    return {
      com_list:[
        {'editor':'block-colorDiv','label':'colorDiv',row:{}}
      ],
      fields_ctx:{
        heads:[
          {'name':'data_src','label':'数据源','editor':'com-field-linetext'},
        ],
        row:{
          data_src:this.ctx.data_src,
        },
      }
    }
  },
  methods:{

  }
}
</script>
