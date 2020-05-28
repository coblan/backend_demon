/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;
/******/
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// identity function for calling harmony imports with the correct context
/******/ 	__webpack_require__.i = function(value) { return value; };
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 2);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var my_click = {
    // head: {fun:'xxx'}
    props: ['rowData', 'field', 'index'],
    template: '<div class="com-table-color-color" style="display: inline-block">\n    <span style="display: inline-block;width: 20px;height: 20px;margin: 2px;border-radius: 10px;" :style="{background:mycolor}"></span>\n    </div>',
    created: function created() {
        // find head from parent table
        var table_par = this.$parent;
        while (true) {
            if (table_par.heads) {
                break;
            }
            table_par = table_par.$parent;
            if (!table_par) {
                break;
            }
        }
        this.table_par = table_par;
        this.head = ex.findone(this.table_par.heads, { name: this.field });

        this.parStore = ex.vueParStore(this);
    },
    computed: {
        mycolor: function mycolor() {
            if (this.head.value_field) {
                var value = this.rowData[this.head.value_field];
            } else {
                var value = this.rowData[this.field];
            }
            return value;
            //if(this.rowData[this.field]){
            //    return this.rowData[this.field]
            //}else{
            //    return ''
            //}
        }
    }
};

Vue.component('com-table-color-color', my_click);

/***/ }),
/* 1 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var my_click = {
    // head: {fun:'xxx'}
    props: ['rowData', 'field', 'index'],
    template: '<div class="com-table-palette" style="display: inline-block">\n    <span v-for="color in mycolor" style="display: inline-block;width: 20px;height: 20px;margin: 2px;border-radius: 10px;" :style="{background:get_backgroud(color)}"></span>\n        <!--<component v-if="head.inn_editor"-->\n            <!--:is="head.inn_editor"-->\n            <!--:row-data="rowData" :field="field" :index="index"></component>-->\n        <!--<span v-else="" v-text="rowData[field]" ></span>-->\n    </div>',
    created: function created() {
        // find head from parent table
        var table_par = this.$parent;
        while (true) {
            if (table_par.heads) {
                break;
            }
            table_par = table_par.$parent;
            if (!table_par) {
                break;
            }
        }
        this.table_par = table_par;
        this.head = ex.findone(this.table_par.heads, { name: this.field });

        this.parStore = ex.vueParStore(this);
    },
    computed: {
        mycolor: function mycolor() {
            if (this.rowData[this.field]) {
                return JSON.parse(this.rowData[this.field]);
            } else {
                return [];
            }
        }
    },
    methods: {
        get_backgroud: function get_backgroud(color) {
            if (color.color2) {
                return 'linear-gradient(' + color.color1 + ', ' + color.color2 + ')';
            } else {
                return color.color1;
            }
        },

        on_click: function on_click() {
            ex.eval(this.head.action, { row: this.rowData, head: this.head, ps: this.parStore });
            //this.$emit('on-custom-comp',{name:this.head.fun,row:this.rowData,head:this.head})
        }
    }
};

Vue.component('com-table-palette', my_click);

/***/ }),
/* 2 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var _palette = __webpack_require__(1);

var palette = _interopRequireWildcard(_palette);

var _color = __webpack_require__(0);

var color = _interopRequireWildcard(_color);

function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) newObj[key] = obj[key]; } } newObj.default = obj; return newObj; } }

/***/ })
/******/ ]);