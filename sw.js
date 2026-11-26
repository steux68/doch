/* Service-Worker: macht die Seite als App installierbar und lässt sie offline laufen.
   Online: bei jedem Öffnen wird beim Server nach einer neueren Fassung gefragt (cache:'no-cache'), die Antwort wird für später gemerkt.
   Offline (zum Beispiel im Stall): es kommt die zuletzt gemerkte Fassung. Die Update-Taste leert den Speicher. */
const CACHE='offline-v1';
/* Audit 27.11.: das gemeinsame Modul common.js gleich beim Installieren speichern, damit es auch beim ersten Start ohne Netz da ist */
self.addEventListener('install',e=>{self.skipWaiting();e.waitUntil(caches.open(CACHE).then(k=>k.add('common.js')).catch(()=>{}));});
/* Audit 27.11.: alte Kopien aus der früheren Update-Prüfung (index.html?t=…) aus dem Speicher räumen */
self.addEventListener('activate',e=>e.waitUntil(caches.open(CACHE).then(k=>k.keys().then(ks=>Promise.all(ks.filter(q=>/[?&](t|v)=\d{12,}/.test(q.url)).map(q=>k.delete(q))))).catch(()=>{}).then(()=>self.clients.claim())));
self.addEventListener('fetch',e=>{
  if(e.request.method!=='GET')return;
  const u=new URL(e.request.url);
  if(u.origin!==location.origin)return;
  if(u.pathname.endsWith('/version.txt'))return; /* Versions-Prüfung immer direkt beim Server, nie speichern */
  e.respondWith(
    fetch(e.request,{cache:'no-cache'}).then(r=>{
      if(r&&r.status===200&&r.type==='basic'){const c=r.clone();caches.open(CACHE).then(k=>k.put(e.request,c)).catch(()=>{});}
      return r;
    }).catch(()=>caches.match(e.request,{ignoreSearch:true}).then(m=>m||(e.request.mode==='navigate'?caches.match('./',{ignoreSearch:true}).then(x=>x||caches.match('index.html',{ignoreSearch:true})):undefined)).then(m=>m||Response.error()))
  );
});
