(window.webpackJsonp=window.webpackJsonp||[]).push([[6],{220:function(t,o,e){var content=e(237);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,e(53).default)("812a4b42",content,!0,{sourceMap:!1})},236:function(t,o,e){"use strict";var n=e(220);e.n(n).a},237:function(t,o,e){(o=e(52)(!1)).push([t.i,"dev.hello{padding:100 px;background-color:red}",""]),t.exports=o},238:function(t,o,e){"use strict";e(54);var n={components:{},name:"app",data:function(){},created:function(){},mounted:function(){this.axios.post("/api/v1/registrations",{username:"user@gmail.com",password:"123456",password2:"123456"}).then((function(t){alert(t.data)}))},methods:{CreateUser:function(){this.$axios.post("https://perspective.local/api/v1/registrations",{username:"dfs@mail.ru",password:"123456",password2:"123456"}).then((function(t){})).catch((function(t){this.error=t}))}}},r=(e(236),e(44)),component=Object(r.a)(n,(function(){var t=this.$createElement;return(this._self._c||t)("dev",{staticClass:"hello",on:{click:this.CreateUser}},[this._v("\nHello Component\n")])}),[],!1,null,null,null);o.a=component.exports},242:function(t,o,e){var content=e(253);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,e(53).default)("544643a4",content,!0,{sourceMap:!1})},252:function(t,o,e){"use strict";var n=e(242);e.n(n).a},253:function(t,o,e){(o=e(52)(!1)).push([t.i,'.form-group,label{margin-bottom:15px}input,input::-webkit-input-placeholder{font-size:11px;padding-top:3px}.form-control{height:auto!important;padding:8px 12px!important}.input-group{box-shadow:0 2px 5px 0 rgba(0,0,0,.21)!important}#button{border:1px solid #ccc;margin-top:28px;padding:6px 12px;color:#666;text-shadow:0 1px #fff;cursor:pointer;border-radius:3px 3px;box-shadow:inset 0 1px #fff,0 1px #ddd;background:#f5f5f5;background:-webkit-gradient(linear,left top,left bottom,from(#f5f5f5),to(#eee));background:linear-gradient(top,#f5f5f5,#eee);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr="#f5f5f5",endColorstr="#eeeeee",GradientType=0)}.main-form{margin:0 auto;max-width:400px;padding:10px 40px;background:rgba(255,136,0,.99608);color:#fff;text-shadow:none;box-shadow:0 3px 5px 0 rgba(0,0,0,.31)}span.input-group-addon i{color:rgba(255,136,0,.99608);font-size:17px}.login-button{margin-top:5px}',""]),t.exports=o},269:function(t,o,e){"use strict";e.r(o);var n,r=e(0),l=(e(55),e(19)),c=(e(238),e(54),n={components:{},name:"app",data:function(){}},Object(r.a)(n,"data",(function(){return{data:{urls:"/api/v1/auth/login/",username:!1,email:!1,password:!1,msg:""}}})),Object(r.a)(n,"created",(function(){})),Object(r.a)(n,"mounted",(function(){})),Object(r.a)(n,"methods",{loginUser:function(){var t=this;return Object(l.a)(regeneratorRuntime.mark((function o(){var data;return regeneratorRuntime.wrap((function(o){for(;;)switch(o.prev=o.next){case 0:return data={email:t.email,password:t.password},o.prev=1,o.next=4,t.$axios.post(t.data.urls,data).then((function(o){console.log(o),200==o.status?(t.data.msg="Успешно",document.cookie="token="+o.data.key,setTimeout((function(){window.location.href="/"}),1e3)):t.data.msg="Ошибка"}));case 4:o.next=9;break;case 6:o.prev=6,o.t0=o.catch(1),t.data.msg="Ошибка";case 9:case"end":return o.stop()}}),o,null,[[1,6]])})))()}}),n),d=(e(252),e(44)),component=Object(d.a)(c,(function(){var t=this,o=t.$createElement,e=t._self._c||o;return e("div",[e("div",{staticClass:"container"},[e("div",{staticClass:"row main-form"},[e("form",{attrs:{method:"post",action:"#"}},[e("div",{staticClass:"form-group"},[e("label",{staticClass:"cols-sm-2 control-label",attrs:{for:"email"}},[t._v("Your Email")]),t._v(" "),e("div",{staticClass:"cols-sm-10"},[e("div",{staticClass:"input-group"},[t._m(0),t._v(" "),e("input",{directives:[{name:"model",rawName:"v-model",value:t.email,expression:"email"}],staticClass:"form-control",attrs:{type:"text",name:"email",id:"email",placeholder:"Enter your Email"},domProps:{value:t.email},on:{input:function(o){o.target.composing||(t.email=o.target.value)}}})])])]),t._v(" "),e("div",{staticClass:"form-group"},[e("label",{staticClass:"cols-sm-2 control-label",attrs:{for:"password"}},[t._v("Password")]),t._v(" "),e("div",{staticClass:"cols-sm-10"},[e("div",{staticClass:"input-group"},[t._m(1),t._v(" "),e("input",{directives:[{name:"model",rawName:"v-model",value:t.password,expression:"password"}],staticClass:"form-control",attrs:{type:"password",name:"password",id:"password",placeholder:"Enter your Password"},domProps:{value:t.password},on:{input:function(o){o.target.composing||(t.password=o.target.value)}}})])])]),t._v(" "),e("div",{staticClass:"form-group "},[e("button",{staticClass:"btn btn-primary btn-lg btn-block login-button",attrs:{target:"_blank",type:"button",id:"button"},on:{click:t.loginUser}},[t._v("Войти")])])])])])])}),[function(){var t=this.$createElement,o=this._self._c||t;return o("span",{staticClass:"input-group-addon"},[o("i",{staticClass:"fa fa-envelope fa",attrs:{"aria-hidden":"true"}})])},function(){var t=this.$createElement,o=this._self._c||t;return o("span",{staticClass:"input-group-addon"},[o("i",{staticClass:"fa fa-lock fa-lg",attrs:{"aria-hidden":"true"}})])}],!1,null,null,null);o.default=component.exports}}]);