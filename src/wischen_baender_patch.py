# DOCH! 26.11.2026: Staunen — nach oben wischen (am Ende des Inhalts) springt zur naechsten Leiste (Zitate -> Redewendungen -> Geschichte),
# nach unten wischen (am Anfang) zur vorigen. Mausrad ebenso. Studieren (Rueckkehr) wird nie automatisch ausgeloest. Idempotent.
import re, sys
s = open('index.html', encoding='utf-8').read()
if 'id="wischen-js"' in s: sys.exit('schon angewendet')
js = '''<script id="wischen-js">/* Staunen: Wischen blaettert zwischen den Leisten */
(function(){try{var SC=document.getElementById("hscroll");if(!SC)return;var K=["quotes","rede","hist"],y0=0,x0=0,t0=0,st0=0,busy=0;
function bars(){return K.map(function(k){return document.querySelector('.hb[data-k="'+k+'"]');});}
function vis(e){return e&&e.getBoundingClientRect().height>0;}
function cur(){var b=bars();if(!vis(b[0]))return -1;for(var i=0;i<b.length;i++)if(b[i].classList.contains("sel"))return i;return -1;}
function open(){return !!document.querySelector(".tlpop:not([hidden]),dialog[open]");}
function atEnd(){return SC.scrollTop+SC.clientHeight>=SC.scrollHeight-3;}
function atTop(){return SC.scrollTop<=2;}
function go(d){var i=cur();if(i<0||open()||Date.now()<busy)return;var j=i+d;if(j<0||j>=K.length)return;var b=bars()[j];if(!b)return;busy=Date.now()+700;b.click();}
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
