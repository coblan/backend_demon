<template>
  <div>
    <floatEditTrigger v-for="head in bus.coms"  :row.sync="head.bind" v-if="head.bind && head.editor"
                  canEdit="true" @change="onChanged">
      <component refs="mycom" :is="getField( head.editor)" v-bind="head.bind"></component>
    </floatEditTrigger>
<!--      <component v-for="ii in bus.coms" :is="ii.editor" :bind="ii.bind"> </component>-->
  </div>
</template>
<script>
import floatEditTrigger from "./floatEditTrigger.vue";

export default {
  props:{
    bus:{} // {'editor':resp.editor,label:resp.label}
  },
  components:{
    floatEditTrigger
  },
  methods:{
    onChanged(){

    },
    getField(field_str){
      return cfg.uicoms[field_str]
    }
  }
}
</script>