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
    getFields(){
      return [
        {name:'text',label:'ss',editor:'com-field-linetext'}
      ]
    }
  },
}
</script>
