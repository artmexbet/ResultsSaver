(this.webpackJsonpforiti=this.webpackJsonpforiti||[]).push([[0],{196:function(e,t,n){},388:function(e,t,n){},389:function(e,t,n){},396:function(e,t,n){},527:function(e,t,n){"use strict";n.r(t);var c,a,s,r,i,o,l=n(0),u=n(17),j=n.n(u),d=(n(388),n(389),n(101)),b=n(102),h=n(20),O=n(352),f=b.a.nav(c||(c=Object(d.a)(["\n  background: #000;\n  height: 80px;\n  display: flex;\n  background-color: #000;\n  justify-content: space-between;\n  padding: 0.5rem calc((100vw - 1000px) / 2);\n  z-index: 10;\n  /* Third Nav */\n  /* justify-content: flex-start; */\n"]))),x=Object(b.a)(h.c)(a||(a=Object(d.a)(["\n  color: #fff;\n  display: flex;\n  align-items: center;\n  text-decoration: none;\n  padding: 0 1rem;\n  height: 100%;\n  max-height: 100px;\n  cursor: pointer;\n  &.active {\n    color: #15cdfc;\n  }\n  :hover {\n    -moz-transition: background-color 0.2s 0.1s ease;\n-o-transition: background-color 0.2s 0.1s ease;\n-webkit-transition: background-color 0.2s 0.1s ease;\n-moz-transition: box-shadow 50ms 0.1s ease;\n-o-transition: box-shadow 50ms 0.1s ease;\n-webkit-transition: box-shadow 50ms 0.1s ease;\n    background: #03e9f4;\n    color: #fff;\n    border-radius: 5px;\n    box-shadow: 0 0 5px #03e9f4,\n                0 0 25px #03e9f4,\n                0 0 50px #03e9f4,\n                0 0 100px #03e9f4;\n  }\n  \n"]))),p=Object(b.a)(O.a)(s||(s=Object(d.a)(["\n  display: none;\n  color: #fff;\n \n  }\n"]))),g=b.a.div(r||(r=Object(d.a)(["\n  display: flex;\n  align-items: center;\n  margin-right: -24px;\n  /* Second Nav */\n  /* margin-right: 24px; */\n  /* Third Nav */\n  /* width: 100vw;\n  white-space: nowrap; */\n  \n"]))),m=b.a.nav(i||(i=Object(d.a)(["\n  display: flex;\n  align-items: center;\n  margin-right: 24px;\n  /* Third Nav */\n  /* justify-content: flex-end;\n  width: 100vw; */\n  @media screen and (max-width: 768px) {\n    display: none;\n  }\n"]))),v=Object(b.a)(h.c)(o||(o=Object(d.a)(["\n  border-radius: 4px;\n  background: #15cdfc;\n  padding: 10px 22px;\n  color: #000;\n  outline: none;\n  border: none;\n  cursor: pointer;\n  transition: all 0.2s ease-in-out;\n  text-decoration: none;\n  /* Second Nav */\n  margin-left: 24px;\n  &:hover {\n    transition: all 0.2s ease-in-out;\n    background: #fff;\n    color: #010606;\n  }\n"]))),y=n(3),w=function(){return Object(y.jsx)(y.Fragment,{children:Object(y.jsxs)(f,{children:[Object(y.jsx)(x,{to:"/",children:Object(y.jsx)("h1",{children:"\u0418\u0422\u0418"})}),Object(y.jsx)(p,{}),Object(y.jsxs)(g,{children:[Object(y.jsx)(x,{to:"/top",activeStyle:!0,children:"\u041b\u0443\u0447\u0448\u0438\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b"}),Object(y.jsx)(x,{to:"/first",activeStyle:!0,children:"\u041f\u0435\u0440\u0432\u044b\u0439 \u0434\u0435\u043d\u044c"}),Object(y.jsx)(x,{to:"/second",activeStyle:!0,children:"\u0412\u0442\u043e\u0440\u043e\u0439 \u0434\u0435\u043d\u044c"})]}),Object(y.jsx)(m,{children:Object(y.jsx)(v,{to:"/log",children:"\u0412\u043e\u0439\u0442\u0438"})})]})})},S=n(19),E=n(22),C=n.n(E),I=n(38),P=n(27),k=n(236),_=n(589),N=n(593),T=n(592),B=n(588),L=n(590),R=n(591),H=n(529),J=n(85),A=n.n(J),F=(n(196),Object(k.a)({table:{minWidth:650}}));function M(){var e=new XMLHttpRequest;e.open("PUT","http://localhost:5000/change_day",!0),e.setRequestHeader("Content-Type","application/json");try{var t=JSON.stringify({new_day:0});e.send(t)}catch(Q){console.log(Q)}var n=F(),c=Object(l.useState)(),a=Object(P.a)(c,2),s=a[0],r=a[1],i=Object(l.useState)(!0),o=Object(P.a)(i,2),u=o[0],j=o[1],d=function(){var e=Object(I.a)(C.a.mark((function e(){return C.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.abrupt("return",fetch("http://localhost:5000/users/1").then((function(e){return e.json()})).then((function(e){r(e),j(!1)})));case 1:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}();Object(l.useEffect)((function(){return d(s),0}),[]);var b=Object(l.useState)(""),h=Object(P.a)(b,2),O=h[0],f=h[1],x=Object(l.useState)("5"),p=Object(P.a)(x,2),g=p[0],m=p[1],v=Object(l.useState)("6"),w=Object(P.a)(v,2),S=w[0],E=w[1],k=Object(l.useState)("7"),J=Object(P.a)(k,2),M=J[0],q=J[1],D=Object(l.useState)("8"),U=Object(P.a)(D,2),W=U[0],z=U[1],K=Object(l.useState)("9"),X=Object(P.a)(K,2),V=X[0],G=X[1];return Object(y.jsx)(y.Fragment,{children:u?Object(y.jsx)(A.a,{className:"loaderApplication",type:"bubbles",color:"#",height:100,width:100}):Object(y.jsxs)(y.Fragment,{children:[Object(y.jsx)("input",{id:"find",type:"text",placeholder:"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u0434",onChange:function(e){return f(e.target.value)}}),Object(y.jsx)("input",{id:"classfive",type:"checkbox",defaultChecked:!0,value:"5",onChange:function(e){console.log(document.getElementById("classfive")),!0===document.getElementById("classfive").checked?(console.log(document.getElementById("classfive")),m(document.getElementById("classfive").value)):m(" ")}}),"5 \u041a\u043b\u0430\u0441\u0441",Object(y.jsx)("input",{id:"classsix",type:"checkbox",defaultChecked:!0,value:"6",onChange:function(){console.log(document.getElementById("classsix")),!0===document.getElementById("classsix").checked?E(document.getElementById("classsix").value):(console.log(document.getElementById("classsix")),E(" "))}}),"6 \u041a\u043b\u0430\u0441\u0441",Object(y.jsx)("input",{id:"classseven",type:"checkbox",defaultChecked:!0,value:"7",onChange:function(){!0===document.getElementById("classseven").checked?q(document.getElementById("classseven").value):q(" ")}}),"7 \u041a\u043b\u0430\u0441\u0441",Object(y.jsx)("input",{id:"classseight",type:"checkbox",defaultChecked:!0,value:"8",onChange:function(){!0===document.getElementById("classseight").checked?z(document.getElementById("classseight").value):z(" ")}}),"8 \u041a\u043b\u0430\u0441\u0441",Object(y.jsx)("input",{id:"classnine",type:"checkbox",defaultChecked:!0,value:"9",onChange:function(){!0===document.getElementById("classnine").checked?G(document.getElementById("classnine").value):G(" ")}}),"9 \u041a\u043b\u0430\u0441\u0441",console.log(g,S),Object(y.jsx)(B.a,{styles:H.a,className:"page",children:Object(y.jsxs)(_.a,{className:n.table,size:"small","aria-label":"a dense table",children:[Object(y.jsx)(L.a,{children:Object(y.jsxs)(R.a,{children:[Object(y.jsx)(T.a,{children:"\u2116"}),Object(y.jsx)(T.a,{align:"left",children:"\u0418\u043c\u044f"}),Object(y.jsx)(T.a,{align:"left",children:"\u041a\u043b\u0430\u0441\u0441"}),Object(y.jsx)(T.a,{align:"left",children:"\u0411\u0443\u043a\u0432\u0430"}),Object(y.jsx)(T.a,{align:"left",children:"\u0411\u0430\u043b\u043b\u044b"})]})}),Object(y.jsx)(N.a,{children:s.users.filter((function(e){if(""===O){if(""===g&&""===S&&""===M&&""===W&&""===V)return e;if(e.class.toString().toLowerCase().includes(g.toLowerCase())||e.class.toString().toLowerCase().includes(S.toLowerCase())||e.class.toString().toLowerCase().includes(M.toLowerCase())||e.class.toString().toLowerCase().includes(W.toLowerCase())||e.class.toString().toLowerCase().includes(V.toLowerCase()))return e}else if(e.id.toString().toLowerCase().includes(O.toLowerCase()))return e})).map((function(e){return Object(y.jsxs)(R.a,{children:[Object(y.jsx)(T.a,{component:"th",scope:"row",children:e.id}),Object(y.jsx)(T.a,{align:"left",children:e.name}),Object(y.jsx)(T.a,{align:"left",children:e.class}),Object(y.jsx)(T.a,{align:"left",children:e.class_letter}),Object(y.jsx)(T.a,{align:"left",children:Object(y.jsx)("a",{href:"http://localhost:3000/userinfo/".concat(e.id),children:"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435"})})]},e.id)}))})]})})]})})}Object(k.a)({table:{minWidth:650}});n(396);var q=n(310),D=n(311),U=new(function(){function e(){Object(q.a)(this,e),this.authenticated=!1}return Object(D.a)(e,[{key:"login",value:function(e){this.authenticated=!0,e()}},{key:"logout",value:function(e){this.authenticated=!1,e()}},{key:"isAuthenticated",value:function(){return this.authenticated}}]),e}()),W=(n(397),{login:function(e,t){var n=new Request("http://localhost:5000/check_admins",{method:"POST",body:JSON.stringify({login:e,password:t}),headers:new Headers({"Content-Type":"application/json"})});return fetch(n).then((function(e){if(e.status<200||e.status>=300)throw new Error(e.statusText);return e.json().then((function(e){return localStorage.setItem("auth",JSON.stringify(e.data)),e.data.access})).catch((function(e){return Promise.reject()}))}))},checkError:function(e){var t=e.status;return 401===t||403===t?(localStorage.removeItem("auth"),Promise.reject({redirectTo:"/log"})):Promise.resolve()},checkAuth:function(){return localStorage.getItem("auth")?Promise.resolve():Promise.reject()},logout:function(){return localStorage.removeItem("auth"),Promise.resolve()},getIdentity:function(){try{var e=JSON.parse(localStorage.getItem("auth")),t=e.id,n=e.subject,c=e.role;return Promise.resolve({id:t,subject:n,role:c})}catch(a){return Promise.reject(a)}},getPermissions:function(){var e=localStorage.getItem("permissions");return e?Promise.resolve(e):Promise.reject()}}),z=function(e){var t=Object(S.g)(),n=JSON.parse(localStorage.getItem("auth"));return null!==n&&1===n.access&&U.login((function(){t.push("/admin")})),Object(y.jsxs)("div",{className:"login-box",children:[Object(y.jsx)("h2",{children:"\u0412\u0445\u043e\u0434"}),Object(y.jsxs)("form",{children:[Object(y.jsxs)("div",{className:"user-box",children:[Object(y.jsx)("input",{type:"text",name:!0,required:!0,id:"log"}),Object(y.jsx)("label",{children:"\u041b\u043e\u0433\u0438\u043d"})]}),Object(y.jsxs)("div",{className:"user-box",children:[Object(y.jsx)("input",{type:"password",name:!0,required:!0,id:"pass"}),Object(y.jsx)("label",{children:"\u041f\u0430\u0440\u043e\u043b\u044c"})]}),Object(y.jsxs)("a",{href:"#",onClick:function(){Object(I.a)(C.a.mark((function e(){var n,c,a;return C.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return n=document.getElementById("log").value,c=document.getElementById("pass").value,e.next=4,W.login(n,c);case 4:a=e.sent,0!==a&&"undefiend"!==t&&U.login((function(){t.push("/admin")}));case 7:case"end":return e.stop()}}),e)})))()},children:[Object(y.jsx)("span",{}),Object(y.jsx)("span",{}),Object(y.jsx)("span",{}),Object(y.jsx)("span",{}),"\u0412\u043e\u0439\u0442\u0438"]})]})]})},K=n(16),X=n(95),V=n(612),G=n(611),Q=n(90),Y=(n(91),n(154)),Z=n(613),$=n(614),ee=n(627),te=n(608),ne=n(623),ce=n(166),ae="http://localhost:5000",se=X.a.fetchJson,re=(Object(K.a)(Object(K.a)({},Q.a),{},{getList:function(e,t){var n=t.pagination,c=n.page,a=n.perPage,s=t.sort,r=s.field,i=s.order,o={sort:JSON.stringify([r,i]),range:JSON.stringify([(c-1)*a,c*a-1]),filter:JSON.stringify(t.filter)};return(0,X.a.fetchJson)("http://localhost:5000/".concat(e,"/").concat(Object(ce.stringify)(o))).then((function(e){e.headers;return{data:e.json.users.map((function(e){return Object(K.a)({id:e.id},e)})),total:parseInt(10,20)}}))},getOne:function(e,t){return se("".concat(ae,"/users")).then().catch((function(e){return console.log(e),Promise.reject()}))},getMany:function(e,t){return Promise.reject()},getManyReference:function(e,t){return Promise.resolve()},create:function(e,t){return Promise.resolve()},update:function(e,t){if("posts"!==e||!t.data.pictures)return Q.a.update(e,t)},updateMany:function(e,t){return Promise.resolve()},delete:function(e,t){return se("".concat(ae,"/delete_user")).then().catch((function(e){return console.log(e),Promise.reject()}))},deleteMany:function(e,t){return Promise.resolve()}}),n(629),n(534)),ie=n(630),oe=n(620);Object(k.a)((function(e){return{chip:{marginBottom:e.spacing(1)}}}));Object(Q.a)("http://localhost:5000/delete_user");var le=new XMLHttpRequest,ue=function(e){le.open("DELETE","http://localhost:5000/delete_user",!0),le.setRequestHeader("Content-Type","application/json"),le.onreadystatechange=function(){};try{var t=document.querySelector("#Uid").textContent,n=JSON.stringify({id:parseInt(t)});le.send(n)}catch(c){console.log(c)}},je=function(e){var t=Object(l.useState)({users:[]}),n=Object(P.a)(t,2),c=n[0],a=n[1],s=function(){var e=Object(I.a)(C.a.mark((function e(){return C.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.abrupt("return",fetch("http://localhost:5000/sum").then((function(e){return e.json()})).then((function(e){a(e)})));case 1:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}();return Object(l.useEffect)((function(){return s(c),0}),[]),console.log(c),Object(y.jsxs)(y.Fragment,{children:[Object(y.jsx)(oe.a,{id:"searchadmin",options:c.users,getOptionLabel:function(e){return e.id.toString()},style:{width:300},renderInput:function(e){return Object(y.jsx)(ie.a,Object(K.a)(Object(K.a)({},e),{},{label:"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u043c\u0435\u0440",variant:"outlined"}))}}),Object(y.jsx)(re.a,{onClick:function(){return window.location.replace("http://localhost:3000/admin#/users/".concat(document.getElementById("searchadmin").value))},style:{display:"flex",width:"35%","background-color":"#237BFF",color:"#fff"},children:"\u041d\u0430\u0439\u0442\u0438"})]})},de=function(e){return Object(Y.a)("sum",{page:1,perPage:10},{field:"id",order:"DESC"}),Object(y.jsxs)(y.Fragment,{children:[Object(y.jsx)(je,{}),Object(y.jsx)(Z.a,Object(K.a)(Object(K.a)({title:"\u0421\u043f\u0438\u0441\u043e\u043a \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u043e\u0432",exporter:!1,bulkActionButtons:!1,sort:{field:"id",order:"DESC"}},e),{},{children:Object(y.jsxs)($.a,{children:[Object(y.jsx)(ee.a,{label:"\u041d\u043e\u043c\u0435\u0440",id:"Uid",source:"id"}),Object(y.jsx)(ee.a,{label:"\u0418\u043c\u044f",source:"name"}),Object(y.jsx)(ee.a,{label:"\u041a\u043b\u0430\u0441\u0441",source:"class"}),Object(y.jsx)(ee.a,{label:"\u0411\u0443\u043a\u0432\u0430",source:"class_letter"}),Object(y.jsx)(te.a,{label:"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c",basePath:"/users"}),Object(y.jsx)(ne.a,{label:"\u0423\u0434\u0430\u043b\u0438\u0442\u044c",basePath:"/users",onClick:ue})]})}))]})},be=n(118),he=n(619),Oe=n(615),fe=n(610),xe=new XMLHttpRequest,pe=function(e){xe.open("POST","http://localhost:5000/add_user",!0),xe.setRequestHeader("Content-Type","application/json"),xe.onreadystatechange=function(){};try{var t=document.getElementById("name").value,n=document.getElementById("class").value,c=document.getElementById("class_letter").value,a=JSON.stringify({name:t,class:n,class_letter:c,days:[]});xe.send(a)}catch(s){console.log(s)}},ge=function(e){return Object(y.jsx)(be.a,{children:Object(y.jsx)(he.a,Object(K.a)(Object(K.a)({},e),{},{title:"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u0430",children:Object(y.jsxs)(Oe.a,{redirect:"/admin",save:pe,children:[Object(y.jsx)(fe.a,{id:"name",label:"\u0418\u043c\u044f",source:"uname"}),Object(y.jsx)(fe.a,{id:"class",label:"\u041a\u043b\u0430\u0441\u0441",source:"class"}),Object(y.jsx)(fe.a,{id:"class_letter",label:"\u0411\u0443\u043a\u0432\u0430",source:"class_letter"}),Object(y.jsx)(fe.a,{id:"class_letter",label:"\u041a\u043e\u043c\u0430\u043d\u0434\u0430",source:"class_letter"})]})}))})},me=n(616),ve=new XMLHttpRequest,ye=function(e){var t=document.getElementById("id").value;ve.open("PATCH","http://localhost:5000/users/".concat(t),!0),ve.setRequestHeader("Content-Type","application/json"),ve.onreadystatechange=function(){};try{var n=document.getElementById("name").value,c=document.getElementById("class").value,a=document.getElementById("class_letter").value,s=JSON.stringify({name:n,class:c,class_letter:a,days:[]});ve.send(s)}catch(r){console.log(r)}return Promise.resolve({})},we=function(e){return Object(y.jsx)(me.a,Object(K.a)(Object(K.a)({title:"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c"},e),{},{children:Object(y.jsxs)(Oe.a,{save:ye,children:[Object(y.jsx)(fe.a,{disabled:!0,source:"id",id:"id"}),Object(y.jsx)(fe.a,{label:"\u0418\u043c\u044f",source:"name"}),Object(y.jsx)(fe.a,{label:"\u041a\u043b\u0430\u0441\u0441",source:"class"}),Object(y.jsx)(fe.a,{label:"\u0411\u0443\u043a\u0432\u0430",source:"class_letter"})]})}))},Se=n(115),Ee=n(632),Ce=n(624),Ie=n(617),Pe=n(625),ke=function(e){return Object(y.jsxs)(Se.a,{children:[Object(y.jsx)(Ee.a,{basePath:"/\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b"}),Object(y.jsx)(re.a,{onClick:Object(I.a)(C.a.mark((function e(){return C.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.abrupt("return",fetch("http://localhost:5000/recount",{method:"GET"}));case 1:case"end":return e.stop()}}),e)}))),children:"\u041f\u0435\u0440\u0435\u0441\u0447\u0451\u0442 \u0431\u0430\u043b\u043b\u043e\u0432"})]})},_e=function(e){return Object(y.jsxs)(Ce.a,Object(K.a)(Object(K.a)({},e),{},{children:[Object(y.jsx)(fe.a,{label:"Search",source:"id",alwaysOn:!0}),Object(y.jsx)(Ie.a,{label:"User",source:"name",reference:"users",allowEmpty:!0,children:Object(y.jsx)(Pe.a,{optionText:"name"})})]}))},Ne=function(e){return Object(y.jsx)(Z.a,Object(K.a)(Object(K.a)({filters:Object(y.jsx)(_e,{}),title:"\u0421\u043f\u0438\u0441\u043e\u043a \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u043e\u0432",bulkActionButtons:!1,exporter:!1,actions:Object(y.jsx)(ke,{})},e),{},{children:Object(y.jsxs)($.a,{children:[Object(y.jsx)(ee.a,{label:"\u041d\u043e\u043c\u0435\u0440",id:"Uid",source:"id"}),Object(y.jsx)(ee.a,{label:"\u0418\u043c\u044f",source:"name"}),Object(y.jsx)(ee.a,{label:"\u041a\u043b\u0430\u0441\u0441",source:"class"})]})}))},Te=new XMLHttpRequest,Be=function(e){var t=document.getElementById("id").value,n="http://localhost:5000/add_result/".concat(t);Te.open("POST",n,!0),Te.setRequestHeader("Content-Type","application/json"),Te.onreadystatechange=function(){};try{var c=document.getElementById("scores").value,a=document.getElementById("subject").value,s=JSON.stringify({subject:a,score:parseInt(c)});Te.send(s)}catch(r){console.log(r)}},Le=function(e){var t=JSON.parse(localStorage.getItem("auth")).speciality;return Object(y.jsx)(be.a,{children:Object(y.jsx)(he.a,Object(K.a)(Object(K.a)({},e),{},{title:"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u0430",children:Object(y.jsxs)(Oe.a,{redirect:"/admin",save:Be,children:[Object(y.jsx)(fe.a,{id:"id",source:"id",label:"\u041d\u043e\u043c\u0435\u0440"}),Object(y.jsx)(ie.a,{id:"subject",label:"\u041f\u0440\u0435\u0434\u043c\u0435\u0442",defaultValue:t,InputProps:{readOnly:!0}}),Object(y.jsx)(fe.a,{id:"scores",source:"score",label:"\u0411\u0430\u043b\u043b\u044b"})]})}))})},Re=n(621),He=n(628),Je=new XMLHttpRequest,Ae=function(e){var t=Object(l.useState)(""),n=Object(P.a)(t,2),c=n[0],a=n[1],s=Object(l.useState)({data:[]}),r=Object(P.a)(s,2),i=r[0],o=r[1],u=function(){var e=Object(I.a)(C.a.mark((function e(){return C.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,fetch("http://localhost:5000/subjects").then((function(e){return e.json()})).then((function(e){o(e)}));case 2:return e.abrupt("return",e.sent);case 3:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}();Object(l.useEffect)((function(){u(i)}),[]);return Object(y.jsx)(be.a,{children:Object(y.jsx)(he.a,Object(K.a)(Object(K.a)({},e),{},{title:"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0410\u0434\u043c\u0438\u043d\u0430",children:Object(y.jsxs)(Oe.a,{redirect:"/admin",save:function(e){Je.open("POST","http://localhost:5000/add_admin",!0),Je.setRequestHeader("Content-Type","application/json"),Je.onreadystatechange=function(){};try{var t=document.getElementById("name").value,n=document.getElementById("log").value,a=document.getElementById("pass").value,s=JSON.stringify({login:n,password:a,name:t,subject:c});Je.send(s)}catch(r){console.log(r)}},children:[Object(y.jsx)(fe.a,{id:"name",source:"nam",label:"\u0418\u043c\u044f"}),Object(y.jsx)(fe.a,{id:"log",source:"lo",label:"\u041b\u043e\u0433\u0438\u043d"}),Object(y.jsx)(fe.a,{id:"pass",source:"pa",label:"\u041f\u0430\u0440\u043e\u043b\u044c"}),Object(y.jsx)(Re.a,{onChange:function(e){return a(e.target.value)},defaultValue:"\u043c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u043a\u0430",id:"grouped",children:i.data.map((function(e){return Object(y.jsx)(He.a,{value:e,children:e})}))})]})}))})},Fe=Object(k.a)({table:{minWidth:650}}),Me=function(e){return Object(y.jsx)(Se.a,Object(K.a)(Object(K.a)({},e),{},{children:Object(y.jsx)(Ee.a,{label:"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c",basePath:"/\u0410\u0434\u043c\u0438\u043d\u044b"})}))},qe=function(e){var t=Fe(),n=Object(l.useState)([]),c=Object(P.a)(n,2),a=c[0],s=c[1],r=Object(l.useState)(!0),i=Object(P.a)(r,2),o=i[0],u=i[1],j=function(){var e=Object(I.a)(C.a.mark((function e(){return C.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.abrupt("return",fetch("http://localhost:5000/admins").then((function(e){return e.json()})).then((function(e){s(e),u(!1)})));case 1:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}();Object(l.useEffect)((function(){j(a)}),[]);var d=Object(l.useState)(""),b=Object(P.a)(d,2),h=b[0],O=b[1];return Object(y.jsx)(y.Fragment,{children:o?Object(y.jsx)(A.a,{className:"loaderApplication",type:"bubbles",color:"#",height:100,width:100}):Object(y.jsxs)(y.Fragment,{children:[Object(y.jsx)(Me,{}),Object(y.jsx)("input",{placeholder:"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u043c\u0435\u0440",type:"text",onChange:function(e){return O(e.target.value)}}),Object(y.jsx)(B.a,{styles:H.a,className:"page",children:Object(y.jsxs)(_.a,{className:t.table,size:"small","aria-label":"a dense table",children:[Object(y.jsx)(L.a,{children:Object(y.jsxs)(R.a,{children:[Object(y.jsx)(T.a,{align:"left",children:"\u0418\u043c\u044f"}),Object(y.jsx)(T.a,{align:"left",children:"\u041b\u043e\u0433\u0438\u043d"}),Object(y.jsx)(T.a,{align:"left",children:"\u041f\u0430\u0440\u043e\u043b\u044c"}),Object(y.jsx)(T.a,{align:"left",children:"\u041f\u0440\u0435\u0434\u043c\u0435\u0442"})]})}),Object(y.jsx)(N.a,{children:a.data.filter((function(e){return""===h||e.name.toLowerCase().includes(h.toLowerCase())?e:void 0})).map((function(e){return Object(y.jsxs)(R.a,{children:[Object(y.jsx)(T.a,{align:"left",children:e.name}),Object(y.jsx)(T.a,{align:"left",children:e.login}),Object(y.jsx)(T.a,{align:"left",children:e.password}),Object(y.jsx)(T.a,{align:"left",children:e.subject}),Object(y.jsx)(T.a,{align:"left",children:e.result})]},e.id)}))})]})})]})})},De=n(337),Ue=n.n(De),We=n(182),ze=n(336),Ke=n.n(ze),Xe=function(e){return Object(y.jsxs)(He.a,{onClick:function(){W.logout(),document.location.href="http://localhost:3000"},children:[Object(y.jsx)(Ue.a,{})," \u0412\u044b\u0439\u0442\u0438"]})},Ve="http://localhost:5000",Ge=X.a.fetchJson,Qe=Object(K.a)(Object(K.a)({},Q.a),{},{getList:function(e,t){var n=t.pagination,c=n.page,a=n.perPage,s=t.sort,r=s.field,i=s.order,o={sort:JSON.stringify([r,i]),range:JSON.stringify([(c-1)*a,c*a-1]),filter:JSON.stringify(t.filter)},l="".concat(Ve,"/sum?").concat(Object(ce.stringify)(o));return Ge(l).then((function(e){e.headers;var t=e.json;return{data:t.users.slice(40*(c-1),40*c).map((function(e){return Object(K.a)({id:e.id},e)})),total:parseInt(t.users.length/a,20)}}))},getOne:function(e,t){return Ge("".concat(Ve,"/users")).then().catch((function(e){return console.log(e),Promise.reject()}))},getMany:function(e,t){return Promise.reject()},getManyReference:function(e,t){return Promise.resolve()},create:function(e,t){return Promise.resolve()},update:function(e,t){if("posts"!==e||!t.data.pictures)return Q.a.update(e,t)},updateMany:function(e,t){return Promise.resolve()},delete:function(e,t){return Ge("".concat(Ve,"/delete_user")).then().catch((function(e){return console.log(e),Promise.reject()}))},deleteMany:function(e,t){return Promise.resolve()}}),Ye=function(e){var t=Object(We.a)((function(){return Ke.a}),"ru"),n=JSON.parse(localStorage.getItem("auth")).speciality;return Object(y.jsxs)(V.a,{i18nProvider:t,dataProvider:Qe,logoutButton:Xe,authProvider:W,loginPage:z,children:["MainAdmin"===n?Object(y.jsx)(G.a,{name:"users",list:de,create:ge,edit:we}):Object(y.jsx)("div",{}),"MainAdmin"===n?Object(y.jsx)(G.a,{name:"\u0410\u0434\u043c\u0438\u043d\u044b",list:qe,create:Ae}):Object(y.jsx)("div",{}),Object(y.jsx)(G.a,{name:"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b",list:Ne,create:Le})]})},Ze=n(354),$e=function(e){var t=e.component,n=Object(Ze.a)(e,["component"]);return Object(y.jsx)(S.b,Object(K.a)(Object(K.a)({},n),{},{render:function(e){return U.isAuthenticated()?Object(y.jsx)(t,Object(K.a)({},e)):Object(y.jsx)(S.a,{to:{pathname:"/",state:{from:e.location}}})}}))},et={background:"#15cdfc",color:"white",height:"100%",minHeight:"100vh",display:"flex",justifyContent:"center",alignItems:"center"},tt=function(){return Object(y.jsx)("div",{style:et,children:Object(y.jsxs)("div",{children:[Object(y.jsx)("h1",{style:{"font-size":100},children:"\u041e\u0448\u0438\u0431\u043a\u0430 404"}),Object(y.jsx)("br",{}),Object(y.jsx)("h3",{style:{align:"center"},children:"\u0414\u0430\u043d\u043d\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u043d\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442("})]})})},nt=Object(k.a)({table:{minWidth:650}}),ct=function(){var e=window.location.href.replace(window.location.hash,"");e=e.split("/"),console.log(e),e=parseInt(e[4]);var t=Object(l.useState)({data:{}}),n=Object(P.a)(t,2),c=n[0],a=n[1],s=Object(l.useState)({users:[]}),r=Object(P.a)(s,2),i=r[0],o=r[1],u=function(){var t=Object(I.a)(C.a.mark((function t(){return C.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:fetch("http://localhost:5000/get_user/".concat(e)).then((function(e){return e.json()})).then((function(e){return a(e)}));case 1:case"end":return t.stop()}}),t)})));return function(){return t.apply(this,arguments)}}(),j=function(){var e=Object(I.a)(C.a.mark((function e(){return C.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:fetch("http://localhost:5000/sum").then((function(e){return e.json()})).then((function(e){return o(e)})).catch((function(e){return Promise.reject}));case 1:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}();Object(l.useEffect)((function(){u(),j()}),[]);var d=nt();return Object(y.jsxs)(y.Fragment,{children:[c.data.name,parseInt(e)-(e-1)<=i.users.length&&"undefiend"!==c.data.results?Object(y.jsx)(B.a,{styles:H.a,className:"page",children:Object(y.jsxs)(_.a,{className:d.table,size:"small","aria-label":"a dense table",children:[Object(y.jsx)(L.a,{children:Object(y.jsxs)(R.a,{children:[Object(y.jsx)(T.a,{children:"\u2116"}),Object(y.jsx)(T.a,{align:"left",children:"\u041a\u043b\u0430\u0441\u0441"})]})}),Object(y.jsx)(N.a,{children:Object(y.jsxs)(R.a,{children:[Object(y.jsx)(T.a,{component:"th",scope:"row",children:c.data.id}),Object(y.jsx)(T.a,{align:"left",children:c.data.class}),c.data.results.map((function(e){return Object(y.jsxs)(T.a,{align:"left",children:[" ",e.subject,Object(y.jsx)("br",{}),e.value]})}))]},c.data.id)})]})}):Object(y.jsx)("div",{children:"\u0422\u0430\u043a\u043e\u0433\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f \u043d\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442"})]})},at=Object(k.a)({table:{minWidth:650}});function st(){var e=at(),t=Object(l.useState)({data:[{}]}),n=Object(P.a)(t,2),c=n[0],a=n[1],s=Object(l.useState)(!0),r=Object(P.a)(s,2),i=r[0],o=r[1],u=function(){var e=Object(I.a)(C.a.mark((function e(){return C.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.abrupt("return",fetch("http://localhost:5000/users/betters").then((function(e){return e.json()})).then((function(e){a(e),o(!1)})));case 1:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}();return Object(l.useEffect)((function(){return u(c),0}),[]),Object(y.jsx)(y.Fragment,{children:i||"undefined"===c.users?Object(y.jsx)(A.a,{className:"loaderApplication",type:"bubbles",color:"#",height:100,width:100}):Object(y.jsxs)(y.Fragment,{children:[console.log(c),Object(y.jsx)(B.a,{styles:H.a,className:"page",children:Object(y.jsxs)(_.a,{className:e.table,size:"small","aria-label":"a dense table",children:[Object(y.jsx)(L.a,{children:Object(y.jsxs)(R.a,{children:[Object(y.jsx)(T.a,{children:"\u2116"}),Object(y.jsx)(T.a,{align:"left",children:"\u0418\u043c\u044f"}),Object(y.jsx)(T.a,{align:"left",children:"\u041a\u043b\u0430\u0441\u0441"}),Object(y.jsx)(T.a,{align:"left",children:"\u0411\u0443\u043a\u0432\u0430"}),Object(y.jsx)(T.a,{align:"left",children:"\u0411\u0430\u043b\u043b\u044b"})]})}),Object(y.jsx)(N.a,{children:c.data.map((function(e){return Object(y.jsxs)(R.a,{children:[Object(y.jsx)(T.a,{component:"th",scope:"row",children:e.id}),Object(y.jsx)(T.a,{align:"left",children:e.name}),Object(y.jsx)(T.a,{align:"left",children:e.class}),Object(y.jsx)(T.a,{align:"left",children:e.class_letter}),Object(y.jsx)(T.a,{align:"left",children:e.result})]},e.id)}))})]})})]})})}var rt=function(){return Object(y.jsx)(h.a,{children:Object(y.jsxs)(S.d,{children:[Object(y.jsx)($e,{path:"/admin",component:Ye}),Object(y.jsxs)(S.b,{exact:!0,path:"/",children:[Object(y.jsx)(w,{}),Object(y.jsx)(M,{})]}),Object(y.jsxs)(S.b,{exact:!0,path:"/first",children:[Object(y.jsx)(w,{}),Object(y.jsx)(M,{})]}),Object(y.jsxs)(S.b,{exact:!0,path:"/top",children:[Object(y.jsx)(w,{}),Object(y.jsx)(st,{})]}),Object(y.jsxs)(S.b,{path:"/userinfo",children:[Object(y.jsx)(w,{}),Object(y.jsx)(ct,{})]}),Object(y.jsx)(S.b,{exact:!0,path:"/log",children:Object(y.jsx)(z,{})}),Object(y.jsx)(S.b,{path:"*",component:tt})]})})},it=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,633)).then((function(t){var n=t.getCLS,c=t.getFID,a=t.getFCP,s=t.getLCP,r=t.getTTFB;n(e),c(e),a(e),s(e),r(e)}))},ot=n(350),lt=Object({NODE_ENV:"production",PUBLIC_URL:".",WDS_SOCKET_HOST:void 0,WDS_SOCKET_PATH:void 0,WDS_SOCKET_PORT:void 0,FAST_REFRESH:!0}).REACT_APP_AUTH0_DOMAIN,ut=Object({NODE_ENV:"production",PUBLIC_URL:".",WDS_SOCKET_HOST:void 0,WDS_SOCKET_PATH:void 0,WDS_SOCKET_PORT:void 0,FAST_REFRESH:!0}).REACT_APP_AUTH0_CLIENT_ID;j.a.render(Object(y.jsx)(ot.a,{domain:lt,clientId:ut,redirectUri:window.location.origin,children:Object(y.jsx)(rt,{})}),document.getElementById("root")),it()}},[[527,1,2]]]);
//# sourceMappingURL=main.b2a56a57.chunk.js.map