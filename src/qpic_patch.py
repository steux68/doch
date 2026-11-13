#!/usr/bin/env python3
"""Zitate-Popup: Foto der Person neben dem Namen (wie in der Liste), bei jedem Zitat, auch beim Blättern mit W/E und Wischen.
Idempotent. Run from the repo root: python3 src/qpic_patch.py"""
import re
f="index.html"
s=open(f,encoding="utf8").read()
if "qpic-css" in s:
    print("already patched"); raise SystemExit
old_h=""" $("qb").innerHTML='<h4>'+E(g(".who"))+'</h4><p class="qq">"""
new_h=""" const im=a.querySelector("img[data-w]"),wimg=im?im.dataset.w:"";
 $("qb").innerHTML='<div class="qtop"><span class="qpic" aria-hidden="true"><i>'+E(g(".pic i"))+'</i>'+(wimg?'<img alt="" data-w="'+E(wimg)+'">':'')+'</span><h4>'+E(g(".who"))+'</h4></div><p class="qq">"""
assert s.count(old_h)==1
s=s.replace(old_h,new_h)
old_c=""" $("qc").textContent=(i+1)+" / "+n;$("qb").scrollTop=0;}"""
new_c=""" if(typeof loadPics==="function")loadPics($("qb"));
 $("qc").textContent=(i+1)+" / "+n;$("qb").scrollTop=0;}"""
assert s.count(old_c)==1
s=s.replace(old_c,new_c)
css='''<style id="qpic-css">
.tlbody .qtop{display:flex;gap:12px;align-items:flex-start;margin:0 0 10px}
.tlbody .qtop h4{margin:0;flex:1;min-width:0}
.qpic{flex:none;width:96px;height:120px;position:relative;display:grid;place-items:center;font-size:20px;font-weight:700;background:var(--pale);overflow:hidden;box-sizing:border-box;outline:1px dotted #b8b8b8;outline-offset:-1px}
.qpic img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 20%;opacity:0;filter:grayscale(1)}
.qpic.has img{opacity:1}.qpic.has i{visibility:hidden}.qpic i{font-style:normal}
</style>
'''
marker='<script id="qpop-js">'
assert s.count(marker)==1
s=s.replace(marker,css+marker)
assert s.count('content="2026-11-11b"')==1
s=s.replace('content="2026-11-11b"','content="2026-11-13a"')
open(f,"w",encoding="utf8").write(s)
print("patched")
