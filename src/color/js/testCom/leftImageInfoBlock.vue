<template>
  <div>
    <div>
      bb
    </div>
<!--    <leftImgInfo :fa="ctx.fa" :title="ctx.title"  :info="ctx.info" :type="ctx.type"></leftImgInfo>-->
  </div>
</template>
<script>
import leftImgInfo from  'webcase/director/statistic/leftImgInfo.vue'
export  default  {
  props:['ctx'],
  components:{
    leftImgInfo
  }
}
</script>