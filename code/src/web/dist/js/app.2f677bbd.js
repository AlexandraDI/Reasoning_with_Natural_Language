(function(e){function t(t){for(var a,o,i=t[0],l=t[1],c=t[2],d=0,u=[];d<i.length;d++)o=i[d],Object.prototype.hasOwnProperty.call(n,o)&&n[o]&&u.push(n[o][0]),n[o]=0;for(a in l)Object.prototype.hasOwnProperty.call(l,a)&&(e[a]=l[a]);p&&p(t);while(u.length)u.shift()();return r.push.apply(r,c||[]),s()}function s(){for(var e,t=0;t<r.length;t++){for(var s=r[t],a=!0,i=1;i<s.length;i++){var l=s[i];0!==n[l]&&(a=!1)}a&&(r.splice(t--,1),e=o(o.s=s[0]))}return e}var a={},n={app:0},r=[];function o(t){if(a[t])return a[t].exports;var s=a[t]={i:t,l:!1,exports:{}};return e[t].call(s.exports,s,s.exports,o),s.l=!0,s.exports}o.m=e,o.c=a,o.d=function(e,t,s){o.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:s})},o.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.t=function(e,t){if(1&t&&(e=o(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var s=Object.create(null);if(o.r(s),Object.defineProperty(s,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var a in e)o.d(s,a,function(t){return e[t]}.bind(null,a));return s},o.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return o.d(t,"a",t),t},o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},o.p="/";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],l=i.push.bind(i);i.push=t,i=i.slice();for(var c=0;c<i.length;c++)t(i[c]);var p=l;r.push([0,"chunk-vendors"]),s()})({0:function(e,t,s){e.exports=s("56d7")},"034f":function(e,t,s){"use strict";s("85ec")},"13bd":function(e,t,s){"use strict";s("ee68")},"56d7":function(e,t,s){"use strict";s.r(t);s("e260"),s("e6cf"),s("cca6"),s("a79d");var a=s("2b0e"),n=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{attrs:{id:"app"}},[s("main",[s("application-header"),s("ModeSwitcher",{on:{"switch-page":e.change_page}}),s("div",{staticClass:"tab-content",attrs:{id:"pills-tabContent"}},[s("div",{staticClass:"tab-pane",attrs:{id:"reasoner",role:"tabpanel","aria-labelledby":"reasoner-tab"}},[s("ReasonerPage",{on:{"display-tree":e.display_tree}})],1),s("div",{staticClass:"tab-pane",attrs:{id:"language",role:"tabpanel","aria-labelledby":"language-tab"}},[s("LanguageCheckerPage")],1)]),e.error?s("div",{staticClass:"card bg-danger mt-2"},[s("div",{staticClass:"card-header"},["ParseException"===e.error.type?s("span",{staticClass:"lead"},[e._v(" Parse Exception ")]):e._e(),"ParseException"!==e.error.type?s("span",{staticClass:"lead"},[e._v(" Internal Error ")]):e._e()]),s("div",{staticClass:"card-body"},["ParseException"!==e.error.type?s("div",[s("span",{staticClass:"lead"},[e._v("Oops something went wrong and we dont really know what.")]),s("br"),s("span",{staticClass:"lead"},[e._v("This could help tho: "+e._s(e.error.error))])]):e._e(),"ParseException"===e.error.type?s("div",[s("span",{staticClass:"lead"},[e._v("We detected a error in the parsing process")]),s("br"),s("span",{staticClass:"lead"},[e._v("This are the errors we collected along the way:")]),s("br"),s("ul",e._l(e.error.list,(function(t){return s("li",{key:t},[e._v(e._s(t))])})),0)]):e._e()])]):e._e(),s("div",{staticClass:"card",staticStyle:{position:"fixed"},style:{display:e.tooltip_visible?"block":"none",top:e.topOffset,left:e.leftOffset},attrs:{id:"tooltip"}},[s("div",{staticClass:"card-header"},[e._v(e._s(e.tooltip_header))]),s("div",{staticClass:"card-body"},[e.basic_in_expressions?s("table",{staticClass:"m-2"},[s("tr",{staticStyle:{"border-bottom":"2px solid black"}},[s("td",{staticStyle:{"text-align":"center"}},e._l(e.basic_in_expressions,(function(t,a){return s("span",{key:a},[e._v(" "+e._s(t)+" "),e.basic_in_expressions.length>1&&a!==e.basic_in_expressions.length-1?s("span",[e._v(",")]):e._e()])})),0)]),s("tr",[s("td",{staticStyle:{"text-align":"center"}},e._l(e.basic_out_expressions,(function(t,a){return s("span",{key:a},[e._l(t,(function(a,n){return s("span",{key:n},[e._v(" "+e._s(a)),t.length>1&&n!==t.length-1?s("span",[e._v(",")]):e._e()])})),e.basic_out_expressions.length>1&&a!==e.basic_out_expressions.length-1?s("span",[e._v("|")]):e._e()],2)})),0)])]):e._e(),e.basic_in_expressions?s("p",[e._v("This rule applied looks like this:")]):e._e(),e.in_expressions?s("table",{staticClass:"m-2"},[s("tr",{staticStyle:{"border-bottom":"2px solid black"}},[s("td",{staticStyle:{"text-align":"center"}},e._l(e.in_expressions,(function(t,a){return s("span",{key:a},[e._v(" "+e._s(t)+" "),e.in_expressions.length>1&&a!==e.in_expressions.length-1?s("span",[e._v(",")]):e._e()])})),0)]),s("tr",[s("td",{staticStyle:{"text-align":"center"}},e._l(e.out_expressions,(function(t,a){return s("span",{key:a},[e._l(t,(function(a,n){return s("span",{key:n},[e._v(" "+e._s(a)+" "),t.length>1&&n!==t.length-1?s("span",[e._v(",")]):e._e()])})),e.out_expressions.length>1&&a!==e.out_expressions.length-1?s("span",[e._v("|")]):e._e()],2)})),0)])]):e._e(),s("p",{staticClass:"m-2",domProps:{innerHTML:e._s(e.tooltip_description)}})])])],1),s("div",{staticClass:"graph",class:{border:e.graph_rendered},attrs:{id:"graph"}}),e.response||e.language_output?s("div",{staticStyle:{height:"calc(0.5 * 100vh)"}}):e._e()])},r=[],o=(s("a434"),s("ac1f"),s("5319"),s("5b81"),s("b0c0"),s("a4d3"),s("e01a"),s("8c4f")),i=s("1157"),l=(s("5b52"),s("0d50"),s("ab8b"),s("f507"),function(){var e=this,t=e.$createElement;e._self._c;return e._m(0)}),c=[function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("header",[s("h1",{staticClass:"heading"},[e._v("Natural Language Reasoner")])])}],p=(s("13bd"),s("2877")),d={},u=Object(p["a"])(d,l,c,!1,null,"77e48a31",null),_=u.exports,g=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("ul",{staticClass:"nav nav-pills nav-fill pb-3",attrs:{id:"tab",role:"tablist"}},[s("li",{staticClass:"nav-item",attrs:{role:"presentation"}},[s("button",{staticClass:"nav-link border",attrs:{id:"reasoner-tab",type:"button","data-bs-toggle":"tab","data-bs-target":"#reasoner",role:"tab","aria-controls":"reasoner","aria-selected":"false"},on:{click:function(t){return e.switchPage("reasoner")}}},[e._v(" Reasoner ")])]),s("li",{staticClass:"nav-item",attrs:{role:"presentation"}},[s("button",{staticClass:"nav-link border",attrs:{id:"language-tab",type:"button","data-bs-toggle":"tab","data-bs-target":"#language",role:"tab","aria-controls":"language","aria-selected":"false"},on:{click:function(t){return e.switchPage("language")}}},[e._v(" Language Check ")])])])},h=[],b={methods:{switchPage:function(e){this.$emit("switch-page",e)}}},f=b,v=Object(p["a"])(f,g,h,!1,null,null,null),m=v.exports,x=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",[s("ReasoningExamplesMenu",{on:{"on-select-example":e.set_reasoning_expression}}),s("ExpressionsForm",{attrs:{expressions:this.expressions,to_be_shown:this.to_be_shown},on:{submit:e.send_request,"change-expression":this.modify_expression,"add-expression":this.add_expression,"remove-expression":this.remove_expression}}),s("div",{style:{display:e.response&&null==e.error?"block":"none"}},[s("div",{staticClass:"card my-4",class:{"bg-success":e.tree_closes,"bg-danger":!e.tree_closes}},[e.tree_closes?s("h2",{staticClass:"display-5 text-center"},[e._v("The statement is valid")]):e._e(),e.tree_closes?e._e():s("h2",{staticClass:"display-5 text-center"},[e._v("There is a branch that doesn't close")])]),0!==e.applied_rules.length?s("div",{staticClass:"accordion mb-4",attrs:{id:"accordionAppliedRule"}},[s("div",{staticClass:"accordion-item"},[e._m(0),s("div",{staticClass:"accordion-collapse collapse",attrs:{id:"collapseAppliedRule","aria-labelledby":"heading-applied-rule","data-bs-parent":"#accordionAppliedRule"}},[s("div",{staticClass:"accordion-body"},[s("div",{staticClass:"accordion",attrs:{id:"accordion"}},e._l(e.applied_rules,(function(t,a){return s("div",{key:a,staticClass:"accordion-item"},["root_node"!==a?s("h1",{staticClass:"accordion-header",attrs:{id:"heading-applied-rule-"+a}},[s("button",{staticClass:"accordion-button collapsed",attrs:{type:"button","data-bs-toggle":"collapse","data-bs-target":"#collapseAppliedRule-"+a,"aria-expanded":"false","aria-controls":"collapseAppliedRule-"+a}},[s("span",{staticClass:"fs-5"},[e._v(" "+e._s(t.rule_name)+" ")])])]):e._e(),s("div",{staticClass:"accordion-collapse collapse",attrs:{id:"collapseAppliedRule-"+a,"data-bs-parent":"#accordion"}},[s("div",{staticClass:"accordion-body"},[s("table",{staticClass:"table"},[s("thead",[s("tr",[s("th",{attrs:{scope:"col"}},[e._v("Referenced Line")]),t.created_expressions?s("th",{attrs:{scope:"col"}},[e._v("Created Expressions ")]):e._e(),s("th",{attrs:{scope:"col"}},[e._v("Used Expression")]),"None"!==t.matched_expression?s("th",{attrs:{scope:"col"}},[e._v(" Matched Expression ")]):e._e()])]),s("tbody",[s("tr",[s("td",[e._v(e._s(t.referenced_line))]),t.created_expressions?s("td",[s("ul",e._l(t.created_expressions,(function(t,a){return s("li",{key:a},[e._v(" "+e._s(t)+" ")])})),0)]):e._e(),s("td",[e._v(e._s(t.c_expression))]),"None"!==t.matched_expression?s("td",[e._v(" "+e._s(t.matched_expression)+" ")]):e._e()])])])])])])})),0)])])])]):e._e(),e.response?s("p",[e._v("*You can hover over each node to receive a more detailed explanation of the applied rule.")]):e._e()])],1)},y=[function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("h1",{staticClass:"accordion-header",attrs:{id:"heading-applied-rule"}},[s("button",{staticClass:"accordion-button collapsed",attrs:{type:"button","data-bs-toggle":"collapse","data-bs-target":"#collapseAppliedRule","aria-expanded":"false","aria-controls":"collapseAppliedRule"}},[s("span",{staticClass:"fs-3"},[e._v(" Applied Rules ")])])])}],C=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("ul",{staticClass:"nav nav-tabs",attrs:{role:"tablist"}},e._l(e.data,(function(t){return s("li",{key:t.tab_name,staticClass:"nav-item",class:{dropdown:t.examples.length>1},attrs:{role:"presentation"}},[1===t.examples.length?s("a",{staticClass:"nav-link",class:{active:t.tab_name===e.current_tab},attrs:{href:"#","aria-current":"page"},on:{click:function(s){return e.selectExample(t,0)}}},[e._v(e._s(t.tab_name))]):e._e(),t.examples.length>1?s("a",{staticClass:"nav-link dropdown-toggle",class:{active:t.tab_name===e.current_tab},attrs:{"data-toggle":"dropdown","data-bs-toggle":"dropdown","data-bs-auto-close":"true",href:"#","aria-expanded":"false"}},[e._v(e._s(t.tab_name))]):e._e(),t.examples.length>1?s("ul",{staticClass:"dropdown dropdown-menu",attrs:{role:"menu",id:t.tab_name}},e._l(t.examples,(function(a,n){return s("li",{key:n},[s("a",{staticClass:"dropdown-item",attrs:{href:"#"},on:{click:function(s){return e.selectExample(t,n)}}},[e._v(e._s(a.name))])])})),0):e._e()])})),0)},w=[],k=s("bc3a"),E=s.n(k),O={name:"ReasoningExamplesMenu",mounted:function(){var e=this;E.a.get("/examples?name=reasoner_examples.json").then((function(t){e.data=t["data"],e.selectExample(e.data[0],0)}))},data:function(){return{data:{},current_tab:""}},methods:{selectExample:function(e,t){this.current_tab=e.tab_name;var s=e.examples[t],a=s["to_be_shown"],n=s["expressions"];this.$emit("on-select-example",n,a);var r=document.getElementById(e.tab_name);r&&r.classList.remove("show")}}},P=O,S=Object(p["a"])(P,C,w,!1,null,"83517c8a",null),j=S.exports,A=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("fieldset",{staticClass:"list-group p-4 border-end border-bottom border-start tab-content",attrs:{name:"form"}},[e._l(e.expressions,(function(t,a){return s("div",{key:a,staticClass:"expression_input pb-1"},[s("label",{staticClass:"form-label"},[e._v(e._s(a+1)+". input:")]),s("input",{staticClass:"form-control",attrs:{type:"text",placeholder:"Next Expression"},domProps:{value:t.value},on:{input:function(t){return e.propagate_modification(t,a)}}}),s("button",{staticClass:"btn btn-danger",class:{disabled:1===e.expressions.length},attrs:{type:"button"},on:{click:function(t){return e.remove_field(t,a)}}},[e._v("- ")]),a===e.expressions.length-1?s("button",{staticClass:"btn btn-success",attrs:{type:"button"},on:{click:e.add_field}},[e._v("+ ")]):e._e(),s("br")])})),s("div",{staticClass:"expression_input"},[s("label",[e._v("To be shown:")]),s("input",{staticClass:"form-control",attrs:{type:"text"},domProps:{value:e.to_be_shown},on:{input:function(t){return e.propagate_modification(t,-1)}}}),s("br")]),s("button",{staticClass:"btn btn-primary",staticStyle:{"margin-top":"8px"},attrs:{type:"button"},on:{click:e.submit}},[e._v("Solve ")])],2)},R=[],$={name:"ExpressionsForm",props:{expressions:Array,to_be_shown:String},methods:{submit:function(){this.$emit("submit")},add_field:function(){this.$emit("add-expression")},remove_field:function(e,t){this.$emit("remove-expression",t)},propagate_modification:function(e,t){this.$emit("change-expression",t,e.target.value)}}},L=$,T=(s("d442"),Object(p["a"])(L,A,R,!1,null,"679487b0",null)),M=T.exports,N={name:"ReasonerPage",components:{ReasoningExamplesMenu:j,ExpressionsForm:M},data:function(){return{expressions:[""],to_be_shown:"",response:null,error:null,tree_closes:!0,applied_rules:[]}},methods:{set_reasoning_expression:function(e,t){console.log("set_example_reasoning_expression",e,t),this.expressions=e,this.to_be_shown=t},modify_expression:function(e,t){e<0?this.to_be_shown=t:this.expressions[e]["value"]=t},add_expression:function(){this.expressions.push({value:""})},remove_expression:function(e){this.expressions.splice(e,1)},send_request:function(){var e=this;console.log("send_request"),this.error=null;var t={expressions:this.expressions,to_be_shown:this.to_be_shown};E.a.post("/solve-request",t).catch((function(t){e.error=JSON.parse(t.response.data.replaceAll('"',"`").replaceAll("'",'"'))})).then((function(t){var s=t.data;for(var a in e.response=s,e.applied_rules=s["applied_rules"],e.tree_closes=JSON.parse(s["all_branches_closed"]),e.applied_rules){var n=e.applied_rules[a];n.created_expressions&&(console.log(n.created_expressions.replaceAll("'",'"')),n.created_expressions=JSON.parse(n.created_expressions.replaceAll('"',"`").replaceAll("'",'"')))}e.$emit("display-tree",s["dot_graph"])}))}}},q=N,J=Object(p["a"])(q,x,y,!1,null,"859239b2",null),I=J.exports,B=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",[s("h3",[e._v("Language Check")]),s("p",[e._v(" Here you can check out what our constrained natural language is able to parse. You can either write your own sentences or checkout the examples that we provided. ")]),s("div",{staticClass:"accordion mb-4",attrs:{id:"accordionFlushExample"}},[s("div",{staticClass:"accordion-item"},[e._m(0),s("div",{staticClass:"accordion-collapse collapse",attrs:{id:"flush-collapseOne","aria-labelledby":"flush-headingOne","data-bs-parent":"#accordionFlushExample"}},[s("div",{staticClass:"accordion-body"},[s("div",{staticClass:"accordion mb-4",attrs:{id:"language_examples_accordion"}},e._l(e.language_examples,(function(t,a){return s("div",{key:a,staticClass:"accordion-item"},[s("h3",{staticClass:"accordion-header",attrs:{id:"group_heading_"+a}},[s("button",{staticClass:"accordion-button collapsed",attrs:{type:"button","data-bs-toggle":"collapse","data-bs-target":"#group_collapse_"+a,"aria-expanded":"true","aria-controls":"group_collapse_"+a}},[e._v(" "+e._s(t["group_name"])+" ")])]),s("div",{staticClass:"accordion-collapse collapse",attrs:{id:"group_collapse_"+a,"aria-labelledby":"group_heading_"+a,"data-bs-parent":"#language_examples_accordion"}},[s("div",{staticClass:"accordion-body"},[s("div",{staticClass:"d-flex flex-row justify-content-between flex-wrap"},e._l(t["examples"],(function(t){return s("button",{key:t,staticClass:"btn m-1 text-nowrap flex-grow-1",class:{"btn-outline-success":e.sentence!==t,"btn-success":e.sentence===t},attrs:{type:"button"},on:{click:function(s){return e.select_language_example(t)}}},[e._v(" "+e._s(t)+" ")])})),0)])])])})),0)])])])]),s("fieldset",{staticClass:"list-group border p-4",attrs:{name:"form"}},[s("div",{staticClass:"pb-3"},[s("label",{staticClass:"w-100"},[s("span",{staticClass:"form-label"},[e._v("Test sentence:")]),s("input",{staticClass:"form-control",attrs:{type:"text",placeholder:"Next Expression"},domProps:{value:e.sentence}})])]),s("button",{staticClass:"btn btn-primary",class:{disabled:!e.sentence},attrs:{type:"button"},on:{click:e.language_request}},[e._v(" Check ")])]),s("div",{staticClass:"container-fluid p-4"},[e.error?e._e():s("div",{staticStyle:{position:"absolute",left:"50%",transform:"translateX(-50%)"},domProps:{innerHTML:e._s(e.create_sentence_presentation)}})])])},F=[function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("h1",{staticClass:"accordion-header",attrs:{id:"flush-headingOne"}},[s("button",{staticClass:"accordion-button collapsed",attrs:{type:"button","data-bs-toggle":"collapse","data-bs-target":"#flush-collapseOne","aria-expanded":"false","aria-controls":"flush-collapseOne"}},[s("span",{staticClass:"fs-3"},[e._v(" Examples ")])])])}],W={name:"LanguageCheckerPage",data:function(){return{response:null,error:null,language_examples:[],sentence:"When i love you then you love me",language_output:null}},mounted:function(){var e=this;E.a.get("/examples?name=language_examples.json").then((function(t){e.language_examples=t["data"],e.sentence=e.language_examples[0]["examples"][0]}))},methods:{select_language_example:function(e){this.sentence=e,this.language_request()},language_request:function(){var e=this;this.error=null,console.log(this.sentence);var t={sentence:this.sentence};E.a.post("/language-request",t).catch((function(t){e.error=JSON.parse(t.bodyText.replaceAll('"',"`").replaceAll("'",'"'))})).then((function(t){console.log(t),e.language_output=t.data}))},recursive_sentence_structure:function(e){var t=e["type"],s='<div class="p-1 m-1 rounded align-middle d-flex flex-column align-content-center justify-content-center" style="background-color: '+this.get_color(t)+"; border: 3px solid "+this.get_border_color(t)+'">\n';s+="<h4 class='flex-row' style='margin: 0.25em 0.25em 0 0.25em'>"+e["name"]+"</h4>",s+="<div class='d-flex flex-row d-inline-flex align-content-center justify-content-center'>",e["tokens"]&&(s+='<span class="text-center text-nowrap"><strong>'+e["tokens"]+"</strong></span>");for(var a=0;a<e["list"].length;a++){var n=e["list"][a];if(n["list"]&&n["list"].length>=1)s+=this.recursive_sentence_structure(n);else{var r=n["type"];s+='<div class="p-1 m-1 rounded align-middle" style="background-color: '+this.get_color(r)+"; display: flex; justify-content: center; flex-direction: column; border: 2px solid "+this.get_border_color(r)+'">\n',0===r?s+='<span class="text-center"><strong>¬</strong></span>':(n["name"]&&(s+='<span class="text-center text-nowrap">'+n["name"]+"</span>"),n["tokens"]&&(s+='<span class="text-center text-nowrap"><strong>'+n["tokens"]+"</strong></span>")),s+="</div>"}}return s+="</div></div>\n",s},get_color:function(e){var t="#a5363b";return-1===e?t="#fd8f55":1===e?t="#c66432":2===e?t="#4f7e5f":-2===e?t="#6dc88a":3===e?t="#586983":-3===e?t="#8aa1cb":4===e?t="#b161b1":-4===e?t="#ffb8ff":5===e?t="#b39986":-5===e?t="#fdb78a":6===e?t="#1281d6":-6===e&&(t="#68a8ec"),t},get_border_color:function(e){var t="#8a1f25";return 1===e?t="#ca5e26":-1===e?t="#602007":2===e?t="#285f42":-2===e?t="#2f854a":3===e?t="#354d77":-3===e?t="#40567e":4===e?t="#452245":-4===e?t="#8f488f":5===e?t="#836550":-5===e?t="#9d6640":6===e?t="#064673":-6===e&&(t="#284877"),t}},computed:{create_sentence_presentation:function(){return null==this.language_output?"<div></div>":this.recursive_sentence_structure(this.language_output)}}},H=W,Y=Object(p["a"])(H,B,F,!1,null,"4b03d5aa",null),z=Y.exports;a["a"].use(o["a"]);var X=new o["a"]({}),D={name:"App",components:{LanguageCheckerPage:z,ReasonerPage:I,ApplicationHeader:_,ModeSwitcher:m},data:function(){return{expressions:[],to_be_shown:null,error:null,response:null,up:!0,current_tab:"Normal Examples",tabs:[],language_examples:[],sentence:"When i love you then you love me",auto_send:!0,language_output:null,tooltip_header:"",in_expressions:"",out_expressions:"",basic_in_expressions:"",basic_out_expressions:"",tooltip_description:"",tooltip_visible:!1,topOffset:"0px",leftOffset:"0px",graph_rendered:!1}},mounted:function(){var e=this;"#/language"===window.location.hash?this.change_page("language"):this.change_page("reasoner"),window.onmousemove=function(t){if(e.tooltip_visible){var s=t.clientX,a=t.clientY;e.topOffset=a+20+"px",e.leftOffset=s+20+"px"}}},methods:{change_page:function(e){var t=document.getElementById("reasoner"),s=document.getElementById("language"),a=document.getElementById("reasoner-tab"),n=document.getElementById("language-tab");"reasoner"===e?(a.classList.add("active"),t.classList.add("active"),i("#graph").show(),X.push("reasoner")):(n.classList.add("active"),s.classList.add("active"),i("#graph").hide(),X.push("language"))},remove_field:function(e){this.expressions.splice(e,1)},add_field:function(){this.expressions.push({value:""})},toggle_tooltip:function(e,t){var s=this.applied_rules[e[0].id]["rule_desc_obj"],a=JSON.parse(s.replaceAll('"',"`").replaceAll("'",'"'));this.tooltip_header=a["name"],this.in_expressions=a["in_expression"],this.out_expressions=a["out_expression"],this.basic_in_expressions=a["basic_in_expression"],this.basic_out_expressions=a["basic_out_expression"],this.tooltip_description=a["description"],this.tooltip_visible=t},display_tree:function(e){var t=this;this.graph_rendered&&d3.select("#graph").graphviz({useWorker:!1}).resetZoom(),d3.select("#graph").graphviz({useWorker:!1}).on("renderEnd",(function(){t.graph_rendered=!0;for(var e=d3.selectAll(".node"),s=0;s<e._groups[0].length;s++){var a=e._groups[0][s],n=i(a).children();i(i(n[1]).children()[0]).children("polygon")[0].setAttribute("fill","#ffffff"),n[1].onpointerenter=function(e){t.toggle_tooltip(i(e.target).parent(),!0)},n[1].onpointerleave=function(e){t.toggle_tooltip(i(e.target).parent(),!1)}}})).renderDot(e)}}},U=D,Z=(s("034f"),Object(p["a"])(U,n,r,!1,null,null,null)),G=Z.exports;a["a"].config.productionTip=!1,new a["a"]({render:function(e){return e(G)}}).$mount("#app")},"85ec":function(e,t,s){},"9b03":function(e,t,s){},d442:function(e,t,s){"use strict";s("9b03")},ee68:function(e,t,s){}});
//# sourceMappingURL=app.2f677bbd.js.map