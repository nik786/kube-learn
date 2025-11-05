var Color1 = "#005191"
var Color2 = "#ff0000"
var blinkRate= 500;
bV  = parseInt(navigator.appVersion)
bNS = navigator.appName=="Netscape"
bIE = navigator.appName=="Microsoft Internet Explorer"
ok = false
var i=0;
function blinkLink(){
   ok =  true
   if ((bNS && bV >= 5) || (bIE && bV >= 4)){
      i++;
      if (i==1) C = Color1
      if (i==2) C = Color2
      if (bIE) BlinkLink.style.color=C
      if (bNS) document.getElementById('BlinkLink').style.color = C
      if (i > 2) i = 0
      timer=setTimeout('blinkLink()', blinkRate)
   }     
}
