/**
 * Created by Kevin on 2016/12/6.
 */
// var switchbool = false;
var changePWBtnDom = document.getElementById("changePWBtn");
var myInfoBtnDom = document.getElementById("myInfoBtn");
var changePWDom = document.getElementById("changePWForm");
var myInfoCntntDom = document.getElementsByClassName("myInfoCntntDiv");
function onload(){
    switchbool = false;
    changePWDom.style.display="none";
}
function myInfoCntntDis(){
    changePWDom.style.display="none";
    for(var i=0;i<myInfoCntntDom.length;i++)
        myInfoCntntDom[i].style.display="block";
    changePWBtnDom.className="btn col-md-2 col-lg-2 myInfoLblUnSelected";
    myInfoBtnDom.className="btn col-md-2 col-lg-2 myInfoLblSelected";
}
function changePWDis(){
    changePWDom.style.display="block";
    for(var i=0;i<myInfoCntntDom.length;i++)
        myInfoCntntDom[i].style.display="none";
    changePWBtnDom.className="btn col-md-2 col-lg-2 myInfoLblSelected";
    myInfoBtnDom.className="btn col-md-2 col-lg-2 myInfoLblUnSelected";
}