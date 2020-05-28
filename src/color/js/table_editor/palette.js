
var my_click = {
    // head: {fun:'xxx'}
    props:['rowData','field','index'],
    template:`<div class="com-table-palette" style="display: inline-block">
    <span v-for="color in mycolor" style="display: inline-block;width: 20px;height: 20px;margin: 2px;border-radius: 10px;" :style="{background:get_backgroud(color)}"></span>
        <!--<component v-if="head.inn_editor"-->
            <!--:is="head.inn_editor"-->
            <!--:row-data="rowData" :field="field" :index="index"></component>-->
        <!--<span v-else="" v-text="rowData[field]" ></span>-->
    </div>`,
    created:function(){
        // find head from parent table
        var table_par = this.$parent
        while (true){
            if (table_par.heads){
                break
            }
            table_par = table_par.$parent
            if(!table_par){
                break
            }
        }
        this.table_par = table_par
        this. head  = ex.findone(this.table_par.heads,{name:this.field})

        this.parStore = ex.vueParStore(this)
    },
    computed:{
        mycolor(){
            if(this.rowData[this.field]){
                return JSON.parse(this.rowData[this.field])
            }else{
                return []
            }
        }
    },
    methods:{
        get_backgroud(color){
            if(color.color2){
                return `linear-gradient(${color.color1}, ${color.color2})`
            }else{
                return color.color1
            }
        },
        on_click:function(){
            ex.eval(this.head.action,{row:this.rowData,head:this.head,ps:this.parStore})
            //this.$emit('on-custom-comp',{name:this.head.fun,row:this.rowData,head:this.head})
        }
    }
}

Vue.component('com-table-palette',my_click)
