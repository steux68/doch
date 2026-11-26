# DOCH! 26.11.2026: Staunen — nach oben wischen (am Ende des Inhalts) springt zur naechsten Leiste (Zitate -> Redewendungen -> Geschichte),
# nach unten wischen (am Anfang) zur vorigen; von der Titelseite (data-n=0) oeffnet Wischen nach oben zuerst Zitate, nach unten ueber Zitate schliesst sie wieder zur Titelseite. Stand: siehe index.html (id wischen-js). Mausrad ebenso. Studieren (Rueckkehr) wird nie automatisch ausgeloest. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="wischen-js"' in s: sys.exit('schon angewendet')
js = '''<script id="wischen-js">/* Staunen: Wischen blaettert zwischen Titelseite und den Leisten */
(function(){try{var SC=document.getElementById("hscroll");if(!SC)return;var y0=0,x0=0,t0=0,st0=0,busy=0;
function bars(){return [].slice.call(SC.querySelectorAll(":scope>.hb")).slice(0,3);}
function vis(){var b=bars()[0];return b&&b.getBoundingClientRect().height>0;}
function open(){return !!document.querySelector(".tlpop:not([hidden]),dialog[open]");}
function atEnd(){return SC.scrollTop+SC.clientHeight>=SC.scrollHeight-3;}
function atTop(){return SC.scrollTop<=2;}
function go(d){if(!SC.hasAttribute("data-n")||!vis()||open()||Date.now()<busy)return;var B=bars(),n=+SC.getAttribute("data-n"),j;
 if(n===0){if(d<0)return;j=0;}else{var i=n-1;j=i+d;if(j>=B.length)return;if(j<0)j=0;}
 if(!B[j])return;busy=Date.now()+800;B[j].click();}
SC.addEventListener("touchstart",function(e){var t=e.touches[0];y0=t.clientY;x0=t.clientX;t0=Date.now();st0=SC.scrollTop;},{passive:true});
SC.addEventListener("touchend",function(e){var t=e.changedTouches[0],dy=t.clientY-y0,dx=t.clientX-x0;if(Math.abs(dy)<70||Math.abs(dx)>Math.abs(dy)*.6||Date.now()-t0>900)return;
 if(e.target.closest&&e.target.closest("input,textarea,select,.svt,#sehb"))return;
 if(dy<0&&atEnd()&&st0>=SC.scrollHeight-SC.clientHeight-3)go(1);else if(dy>0&&atTop()&&st0<=2)go(-1);},{passive:true});
var wt=0;SC.addEventListener("wheel",function(e){if(Math.abs(e.deltaY)<40||Date.now()-wt<500)return;if(e.deltaY>0&&atEnd()){wt=Date.now();go(1);}else if(e.deltaY<0&&atTop()){wt=Date.now();go(-1);}},{passive:true});
}catch(e){}})();
</script>
'''
m = '<script id="autosnap-js">'
assert s.count(m) == 1
s = s.replace(m, js + m)
if '--noversion' not in sys.argv:
    s = re.sub(r'(<meta name="app-version" content=")([^"]*)(")', lambda x: x.group(1) + '2026-11-26zv' + x.group(3), s, count=1)
open('index.html', 'w', encoding='utf-8').write(s); print('ok')
