<template>
  <div>
    <slot></slot>

  </div>

</template>
<script>
export default {
  props:{

  },
  methods:{
    drop_handler(ev) {
      ev.preventDefault();
      // Get the id of the target and add the moved element to the target's DOM
      // var data = ev.dataTransfer.getData("text/plain");
      var data = ev.dataTransfer.getData('Text')
      this.com_list.push((JSON.parse(data)))
      this.next_com ={}
      window._drag_data ={}
    },
    drag_enter(ev){
      // console.log('enter')
      ev.preventDefault();
      // if(window._drag_data){
      //   this.next_com = window._drag_data
      // }
      // var data = ev.dataTransfer.getData('Text')
      //
      // if(data){
      //   debugger
      //   this.next_com = JSON.parse(data)
      // }

    },
    drag_leave(ev){
      this.next_com ={}
      ev.preventDefault();
    },

  }
}
</script>