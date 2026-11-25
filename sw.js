/* Service-Worker: macht die Seite als App installierbar und lässt sie offline laufen.
   Online: bei jedem Öffnen wird beim Server nach einer neueren Fassung gefragt (cache:'no-cache'), die Antwort wird für später gemerkt.
   Offline (zum Beispiel im Stall): es kommt die zuletzt gemerkte Fassung. Die Update-Taste leert den Speicher. */
const CACHE='offline-v1';
self.addEventListener('install',()=>self.skipWaiting());
self.addEventListener('activate',e=>e.waitUntil(self.clients.claim()));
self.addEventListener('fetch',e=>{
  if(e.request.method!=='GET')return;
  const u=new URL(e.request.url);
  if(u.origin!==location.origin)return;
  e.respondWith(
    fetch(e.request,{cache:'no-cache'}).then(r=>{
      if(r&&r.status===200&&r.type==='basic'){const c=r.clone();caches.open(CACHE).then(k=>k.put(e.request,c)).catch(()=>{});}
      return r;
    }).catch(()=>caches.match(e.request,{ignoreSearch:true}).then(m=>m||(e.request.mode==='navigate'?caches.match('./',{ignoreSearch:true}).then(x=>x||caches.match('index.html',{ignoreSearch:true})):undefined)).then(m=>m||Response.error()))
  );
});
