<template>
  <div>
      test {{text}}
  </div>
</template>
<script>
export default {
  props:{
    text:{}
  },
  methods:{
  },
  label:'测试组件',
  fields(){
    return [
      {name:'text',label:'ss',editor:'com-field-linetext'}
    ]
  }
}
</script>
