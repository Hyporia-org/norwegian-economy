/* Norsk Økonomi – felles funksjonalitet for alle sider.
   Lastes rett etter <body>. Tema settes umiddelbart; resten bindes ved DOMContentLoaded,
   etter at sidenes egne skript har registrert sine lyttere.
   - Tema: følger systeminnstilling, kan overstyres og huskes (localStorage, med try/catch).
   - Mobilmeny og nedtrekk for delrapporter.
   - Hjelpetekster: .fn-hjelp-knapper og .begrep med data-hjelp (hover, fokus og trykk).
   - Forhåndsvalg: .fn-presets med knapper som har data-verdier='{"id":verdi}'.
   - Delbare scenarioer: input med data-url lagres i adressen (?navn=verdi), og ?preset=<navn> velger et forhåndsvalg. */
(function(){
  'use strict';
  var LAGER='norsk-okonomi-tema';
  function les(){try{return localStorage.getItem(LAGER);}catch(e){return null;}}
  function skriv(v){try{localStorage.setItem(LAGER,v);}catch(e){}}
  function systemMork(){try{return window.matchMedia('(prefers-color-scheme: dark)').matches;}catch(e){return false;}}
  function settTema(t){
    document.body.dataset.tema=t;
    var k=document.getElementById('tema-knapp');
    if(k){k.textContent=t==='mork'?'Lys visning':'Mørk visning';k.setAttribute('aria-pressed',String(t==='mork'));}
  }
  var lagret=les();
  settTema(lagret||(systemMork()?'mork':'lys'));

  function $(s,r){return (r||document).querySelector(s);}
  function $$(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s));}
  function utlos(el){
    el.dispatchEvent(new Event('input',{bubbles:true}));
    el.dispatchEvent(new Event('change',{bubbles:true}));
  }
  function settVerdi(el,v){
    if(el.type==='checkbox'){el.checked=(v===true||v==='true'||v===1||v==='1');}
    else{el.value=String(v);}
  }
  function hentVerdi(el){return el.type==='checkbox'?el.checked:el.value;}

  document.addEventListener('DOMContentLoaded',function(){
    /* ---------- Tema ---------- */
    settTema(document.body.dataset.tema||'lys');
    var temaKnapp=document.getElementById('tema-knapp');
    if(temaKnapp)temaKnapp.addEventListener('click',function(){
      var ny=document.body.dataset.tema==='mork'?'lys':'mork';settTema(ny);skriv(ny);
    });

    /* ---------- Meny ---------- */
    var menyKnapp=$('.fn-meny-knapp'),nav=$('.fn-nav');
    if(menyKnapp&&nav){
      menyKnapp.addEventListener('click',function(){
        var apen=nav.classList.toggle('apen');menyKnapp.setAttribute('aria-expanded',String(apen));
      });
      nav.addEventListener('click',function(e){
        if(e.target.closest('a')){nav.classList.remove('apen');menyKnapp.setAttribute('aria-expanded','false');$$('.fn-del',nav).forEach(function(d){d.open=false;});}
      });
    }
    document.addEventListener('click',function(e){
      $$('.fn-del[open]').forEach(function(d){if(!d.contains(e.target))d.open=false;});
    });

    /* ---------- Hjelpetekster ---------- */
    var tip=document.createElement('div');
    tip.className='fn-tip';tip.id='fn-tip';tip.setAttribute('role','tooltip');tip.hidden=true;
    document.body.appendChild(tip);
    var aktiv=null,festet=false,skjulTimer=null;
    function vis(el){
      clearTimeout(skjulTimer);
      if(aktiv&&aktiv!==el){aktiv.removeAttribute('aria-describedby');if(aktiv.classList.contains('fn-hjelp'))aktiv.setAttribute('aria-expanded','false');}
      aktiv=el;tip.innerHTML='';
      var t=el.getAttribute('data-hjelp-tittel');
      if(t){var s=document.createElement('strong');s.textContent=t;tip.appendChild(s);}
      var p=document.createElement('span');p.textContent=el.getAttribute('data-hjelp')||'';tip.appendChild(p);
      var m=el.getAttribute('data-hjelp-meta');
      if(m){var mm=document.createElement('span');mm.className='fn-tip-meta';mm.textContent=m;tip.appendChild(mm);}
      tip.hidden=false;el.setAttribute('aria-describedby','fn-tip');
      if(el.classList.contains('fn-hjelp'))el.setAttribute('aria-expanded','true');
      var r=el.getBoundingClientRect(),bw=tip.offsetWidth,bh=tip.offsetHeight;
      var x=Math.min(Math.max(8,r.left+window.scrollX-12),window.scrollX+document.documentElement.clientWidth-bw-8);
      var y=r.bottom+window.scrollY+8;
      if(r.bottom+bh+16>window.innerHeight&&r.top>bh+16)y=r.top+window.scrollY-bh-8;
      tip.style.left=x+'px';tip.style.top=y+'px';
    }
    function skjul(){
      tip.hidden=true;festet=false;
      if(aktiv){aktiv.removeAttribute('aria-describedby');if(aktiv.classList.contains('fn-hjelp'))aktiv.setAttribute('aria-expanded','false');}
      aktiv=null;
    }
    function bindHjelp(el){
      if(el.dataset.fnBundet)return;el.dataset.fnBundet='1';
      if(el.classList.contains('fn-hjelp')){el.setAttribute('aria-expanded','false');if(!el.getAttribute('aria-label'))el.setAttribute('aria-label','Forklaring'+(el.getAttribute('data-hjelp-tittel')?': '+el.getAttribute('data-hjelp-tittel'):''));}
      if(!el.hasAttribute('tabindex')&&el.tagName!=='BUTTON')el.setAttribute('tabindex','0');
      el.addEventListener('mouseenter',function(){if(!festet)vis(el);});
      el.addEventListener('mouseleave',function(){if(!festet)skjulTimer=setTimeout(skjul,160);});
      el.addEventListener('focus',function(){if(!festet)vis(el);});
      el.addEventListener('blur',function(){if(!festet)skjulTimer=setTimeout(skjul,160);});
      el.addEventListener('click',function(e){
        e.preventDefault();e.stopPropagation();
        if(festet&&aktiv===el){skjul();}else{vis(el);festet=true;}
      });
    }
    $$('.fn-hjelp,.begrep[data-hjelp]').forEach(bindHjelp);
    window.fnBindHjelp=function(rot){$$('.fn-hjelp,.begrep[data-hjelp]',rot).forEach(bindHjelp);};
    tip.addEventListener('mouseenter',function(){clearTimeout(skjulTimer);});
    tip.addEventListener('mouseleave',function(){if(!festet)skjulTimer=setTimeout(skjul,160);});
    document.addEventListener('click',function(e){if(festet&&!tip.contains(e.target))skjul();});
    document.addEventListener('keydown',function(e){if(e.key==='Escape')skjul();});
    window.addEventListener('scroll',function(){if(!festet&&!tip.hidden)skjul();},{passive:true});

    /* ---------- Forhåndsvalg ---------- */
    function knapperIGruppe(g){return $$('button[data-verdier]',g);}
    function parse(b){try{return JSON.parse(b.getAttribute('data-verdier'));}catch(e){return {};}}
    function oppdaterAktiv(g){
      knapperIGruppe(g).forEach(function(b){
        var v=parse(b),lik=true;
        Object.keys(v).forEach(function(id){var el=document.getElementById(id);if(!el)return;var a=hentVerdi(el);if(String(a)!==String(v[id])&&!(el.type!=='checkbox'&&Number(a)===Number(v[id])&&a!==''))lik=false;});
        b.setAttribute('aria-pressed',String(lik));
      });
    }
    function brukPreset(b){
      var v=parse(b);
      Object.keys(v).forEach(function(id){var el=document.getElementById(id);if(el)settVerdi(el,v[id]);});
      Object.keys(v).forEach(function(id){var el=document.getElementById(id);if(el)utlos(el);});
      var g=b.closest('.fn-presets');if(g)oppdaterAktiv(g);
    }
    var grupper=$$('.fn-presets');
    grupper.forEach(function(g){
      knapperIGruppe(g).forEach(function(b){b.type='button';b.addEventListener('click',function(){brukPreset(b);skrivUrl();});});
      var ids={};knapperIGruppe(g).forEach(function(b){Object.keys(parse(b)).forEach(function(id){ids[id]=1;});});
      Object.keys(ids).forEach(function(id){var el=document.getElementById(id);if(el){el.addEventListener('input',function(){oppdaterAktiv(g);});el.addEventListener('change',function(){oppdaterAktiv(g);});}});
    });
    $$('[data-nullstill]').forEach(function(k){
      k.addEventListener('click',function(){
        var g=document.querySelector('.fn-presets[data-gruppe="'+k.getAttribute('data-nullstill')+'"]');
        var b=g&&(g.querySelector('button[data-standard]')||g.querySelector('button[data-verdier]'));
        if(b){brukPreset(b);skrivUrl();}
      });
    });

    /* ---------- Delbare scenarioer i adressen ---------- */
    var urlFelt=$$('[data-url]');
    function skrivUrl(){
      if(!urlFelt.length||!window.history||!history.replaceState)return;
      var p=new URLSearchParams(location.search);p.delete('preset');
      urlFelt.forEach(function(el){
        var def=el.getAttribute('data-standardverdi'),v=String(hentVerdi(el));
        if(def!==null&&def===v)p.delete(el.getAttribute('data-url'));else p.set(el.getAttribute('data-url'),v);
      });
      var q=p.toString();
      try{history.replaceState(null,'',location.pathname+(q?'?'+q:'')+location.hash);}catch(e){}
    }
    urlFelt.forEach(function(el){
      el.setAttribute('data-standardverdi',String(hentVerdi(el)));
      el.addEventListener('change',skrivUrl);
      el.addEventListener('input',function(){clearTimeout(el._fnT);el._fnT=setTimeout(skrivUrl,250);});
    });
    var params=new URLSearchParams(location.search),endret=[];
    var presetNavn=params.get('preset');
    if(presetNavn){var pb=document.querySelector('.fn-presets button[data-navn="'+presetNavn.replace(/"/g,'')+'"]');if(pb)brukPreset(pb);}
    urlFelt.forEach(function(el){
      var k=el.getAttribute('data-url');
      if(params.has(k)){settVerdi(el,params.get(k));endret.push(el);}
    });
    endret.forEach(utlos);
    grupper.forEach(oppdaterAktiv);
    $$('[data-kopier-lenke]').forEach(function(k){
      k.addEventListener('click',function(){
        skrivUrl();var url=location.href,o=k.textContent;
        function ok(){k.textContent='Lenke kopiert';setTimeout(function(){k.textContent=o;},1800);}
        if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(url).then(ok,function(){window.prompt('Kopier lenken:',url);});}
        else{window.prompt('Kopier lenken:',url);}
      });
    });

    /* ---------- Til toppen ---------- */
    if(document.body.hasAttribute('data-til-toppen')){
      var t=document.createElement('button');t.type='button';t.className='fn-til-toppen';t.textContent='↑ Til toppen';
      t.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'});});
      document.body.appendChild(t);
      var vent=false;
      window.addEventListener('scroll',function(){if(vent)return;vent=true;requestAnimationFrame(function(){t.classList.toggle('synlig',window.scrollY>900);vent=false;});},{passive:true});
    }
  });
})();
