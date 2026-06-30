# -*- coding: utf-8 -*-
"""Generador de las 13 landings SEO de Ocean Clinik. Edita CONFIG y PAGES y ejecuta."""
import json, os, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ====== CONFIG (CAMBIAR por datos reales) ======
BASE_URL = "https://www.oceanclinik.es"          # dominio final (cambiar)
WA       = "34600000000"                          # WhatsApp real (cambiar)
REVIEWS  = "https://g.page/r/CAMBIAR-POR-TU-ENLACE-GOOGLE"  # enlace reseñas Google (cambiar)
EMAIL    = "info@theoceanclinik.com"               # email de contacto (confirmar)
TEL_LP   = "+34 600 000 000"                       # teléfono La Palma (cambiar)
TEL_TF   = "+34 600 000 000"                       # teléfono Tenerife Sur (cambiar)

CITIES = {
  "la-palma": {
    "name": "La Palma",
    "tel": TEL_LP,
    "addr": "Avda. El Puente 41",
    "locality": "Santa Cruz de La Palma",
    "region": "Santa Cruz de Tenerife",
    "pc": "38700",
    "area": ["Santa Cruz de La Palma","Los Llanos de Aridane","El Paso","Breña Alta","Breña Baja"],
    "hours": "Lun–Vie 9:00–20:00",
    "ohs": [{"d":["Monday","Tuesday","Wednesday","Thursday","Friday"],"o":"09:00","c":"20:00"}],
    "nap_note": "",
  },
  "tenerife-sur": {
    "name": "Tenerife Sur",
    "tel": "922 41 71 95",
    "wa": "34624506503",
    "addr": "C. 16 de Mayo, C.C. Abades, Local 5",
    "locality": "Abades",
    "region": "Santa Cruz de Tenerife",
    "pc": "38588",
    "area": ["Abades","Arico","El Médano","Los Abrigos","Granadilla de Abona","San Miguel de Abona","Adeje","Arona"],
    "hours": "Lun–Vie 10:00–14:00 y 15:00–19:00 · Sáb 10:00–14:00",
    "ohs": [
      {"d":["Monday","Tuesday","Wednesday","Thursday","Friday"],"o":"10:00","c":"14:00"},
      {"d":["Monday","Tuesday","Wednesday","Thursday","Friday"],"o":"15:00","c":"19:00"},
      {"d":["Saturday"],"o":"10:00","c":"14:00"},
    ],
    "nap_note": "Con aparcamiento",
  },
}

SPRITE = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
<symbol id="ic-check" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></symbol>
<symbol id="ic-phone" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></symbol>
<symbol id="ic-map" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></symbol>
<symbol id="ic-arrow" viewBox="0 0 24 24"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></symbol>
<symbol id="ic-tooth" viewBox="0 0 24 24"><path d="M12 5.5c-1.5-1.6-3.6-2.1-5.1-1.2C5 5.4 4.5 8.1 5.2 11c.4 1.9.7 3.9.9 5.8.2 1.7.5 3.2 1.4 3.2 1 0 1.2-1.6 1.5-3.1.2-1.1.5-1.9 1-1.9s.8.8 1 1.9c.3 1.5.5 3.1 1.5 3.1.9 0 1.2-1.5 1.4-3.2.2-1.9.5-3.9.9-5.8.7-2.9.2-5.6-1.7-6.7-1.5-.9-3.6-.4-5.1 1.2z"/></symbol>
<symbol id="ic-shield" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></symbol>
<symbol id="ic-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 14"/></symbol>
<symbol id="ic-star" viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></symbol>
<symbol id="ic-card" viewBox="0 0 24 24"><rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></symbol>
<symbol id="ic-team" viewBox="0 0 24 24"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></symbol>
<symbol id="ic-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></symbol>
<symbol id="ic-smile" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></symbol>
<symbol id="ic-sparkle" viewBox="0 0 24 24"><path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9L12 3z"/></symbol>
<symbol id="ic-plan" viewBox="0 0 24 24"><rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><line x1="9" y1="12" x2="15" y2="12"/><line x1="9" y1="16" x2="13" y2="16"/></symbol>
<symbol id="ic-calendar" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></symbol>
<symbol id="ic-clinic" viewBox="0 0 24 24"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="12" y1="6" x2="12" y2="11"/><line x1="9.5" y1="8.5" x2="14.5" y2="8.5"/><path d="M9 22v-4h6v4"/></symbol>
<symbol id="ic-heart" viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78L12 21.23l8.84-8.84a5.5 5.5 0 0 0 0-7.78z"/></symbol>
<symbol id="ic-chat" viewBox="0 0 24 24"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></symbol>
<symbol id="ic-mail" viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><polyline points="22 6 12 13 2 6"/></symbol>
</svg>'''

WA_SVG = '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.15-1.77-.87-2.04-.97-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.61-.92-2.21-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.06 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.69.63.71.22 1.36.19 1.87.12.57-.09 1.77-.72 2.02-1.42.25-.7.25-1.3.17-1.42-.07-.13-.27-.2-.57-.35zM12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.38 5.07L2 22l5.05-1.32A9.95 9.95 0 0 0 12 22c5.52 0 10-4.48 10-10S17.52 2 12 2z"/></svg>'

STAR_SVG = '<svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'
STARS = STAR_SVG*5

# JS del formulario: validación + confirmación + evento de conversión (GA4 dataLayer).
FORM_SCRIPT = '''<script>
(function(){
  var f=document.getElementById('lead-form'); if(!f) return;
  var tel=f.querySelector('#tel'), cons=f.querySelector('#consent'),
      nom=f.querySelector('#nombre'), treat=f.querySelector('#treat'), pref=f.querySelector('#pref');
  function showErr(name,on){var e=f.querySelector('.err[data-for="'+name+'"]'); if(e) e.style.display=on?'block':'none';}
  function push(ev){ try{ window.dataLayer=window.dataLayer||[]; window.dataLayer.push({event:ev}); }catch(e){} }
  var started=false;
  f.addEventListener('input',function(){ if(!started){started=true; push('form_start');} });
  if(treat) treat.addEventListener('change',function(){ push('select_treatment'); });
  if(pref) pref.addEventListener('change',function(){ push('select_time_preference'); });
  f.addEventListener('submit',function(ev){
    ev.preventDefault(); var ok=true;
    if(!nom.value.trim()){ ok=false; }
    var digits=(tel.value.match(/[0-9]/g)||[]).length;
    if(digits<9){ showErr('tel',true); ok=false; } else { showErr('tel',false); }
    if(treat && !treat.value){ ok=false; }
    if(pref && !pref.value){ ok=false; }
    if(cons && !cons.checked){ showErr('consent',true); ok=false; } else { showErr('consent',false); }
    if(!ok) return;
    f.style.display='none';
    var okBox=document.getElementById('form-ok'); if(okBox) okBox.hidden=false;
    push('form_submit'); push('generate_lead');
  });
})();
</script>'''

# Testimonios de ejemplo — SUSTITUIR por reseñas reales de Google
TESTIMONIALS = [
  ("Me explicaron todo con calma y sin presión. Salí sabiendo exactamente qué necesitaba y cuánto costaba.", "María G.", "Paciente"),
  ("Tenía miedo al dentista y aquí me sentí muy bien atendida. Trato cercano de principio a fin.", "Juan P.", "Paciente"),
  ("Pedí cita por WhatsApp y me la confirmaron enseguida. Muy profesionales y todo muy claro.", "Lucía R.", "Paciente"),
]
def testi_html():
    out=""
    for t,n,r in TESTIMONIALS:
        ini = n.strip()[0] if n.strip() else "·"
        out += f'<div class="tcard"><div class="st">{STARS}</div><p>“{t}”</p><div class="who"><span class="av">{ini}</span><div><b>{n}</b><span>{r}</span></div></div></div>'
    return out

def card(icon,title,desc,wa_msg=None,wa_base="#"):
    msg = wa_msg or title.lower()
    if wa_base and wa_base!="#":
        text = urllib.parse.quote(f"Hola, estaría interesado/a en {msg}.")
        attrs = f'href="{wa_base}?text={text}" target="_blank" rel="noopener"'
    else:
        attrs = 'href="#cita"'
    return (f'<a class="card" {attrs}><div class="icbox"><svg class="ico"><use href="#{icon}"/></svg></div>'
            f'<h3>{title}</h3><p>{desc}</p>'
            f'<span class="card-wa">{WA_SVG} Consultar por WhatsApp</span></a>')

def bullet(t):
    return f'<li><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>{t}</li>'

# ====== CONTENIDO POR PÁGINA ======
PAGES = [
 # ---------- TENERIFE SUR ----------
 {"slug":"dentista-tenerife-sur","city":"tenerife-sur","type":"Dentist","img":"foto-clinica.jpg",
  "kw":"dentista Tenerife Sur","service":"Dentista",
  "title":"Dentista en Tenerife Sur (Abades) | Ocean Clinik · Casos complejos",
  "desc":"Dentista en Tenerife Sur, en Abades. Cirugía de implantes guiada por ordenador, casos complejos y craneógrafo propio. Aparcamiento y primera valoración. Pide cita en Ocean Clinik.",
  "h1":"Dentista en <span class=\"accent\">Tenerife Sur</span> para recuperar tu sonrisa con seguridad, tecnología 3D y un plan claro desde la primera visita",
  "sub":"En Ocean Clinik Abades valoramos tu caso con calma, te enseñamos lo que vemos y te explicamos tus opciones sin presión. Implantes, ortodoncia, estética dental y casos complejos con diagnóstico digital, cirugía guiada y financiación a medida.",
  "promesas":["Diagnóstico digital","Cirugía guiada","Financiación a medida"],
  "prose_h2":"Clínica dental en Tenerife Sur, en Abades",
  "intro":["Ocean Clinik está en <strong>Abades, Arico</strong>, a pocos minutos de El Médano, Los Abrigos, Granadilla, San Miguel de Abona y Las Chafiras.",
           "Somos una <strong>clínica dental en Tenerife Sur</strong> especializada en tratamientos integrales: <strong>implantes dentales</strong>, cirugía guiada, <strong>ortodoncia invisible</strong>, <strong>estética dental</strong>, periodoncia, endodoncia y <strong>urgencias</strong>.",
           "Nuestro enfoque es sencillo: primero entendemos tu caso, después te explicamos el diagnóstico con imágenes y finalmente te damos un plan claro, por escrito y con opciones de financiación.",
           "Si te han dicho que tu caso es complicado, si tienes miedo al dentista o si llevas tiempo retrasando un tratamiento, pide una valoración. Muchas veces cuanto antes se actúa, más sencillo y menos agresivo puede ser el tratamiento."],
  "cards":[("ic-search","Diagnóstico digital para decidir con seguridad","No recomendamos tratamientos a ciegas. Estudiamos tu boca con tecnología digital para que entiendas qué ocurre y qué opciones tienes.","un diagnóstico digital"),
           ("ic-tooth","Implantes con cirugía guiada","Planificamos la colocación de implantes en 3D para buscar más precisión, comodidad y seguridad durante el tratamiento.","implantes con cirugía guiada"),
           ("ic-shield","Casos complejos y segundas opiniones","Si te han dicho que «no se puede», revisamos tu caso. Te diremos con claridad qué opciones existen y cuáles no recomendamos.","una segunda opinión para mi caso"),
           ("ic-card","Plan claro y financiación","Recibirás una propuesta por escrito, con fases, tiempos aproximados y opciones de pago si procede.","un plan de tratamiento con financiación")],
  "faqs":[("¿Cuánto cuesta un dentista en Tenerife Sur?","Depende del tratamiento y del diagnóstico. No cuesta lo mismo una revisión, una limpieza, una ortodoncia o un tratamiento con implantes. Por eso primero valoramos tu caso y después te damos un presupuesto claro por escrito."),
          ("¿Puedo financiar mi tratamiento dental?","Sí. En Ocean Clinik ofrecemos opciones de financiación para que puedas empezar el tratamiento sin renunciar a una solución adecuada para tu caso."),
          ("¿Hacéis implantes dentales en Tenerife Sur?","Sí. Realizamos tratamientos de implantología y cirugía guiada por ordenador, con planificación digital y estudio individual de cada caso."),
          ("¿Puedo pedir una segunda opinión dental?","Sí. Muchos pacientes vienen porque tienen dudas sobre un diagnóstico o presupuesto anterior. Revisamos tu caso y te explicamos las opciones con claridad."),
          ("¿Atendéis miedo al dentista?","Sí. Si tienes miedo, lo primero es explicarte todo con calma. El objetivo es que entiendas cada paso y no sientas que pierdes el control.")]},

 {"slug":"clinica-dental-tenerife-sur","city":"tenerife-sur","type":"Dentist","img":"foto-clinica.jpg",
  "kw":"clínica dental Tenerife Sur","service":"Clínica dental",
  "title":"Clínica dental en Tenerife Sur | Implantes y cirugía guiada | Ocean Clinik",
  "desc":"Clínica dental en Tenerife Sur, en Abades. Implantes dentales, cirugía guiada, ortodoncia invisible, estética dental y odontología general. Valoración, presupuesto claro y financiación.",
  "h1":"¿Llevas tiempo retrasando tu tratamiento dental o te han dicho que tu caso es <span class=\"accent\">complicado</span>?",
  "sub":"En Ocean Clinik Abades valoramos tu caso con calma y te damos un plan claro para recuperar tu boca con seguridad.<br><br>Implantes dentales, cirugía guiada, rehabilitación oral, ortodoncia invisible, estética dental y odontología general en Tenerife Sur, con tecnología digital, materiales de alta calidad y financiación a medida.",
  "refuerzo":"Primero estudiamos tu caso. Después te explicamos qué tienes, qué opciones existen y cuál es la solución más segura para ti.",
  "hero_micro":"Te contactamos por WhatsApp o teléfono para buscar el mejor hueco.",
  "wa_label":"Hablar por WhatsApp",
  "cta":"Quiero valorar mi caso",
  "promesas":["+5.000 pacientes atendidos","4,9★ valoración en Google","Implantes y casos complejos","Presupuesto claro por escrito","Financiación a medida"],
  "intent_title":"¿Qué necesitas solucionar?",
  "intent":[("ic-tooth","Me falta una pieza o varios dientes","Valoramos si puedes llevar implantes dentales, dientes fijos o una rehabilitación completa con planificación digital 3D.","#cita","Valorar implantes"),
            ("ic-shield","Me han dicho que no tengo hueso o que mi caso es difícil","Estudiamos casos complejos con cirugía guiada, regeneración ósea y planificación avanzada antes de proponerte una solución.","#cita","Pedir segunda opinión"),
            ("ic-smile","Quiero mejorar mi sonrisa","Ortodoncia invisible, carillas, blanqueamiento y estética dental según tu caso, tu boca y el resultado que buscas.","#cita","Valorar mi sonrisa"),
            ("ic-phone","Tengo dolor o una urgencia","Te orientamos rápido y buscamos el primer hueco disponible para valorar tu caso.","tel","Necesito cita urgente"),
            ("ic-search","Tengo un presupuesto de otra clínica","Revisamos tu diagnóstico, te explicamos las alternativas y te damos una opinión clara antes de que tomes una decisión.","#cita","Quiero una segunda opinión")],
  "prose_h2":"Clínica dental en Tenerife Sur, en Abades",
  "intro":["Ocean Clinik está en <strong>Abades, Arico</strong>, a pocos minutos de El Médano, Los Abrigos, Granadilla, San Miguel de Abona y Las Chafiras.",
           "Somos una <strong>clínica dental en Tenerife Sur</strong> especializada en tratamientos integrales: implantes dentales, cirugía guiada, rehabilitación oral, ortodoncia invisible, estética dental, odontología general, periodoncia, endodoncia y urgencias dentales.",
           "Nuestro enfoque es sencillo: primero entendemos tu caso, después te mostramos el diagnóstico con imágenes y finalmente te damos un plan claro, por escrito y con opciones de financiación.",
           "Si llevas tiempo sin ir al dentista, si tienes miedo, si te falta una pieza o si vienes de otra clínica con un presupuesto que no te han explicado bien, pide una valoración. Muchas veces actuar a tiempo evita tratamientos más largos, más incómodos y más costosos."],
  "cards_h2":"Por qué elegir Ocean Clinik Tenerife Sur",
  "cards":[("ic-search","Diagnóstico antes de presupuesto","No hacemos presupuestos rápidos sin entender tu boca. Primero valoramos tu caso, revisamos imágenes y te explicamos qué ocurre.","un diagnóstico antes del presupuesto"),
           ("ic-tooth","Implantes y cirugía guiada","Planificamos los casos de implantología con tecnología digital para buscar más precisión, seguridad y comodidad durante el tratamiento.","implantes con cirugía guiada"),
           ("ic-shield","Casos complejos y segundas opiniones","Si te han dicho que no tienes hueso, que tu caso es difícil o que necesitas una rehabilitación completa, podemos valorar tus opciones.","una segunda opinión para mi caso complejo"),
           ("ic-card","Plan completo por escrito","Recibirás una propuesta clara, con fases, tiempos aproximados, opciones de tratamiento y financiación si procede.","un plan de tratamiento por escrito"),
           ("ic-clinic","Todo tu caso en un mismo centro","Odontología general, implantes, ortodoncia, estética dental y prevención coordinadas por el mismo equipo.","resolver todo mi caso en un mismo centro")],
  "doctor_h2":"Tu caso será valorado por el Dr. Claudio Vázquez y su equipo",
  "doctor_badge":"Dirección clínica · Ocean Clinik Tenerife Sur",
  "doctor_p":["En Ocean Clinik Tenerife Sur, los casos de implantes dentales, cirugía guiada, rehabilitación oral y tratamientos complejos son dirigidos por el <strong>Dr. Claudio Vázquez</strong>, especialista en implantología, cirugía oral y rehabilitación dental.",
              "Su forma de trabajar se basa en tres pilares: <strong>diagnóstico preciso, planificación digital y explicación clara</strong> antes de empezar.",
              "Antes de proponerte un tratamiento, revisaremos tu caso, estudiaremos tu hueso, encía, mordida y estética, y te explicaremos qué opciones tienes, cuál recomendamos y qué puede pasar si lo dejas avanzar."],
  "doctor_checks":["Diagnóstico individual.","Estudio con tecnología digital.","Planificación de implantes y cirugía guiada.","Valoración de casos complejos.","Explicación visual del caso.","Plan de tratamiento por escrito.","Opciones de financiación.","Seguimiento durante todo el proceso."],
  "pasos":[("Nos cuentas qué te preocupa","Dolor, falta de piezas, miedo, estética, presupuesto anterior o una segunda opinión."),
           ("Estudiamos tu boca y tu caso","Revisamos tu situación con las pruebas necesarias para entender bien el problema antes de hablar de tratamiento."),
           ("Te enseñamos lo que vemos","Usamos imágenes y explicaciones claras para que entiendas qué ocurre en tu boca."),
           ("Te damos un plan por escrito","Con fases, tiempos aproximados, opciones de tratamiento y presupuesto claro."),
           ("Decides sin presión","Resolvemos tus dudas y te ayudamos a elegir la opción más adecuada para tu caso.")],
  "pasos_cta":"Pedir mi valoración dental",
  "form_treatments":["Implantes dentales","Segunda opinión","Ortodoncia invisible","Estética dental","Dolor o urgencia","Revisión general","No lo sé, quiero que me orienten"],
  "faqs":[("¿Cuál es la mejor clínica dental en Tenerife Sur?","La mejor clínica dental para ti será la que estudie bien tu caso, te explique el diagnóstico con claridad y te dé un plan de tratamiento adaptado a tu boca. En Ocean Clinik Abades trabajamos con diagnóstico digital, planificación de tratamientos y presupuesto por escrito para que puedas decidir con seguridad."),
          ("¿Hacéis implantes dentales en Tenerife Sur?","Sí. En Ocean Clinik realizamos tratamientos de implantología, cirugía guiada y rehabilitación oral. Valoramos cada caso de forma individual para estudiar el hueso, la encía, la mordida y la estética antes de proponer un tratamiento."),
          ("¿Puedo pedir una segunda opinión dental?","Sí. Muchos pacientes vienen con dudas sobre un diagnóstico o un presupuesto anterior. Revisamos tu caso, te explicamos las alternativas y te damos una valoración clara antes de que tomes una decisión."),
          ("¿Qué pasa si me han dicho que no tengo hueso para implantes?","En algunos casos existen alternativas como regeneración ósea, cirugía guiada u otros enfoques de rehabilitación. Para saberlo es necesario estudiar tu caso con pruebas diagnósticas y planificación adecuada."),
          ("¿Cuánto cuesta un tratamiento dental?","Depende del tratamiento y de la complejidad del caso. No cuesta lo mismo una revisión, una limpieza, una ortodoncia o una rehabilitación con implantes. Por eso primero valoramos tu caso y después te damos un presupuesto claro por escrito."),
          ("¿Ofrecéis financiación?","Sí. Si el tratamiento lo permite, te explicamos opciones de financiación para que puedas adaptar el pago a tu situación."),
          ("¿Dónde está Ocean Clinik Tenerife Sur?","Estamos en Abades, Arico, en C. 16 de Mayo, C.C. Abades, Local 5, 38588. Una ubicación cómoda para pacientes de Abades, El Médano, Los Abrigos, Granadilla, San Miguel de Abona y Las Chafiras."),
          ("¿Cómo puedo pedir cita?","Puedes rellenar el formulario, llamarnos o escribirnos por WhatsApp. Te contactaremos para confirmar el mejor hueco disponible.")]},

 {"slug":"implantes-dentales-tenerife-sur","city":"tenerife-sur","type":"Dentist","img":"foto-clinica.jpg",
  "kw":"implantes dentales Tenerife Sur","service":"Implantes dentales",
  "title":"Implantes dentales en Tenerife Sur | Casos complejos · Ocean Clinik",
  "desc":"Implantes dentales en Tenerife Sur, también casos complejos: implantes cigomáticos y subperiósticos cuando te han dicho que «no tienes hueso». Última tecnología y cirugía guiada. Pide tu valoración en Ocean Clinik.",
  "h1":"¿Te han dicho que <span class=\"accent\">no</span> te pueden poner implantes o que tu caso es complicado?",
  "sub":"<strong>Implantes dentales en Tenerife Sur</strong> para casos simples y complejos. Trabajamos con la última tecnología, incluidos <strong>implantes cigomáticos y subperiósticos</strong> para pacientes a los que han dicho que no se puede. Y si hacemos lo difícil, lo sencillo lo hacemos mejor que nadie.",
  "cta":"Quiero valorar mi caso de implantes",
  "promesas":["Cirugía guiada 3D","Cigomáticos y subperiósticos","Lo complejo y lo simple, mejor"],
  "prose_h2":"Implantes dentales en Tenerife Sur, también cuando te han dicho que no",
  "intro":["En Ocean Clinik Abades valoramos casos de <strong>implantología avanzada, cirugía oral y rehabilitación dental</strong> con la última tecnología, planificación 3D, cirugía guiada y materiales de alta calidad.",
           "Estudiamos tu <strong>hueso, encía, mordida y estética</strong> antes de proponerte nada. Después te explicamos con claridad qué opciones tienes, qué solución recomendamos y cómo podemos ayudarte a recuperar tus dientes con seguridad.",
           "Trabajamos casos que en otros sitios dan por imposibles. Cuando falta hueso y han descartado un implante convencional, valoramos técnicas avanzadas como los <strong>implantes cigomáticos</strong> (anclados en el pómulo) y los <strong>implantes subperiósticos</strong> (a medida, sobre el hueso). Si te han dicho que «no se puede», pide una segunda opinión antes de resignarte.",
           "Y algo importante: si resolvemos los casos más difíciles, <strong>los casos simples los hacemos aún mejor</strong>. Tanto si te falta una pieza como si necesitas rehabilitar toda la boca, tendrás un plan por escrito y opciones de financiación."],
  "cards":[("ic-search","Estudio previo en 3D","Valoramos hueso, encía y mordida con planificación digital antes de decidir nada.","un estudio de implantes en 3D"),
           ("ic-shield","Cigomáticos y subperiósticos","Cuando te han dicho que «no tienes hueso», valoramos técnicas avanzadas para que vuelvas a llevar dientes fijos.","implantes aunque me hayan dicho que no tengo hueso"),
           ("ic-tooth","Dientes fijos otra vez","Recupera la mordida y la estética con una solución fija, sin dentadura removible.","recuperar mis dientes con implantes fijos"),
           ("ic-card","Plan claro y financiación","Propuesta por escrito, con fases, tiempos aproximados y opciones de pago si procede.","un presupuesto de implantes con financiación")],
  "faqs":[("¿Cuánto cuesta un implante dental?","Depende del diagnóstico y del plan recomendado para tu caso. No es lo mismo un implante unitario que una rehabilitación completa. Te lo explicamos con claridad y por escrito en la valoración."),
          ("¿Y si me han dicho que no tengo hueso?","Pide una segunda opinión. Para casos con poca cantidad de hueso valoramos técnicas como los implantes cigomáticos o subperiósticos; muchas veces hay solución aunque te hayan dicho que no."),
          ("¿Qué son los implantes cigomáticos y subperiósticos?","Son soluciones para casos complejos con falta de hueso. El cigomático se ancla en el hueso del pómulo y el subperióstico es una estructura a medida que se apoya sobre el hueso. Valoramos si tu caso es candidato."),
          ("¿Duele ponerse un implante?","El tratamiento se realiza con anestesia y un protocolo cuidadoso. Te explicamos cada fase antes de empezar para que sepas en todo momento qué va a pasar."),
          ("¿Puedo financiar los implantes?","Sí. Te explicamos las opciones de financiación para que puedas empezar el tratamiento sin renunciar a la mejor solución para tu caso.")]},

 {"slug":"ortodoncia-invisible-tenerife-sur","city":"tenerife-sur","type":"Dentist","img":"foto-clinica.jpg",
  "kw":"ortodoncia invisible Tenerife Sur","service":"Ortodoncia invisible",
  "title":"Ortodoncia invisible en Tenerife Sur | +30 años · Ocean Clinik",
  "desc":"Ortodoncia invisible en Tenerife Sur con más de 30 años de experiencia. Alinea tu sonrisa de forma discreta con alineadores transparentes y un plan claro. Pide tu valoración en Ocean Clinik.",
  "h1":"Ortodoncia invisible en <span class=\"accent\">Tenerife Sur</span> con más de 30 años de experiencia alineando sonrisas",
  "sub":"Alineadores transparentes, cómodos y removibles, en manos de un equipo con <strong>más de 30 años de experiencia</strong> en ortodoncia. Antes de empezar valoramos tu caso, te enseñamos cómo quedaría y te damos un plan claro con la duración estimada y opciones de financiación.",
  "cta":"Quiero valorar mi ortodoncia",
  "promesas":["+30 años de experiencia","Discreta y removible","Financiación a medida"],
  "stats":[["+30","años de experiencia"],["+5.000","pacientes atendidos"],["4,9★","valoración media"],["Sí","financiación a medida"]],
  "doctor_kicker":"Quién te trata",
  "doctor_h2":"Ortodoncia con más de 30 años de experiencia",
  "doctor_p":["La ortodoncia no va solo de poner alineadores: va de <strong>planificar bien el movimiento de los dientes</strong> y controlar cada fase. En Ocean Clinik tratamos la ortodoncia con un equipo que acumula <strong>más de 30 años de experiencia</strong> alineando sonrisas.",
              "Antes de empezar estudiamos tu mordida y tus encías, te enseñamos el plan y te explicamos qué se puede conseguir de forma realista. El objetivo es que entiendas tu caso y veas el resultado previsto antes de dar el primer paso."],
  "doctor_checks":["Más de 30 años de experiencia en ortodoncia.","Estudio de mordida y encías.","Plan visual del caso antes de empezar.","Alineadores transparentes y cómodos.","Revisiones de seguimiento.","Opciones de financiación."],
  "doctor_badge":"Ortodoncia · Ocean Clinik Tenerife Sur",
  "prose_h2":"Ortodoncia invisible en Tenerife Sur, con más de 30 años de experiencia",
  "intro":["La <strong>ortodoncia invisible en Tenerife Sur</strong> te permite alinear los dientes sin brackets metálicos, con férulas transparentes que apenas se notan y que puedes quitarte para comer y cepillarte.",
           "En Ocean Clinik Abades tratamos la ortodoncia con un equipo de <strong>más de 30 años de experiencia</strong>. Valoramos primero tu <strong>mordida, encías y expectativas</strong>: no todas las sonrisas necesitan lo mismo, así que te explicamos si la ortodoncia invisible es la mejor opción para tu caso.",
           "Antes de empezar te enseñamos el plan: qué movimientos se buscan, cuánto puede durar de forma realista y cómo será el seguimiento hasta el final.",
           "Tanto si nunca te has tratado como si llevaste ortodoncia de joven y los dientes se han vuelto a mover, pide una valoración y te explicamos tus opciones, con financiación a medida."],
  "cards":[("ic-smile","Casi invisible","Alineadores transparentes que pasan desapercibidos en tu día a día y al hablar.","ortodoncia invisible"),
           ("ic-plan","Plan visual desde el principio","Te enseñamos qué movimientos se buscan y cómo quedaría tu sonrisa antes de empezar.","ver un plan de ortodoncia de mi caso"),
           ("ic-heart","Cómoda y removible","Te la quitas para comer y mantienes la higiene de siempre, sin renuncias.","ortodoncia con alineadores removibles"),
           ("ic-card","Financiación a medida","Un presupuesto claro por escrito y opciones de pago para empezar sin agobios.","ortodoncia invisible con financiación")],
  "faqs":[("¿La ortodoncia invisible sirve para todos los casos?","Es adecuada para muchos casos, pero no para todos. Por eso valoramos tu mordida y tus encías antes de recomendarla y te decimos con sinceridad si es tu mejor opción."),
          ("¿Cuánto dura el tratamiento?","Depende de cada caso. Tras el estudio te damos una estimación realista de la duración, sin prometer plazos imposibles."),
          ("¿Se nota al hablar?","Los alineadores son transparentes y se ajustan a tus dientes, así que pasan muy desapercibidos. Es uno de los motivos por los que tantos pacientes los eligen."),
          ("¿Puedo quitármela para comer?","Sí. Te la quitas para comer y para cepillarte, y vuelves a ponértela después. Por eso mantienes tu higiene de siempre."),
          ("¿Cuánto cuesta la ortodoncia invisible?","El precio depende de la complejidad del caso. Te damos un presupuesto claro por escrito tras la valoración, con opciones de financiación.")]},

 {"slug":"carillas-dentales-tenerife","city":"tenerife-sur","type":"Dentist","img":"foto-clinica.jpg",
  "kw":"carillas dentales Tenerife","service":"Carillas dentales",
  "title":"Carillas dentales en Tenerife | Ocean Clinik",
  "desc":"Carillas dentales en Tenerife para mejorar el color y la forma de tu sonrisa con un resultado natural. Pide tu valoración estética.",
  "h1":"Carillas dentales en <span class=\"accent\">Tenerife</span> para una sonrisa natural, diseñada contigo antes de empezar",
  "sub":"Mejora el color, la forma y la armonía de tu sonrisa con carillas. Diseñamos el resultado contigo y te lo enseñamos antes de tocar tus dientes, buscando siempre un acabado natural.",
  "cta":"Quiero valorar mi sonrisa",
  "promesas":["Resultado natural","Diseño de sonrisa previo","Según diagnóstico"],
  "prose_h2":"Carillas dentales en Tenerife, con un resultado natural",
  "intro":["Las <strong>carillas dentales en Tenerife</strong> son una opción para mejorar la estética de tu sonrisa cuando te molestan el color, la forma o pequeñas imperfecciones de los dientes.",
           "En Ocean Clinik Abades no todas las sonrisas necesitan lo mismo: valoramos tu caso y te explicamos qué tipo de tratamiento (carillas u otras opciones) encaja mejor contigo, según diagnóstico.",
           "Antes de tocar nada, <strong>diseñamos tu sonrisa</strong> y te enseñamos cómo quedaría, para que decidas con la información delante y sin sorpresas.",
           "Buscamos siempre la naturalidad: que el resultado encaje con tu rostro y con el resto de tus dientes, no una sonrisa artificial. Pide una valoración y te explicamos tus opciones con financiación a medida."],
  "cards":[("ic-smile","Estética natural","Buscamos un resultado armónico con tu rostro y tu sonrisa, no algo artificial.","carillas dentales con un resultado natural"),
           ("ic-search","Diseño de sonrisa previo","Planificamos y te enseñamos cómo quedaría antes de tocar tus dientes.","un diseño de sonrisa antes de empezar"),
           ("ic-sparkle","Color y forma a tu gusto","Mejoramos el color, la forma y la armonía de tus dientes según lo que te molesta.","mejorar el color y la forma de mis dientes"),
           ("ic-shield","Criterio clínico","Te recomendamos solo lo que tiene sentido para tu caso, no más de lo necesario.","saber si las carillas son para mi caso")],
  "faqs":[("¿Las carillas se notan?","El objetivo es un resultado natural, adaptado a tu rostro y al resto de tus dientes. Bien planificadas, pasan desapercibidas."),
          ("¿Hay que limar mucho los dientes?","Depende del tipo de carilla y de tu caso. Te explicamos en la valoración qué opción es la más conservadora para conseguir el resultado que buscas."),
          ("¿Son para siempre?","Son un tratamiento duradero con los cuidados adecuados. Te explicamos su mantenimiento para que duren el mayor tiempo posible."),
          ("¿Cuántas carillas necesito?","No siempre hacen falta muchas. Tras valorar tu sonrisa te decimos cuántas tendrían sentido para un resultado armónico, sin recomendarte de más."),
          ("¿Cuánto cuestan las carillas?","Depende del número y del tipo. Te damos un presupuesto claro por escrito tras valorar tu caso, con opciones de financiación.")]},

 # ---------- LA PALMA ----------
 {"slug":"dentista-la-palma","city":"la-palma","type":"Dentist","img":"foto-clinica.jpg",
  "kw":"dentista La Palma","service":"Dentista",
  "title":"Dentista en La Palma | Ocean Clinik · Santa Cruz de La Palma",
  "desc":"Dentista en La Palma con trato cercano, diagnóstico claro y presupuesto por escrito. Ocean Clinik, en Santa Cruz de La Palma. Pide tu cita.",
  "h1":"Dentista en <span class=\"accent\">La Palma</span> con trato cercano y explicaciones claras",
  "sub":"Tu dentista en Santa Cruz de La Palma. Revisamos tu boca, te explicamos lo que vemos y te damos un plan claro, sin prisas y sin promesas irreales.",
  "promesas":["Primera valoración","Presupuesto por escrito","Opciones de financiación"],
  "intro":["En Ocean Clinik somos tu <strong>dentista en La Palma</strong>, en pleno centro de Santa Cruz de La Palma. Odontología general y especializada con un trato humano y cercano.",
           "Empezamos siempre por entender tu caso: revisamos, te enseñamos lo que vemos y te proponemos un plan adaptado, según diagnóstico, para que decidas con tranquilidad."],
  "cards":[("ic-search","Diagnóstico claro","Te explicamos tu boca sin tecnicismos."),
           ("ic-clinic","Centro en el casco","En Avda. El Puente 41, fácil de localizar."),
           ("ic-team","Equipo completo","Dental y medicina estética en el mismo centro.")],
  "faqs":[("¿Dónde estáis en La Palma?","En Avda. El Puente 41, 38700 Santa Cruz de La Palma."),
          ("¿Cuánto cuesta la primera visita?","Te lo confirmamos al reservar; el objetivo es revisar tu caso y orientarte."),
          ("¿Atendéis a toda la isla?","Sí, recibimos pacientes de Santa Cruz de La Palma, Los Llanos de Aridane, El Paso y alrededores.")]},

 {"slug":"clinica-dental-la-palma","city":"la-palma","type":"Dentist","img":"foto-clinica.jpg",
  "kw":"clínica dental La Palma","service":"Clínica dental",
  "title":"Clínica dental en La Palma | Ocean Clinik · Santa Cruz de La Palma",
  "desc":"Clínica dental en La Palma, en Santa Cruz de La Palma, con todos los tratamientos en un mismo centro: implantes, ortodoncia invisible y estética dental. Plan claro y financiación. Pide cita en Ocean Clinik.",
  "h1":"Clínica dental en <span class=\"accent\">La Palma</span> donde resuelves toda tu boca en un mismo sitio, con un plan claro y sin ir de clínica en clínica",
  "sub":"En Ocean Clinik, en Santa Cruz de La Palma, reunimos odontología general, implantes, ortodoncia invisible y estética dental bajo un mismo equipo. Valoramos tu caso con calma, te enseñamos lo que vemos y te damos un plan por escrito con opciones de financiación.",
  "cta":"Quiero valorar mi caso",
  "promesas":["Todos los tratamientos","Presupuesto por escrito","Financiación a medida"],
  "prose_h2":"Clínica dental en La Palma, todo en un mismo centro",
  "intro":["Ocean Clinik está en el centro de <strong>Santa Cruz de La Palma</strong>, fácil de localizar y de acceso cómodo para toda la isla: Los Llanos de Aridane, El Paso, Breña Alta y Breña Baja.",
           "Somos una <strong>clínica dental en La Palma</strong> donde resuelves tu boca completa en un mismo centro y con un mismo equipo: <strong>odontología general</strong>, <strong>implantes</strong>, cirugía guiada, <strong>ortodoncia invisible</strong>, <strong>estética dental</strong>, periodoncia, endodoncia y <strong>urgencias</strong>.",
           "Nuestro enfoque es sencillo: primero entendemos tu caso, después te explicamos el diagnóstico con imágenes y finalmente te damos un plan claro, por escrito y con opciones de financiación.",
           "Si llevas tiempo retrasando ir al dentista o vienes con un presupuesto de otra clínica que no te han explicado bien, pide una valoración. Lo normal es salir sabiendo exactamente qué necesitas y cuánto cuesta."],
  "cards":[("ic-clinic","Toda tu boca en un mismo centro","No tienes que ir de un sitio a otro. Resolvemos odontología general, implantes, ortodoncia y estética con el mismo equipo.","resolver toda mi boca en una misma clínica en La Palma"),
           ("ic-tooth","Revisión y prevención","Revisiones, limpiezas, empastes y el cuidado del día a día para que no llegues tarde a los problemas.","una revisión y limpieza dental en La Palma"),
           ("ic-shield","Implantes y rehabilitación","Soluciones fijas para recuperar dientes y volver a masticar con seguridad, también en casos complejos.","implantes o una rehabilitación dental en La Palma"),
           ("ic-card","Plan claro y financiación","Recibirás una propuesta por escrito, con fases, tiempos aproximados y opciones de pago si procede.","un plan de tratamiento con financiación en La Palma")],
  "faqs":[("¿Tienen todos los tratamientos en la misma clínica?","Sí. Integramos odontología general, implantes, ortodoncia y estética dental para que resuelvas tu caso completo sin desplazarte a varios sitios."),
          ("¿Dónde está la clínica dental en La Palma?","En el centro de Santa Cruz de La Palma, fácil de localizar y con acceso cómodo desde toda la isla."),
          ("¿Cuánto cuesta ir a una clínica dental en La Palma?","Depende del tratamiento. No cuesta lo mismo una revisión, una limpieza, una ortodoncia o una rehabilitación con implantes. Por eso primero valoramos tu caso y después te damos un presupuesto claro por escrito."),
          ("¿Ofrecéis financiación?","Sí. Si procede, te explicamos las opciones de pago disponibles para que puedas empezar el tratamiento adaptándolo a tu situación."),
          ("¿Cómo pido cita?","Rellena el formulario o escríbenos por WhatsApp y te confirmamos tu cita en el primer hueco disponible.")]},

 {"slug":"implantes-dentales-la-palma","city":"la-palma","type":"Dentist","img":"foto-clinica.jpg",
  "kw":"implantes dentales La Palma","service":"Implantes dentales",
  "title":"Implantes dentales en La Palma | Casos complejos · Ocean Clinik",
  "desc":"Implantes dentales en La Palma, también casos complejos: implantes cigomáticos y subperiósticos cuando te han dicho que «no tienes hueso». Última tecnología y cirugía guiada. Pide tu valoración en Ocean Clinik.",
  "h1":"¿Te han dicho que <span class=\"accent\">no</span> te pueden poner implantes o que tu caso es complicado?",
  "sub":"<strong>Implantes dentales en La Palma</strong> para casos simples y complejos. Trabajamos con la última tecnología, incluidos <strong>implantes cigomáticos y subperiósticos</strong> para pacientes a los que han dicho que no se puede. Y si hacemos lo difícil, lo sencillo lo hacemos mejor que nadie.",
  "cta":"Quiero valorar mi caso de implantes",
  "promesas":["Cirugía guiada 3D","Cigomáticos y subperiósticos","Lo complejo y lo simple, mejor"],
  "prose_h2":"Implantes dentales en La Palma, también cuando te han dicho que no",
  "intro":["Los <strong>implantes dentales en La Palma</strong> te permiten recuperar la función y la seguridad al sonreír. En Ocean Clinik empezamos por tu diagnóstico, no por el precio, con la última tecnología, planificación 3D y cirugía guiada.",
           "Estudiamos tu <strong>hueso, encía, mordida y estética</strong> antes de proponerte nada. Después te explicamos con claridad qué opciones tienes, qué solución recomendamos y cómo podemos ayudarte a recuperar tus dientes con seguridad.",
           "Trabajamos casos que en otros sitios dan por imposibles. Cuando falta hueso y han descartado un implante convencional, valoramos técnicas avanzadas como los <strong>implantes cigomáticos</strong> (anclados en el pómulo) y los <strong>implantes subperiósticos</strong> (a medida, sobre el hueso). Si te han dicho que «no se puede», pide una segunda opinión antes de resignarte.",
           "Y algo importante: si resolvemos los casos más difíciles, <strong>los casos simples los hacemos aún mejor</strong>. Tanto si te falta una pieza como si necesitas rehabilitar toda la boca, tendrás un plan por escrito y opciones de financiación."],
  "cards":[("ic-search","Estudio previo en 3D","Valoramos hueso, encía y mordida con planificación digital antes de decidir nada.","un estudio de implantes en 3D en La Palma"),
           ("ic-shield","Cigomáticos y subperiósticos","Cuando te han dicho que «no tienes hueso», valoramos técnicas avanzadas para que vuelvas a llevar dientes fijos.","implantes aunque me hayan dicho que no tengo hueso"),
           ("ic-tooth","Dientes fijos otra vez","Recupera la mordida y la estética con una solución fija, sin dentadura removible.","recuperar mis dientes con implantes fijos en La Palma"),
           ("ic-card","Plan claro y financiación","Propuesta por escrito, con fases, tiempos aproximados y opciones de pago si procede.","un presupuesto de implantes con financiación en La Palma")],
  "faqs":[("¿Cuánto cuesta un implante dental en La Palma?","Depende del diagnóstico y del plan recomendado para tu caso. No es lo mismo un implante unitario que una rehabilitación completa. Te lo explicamos con claridad y por escrito en la valoración."),
          ("¿Y si me han dicho que no tengo hueso?","Pide una segunda opinión. Para casos con poca cantidad de hueso valoramos técnicas como los implantes cigomáticos o subperiósticos; muchas veces hay solución aunque te hayan dicho que no."),
          ("¿Qué son los implantes cigomáticos y subperiósticos?","Son soluciones para casos complejos con falta de hueso. El cigomático se ancla en el hueso del pómulo y el subperióstico es una estructura a medida que se apoya sobre el hueso. Valoramos si tu caso es candidato."),
          ("¿Puedo dejar la dentadura por algo fijo?","En muchos casos sí. Valoramos tu situación y te explicamos las opciones fijas sobre implantes."),
          ("¿Puedo financiar los implantes?","Sí. Te explicamos las opciones de financiación para que puedas empezar el tratamiento sin renunciar a la mejor solución para tu caso.")]},

 {"slug":"ortodoncia-invisible-la-palma","city":"la-palma","type":"Dentist","img":"foto-clinica.jpg",
  "kw":"ortodoncia invisible La Palma","service":"Ortodoncia invisible",
  "title":"Ortodoncia invisible en La Palma | +30 años · Ocean Clinik",
  "desc":"Ortodoncia invisible en La Palma con más de 30 años de experiencia. Alinea tu sonrisa de forma discreta con alineadores transparentes y un plan claro. Pide tu valoración en Ocean Clinik.",
  "h1":"Ortodoncia invisible en <span class=\"accent\">La Palma</span> con más de 30 años de experiencia alineando sonrisas",
  "sub":"Alineadores transparentes, cómodos y removibles en Santa Cruz de La Palma, en manos de un equipo con <strong>más de 30 años de experiencia</strong> en ortodoncia. Antes de empezar valoramos tu caso, te enseñamos cómo quedaría y te damos un plan claro con la duración estimada y opciones de financiación.",
  "cta":"Quiero valorar mi ortodoncia",
  "promesas":["+30 años de experiencia","Discreta y removible","Financiación a medida"],
  "stats":[["+30","años de experiencia"],["+5.000","pacientes atendidos"],["4,9★","valoración media"],["Sí","financiación a medida"]],
  "doctor_kicker":"Quién te trata",
  "doctor_h2":"Ortodoncia con más de 30 años de experiencia",
  "doctor_p":["La ortodoncia no va solo de poner alineadores: va de <strong>planificar bien el movimiento de los dientes</strong> y controlar cada fase. En Ocean Clinik tratamos la ortodoncia con un equipo que acumula <strong>más de 30 años de experiencia</strong> alineando sonrisas.",
              "Antes de empezar estudiamos tu mordida y tus encías, te enseñamos el plan y te explicamos qué se puede conseguir de forma realista. El objetivo es que entiendas tu caso y veas el resultado previsto antes de dar el primer paso."],
  "doctor_checks":["Más de 30 años de experiencia en ortodoncia.","Estudio de mordida y encías.","Plan visual del caso antes de empezar.","Alineadores transparentes y cómodos.","Revisiones de seguimiento.","Opciones de financiación."],
  "doctor_badge":"Ortodoncia · Ocean Clinik La Palma",
  "prose_h2":"Ortodoncia invisible en La Palma, con más de 30 años de experiencia",
  "intro":["La <strong>ortodoncia invisible en La Palma</strong> te permite alinear los dientes sin brackets metálicos, con férulas transparentes que apenas se notan y que puedes quitarte para comer y cepillarte.",
           "En Ocean Clinik, en Santa Cruz de La Palma, tratamos la ortodoncia con un equipo de <strong>más de 30 años de experiencia</strong>. Valoramos primero tu <strong>mordida, encías y expectativas</strong>: no todas las sonrisas necesitan lo mismo, así que te explicamos si la ortodoncia invisible es la mejor opción para tu caso.",
           "Antes de empezar te enseñamos el plan: qué movimientos se buscan, cuánto puede durar de forma realista y cómo será el seguimiento hasta el final.",
           "Tanto si nunca te has tratado como si llevaste ortodoncia de joven y los dientes se han vuelto a mover, pide una valoración y te explicamos tus opciones, con financiación a medida."],
  "cards":[("ic-smile","Casi invisible","Alineadores transparentes que pasan desapercibidos en tu día a día y al hablar.","ortodoncia invisible en La Palma"),
           ("ic-plan","Plan visual desde el principio","Te enseñamos qué movimientos se buscan y cómo quedaría tu sonrisa antes de empezar.","ver un plan de ortodoncia de mi caso"),
           ("ic-heart","Cómoda y removible","Te la quitas para comer y mantienes la higiene de siempre, sin renuncias.","ortodoncia con alineadores removibles"),
           ("ic-card","Financiación a medida","Un presupuesto claro por escrito y opciones de pago para empezar sin agobios.","ortodoncia invisible con financiación")],
  "faqs":[("¿La ortodoncia invisible sirve para todos los casos?","Es adecuada para muchos casos, pero no para todos. Por eso valoramos tu mordida y tus encías antes de recomendarla y te decimos con sinceridad si es tu mejor opción."),
          ("¿Cuánto dura el tratamiento?","Depende de cada caso. Tras el estudio te damos una estimación realista de la duración, sin prometer plazos imposibles."),
          ("¿Se nota al hablar?","Los alineadores son transparentes y se ajustan a tus dientes, así que pasan muy desapercibidos. Es uno de los motivos por los que tantos pacientes los eligen."),
          ("¿Puedo quitármela para comer?","Sí. Te la quitas para comer y para cepillarte, y vuelves a ponértela después. Por eso mantienes tu higiene de siempre."),
          ("¿Cuánto cuesta la ortodoncia invisible en La Palma?","El precio depende de la complejidad del caso. Te damos un presupuesto claro por escrito tras la valoración, con opciones de financiación.")]},

 # ---------- ODONTOPEDIATRÍA · OCEAN KIDS ----------
 {"slug":"odontopediatria-tenerife-sur","city":"tenerife-sur","type":"Dentist","img":"foto-clinica.jpg",
  "kw":"odontopediatría Tenerife Sur","service":"Odontopediatría · Ocean Kids",
  "title":"Odontopediatría en Tenerife Sur · Ocean Kids | Dentista de niños sin miedo",
  "desc":"Odontopediatría en Tenerife Sur con Ocean Kids: dentista de niños con trato amable para que tu hijo vaya sin miedo. Primera visita en positivo, prevención y revisiones. Pide cita en Ocean Clinik Abades.",
  "h1":"<span class=\"accent\">Ocean Kids</span>: que tu hijo vaya al dentista en Tenerife Sur sin miedo y con una buena experiencia",
  "sub":"Odontopediatría en Ocean Clinik Abades pensada para los más peques. Cuidamos especialmente la primera visita para que sea positiva, vamos a su ritmo y le explicamos todo con palabras que entiende, para que coja confianza desde el principio.",
  "cta":"Quiero pedir cita para mi hijo/a",
  "promesas":["Sin miedo, en positivo","Trato adaptado a cada edad","Prevención desde pequeños"],
  "intent_title":"¿Qué necesita tu hijo o hija?",
  "intent":[("ic-smile","Es su primera visita al dentista","La preparamos en positivo para que sea una buena experiencia y no coja miedo.","#cita"),
            ("ic-shield","Tiene una caries o le duele","Lo valoramos con cuidado y te explicamos el tratamiento y cómo se lo contamos a tu hijo/a.","#cita"),
            ("ic-search","Quiero una revisión y prevención","Revisiones, sellados y flúor para prevenir y detectar a tiempo.","#cita"),
            ("ic-tooth","Me preocupa cómo le salen los dientes","Vigilamos el recambio y la mordida para guiar el crecimiento si hace falta.","#cita")],
  "doctor_kicker":"Ocean Kids","doctor_badge":"Ocean Kids · Ocean Clinik Tenerife Sur",
  "doctor_h2":"Ocean Kids: odontología infantil sin miedo",
  "doctor_p":["Para un niño, la clave no es solo tratar la caries: es que <strong>salga contento y sin miedo</strong> para querer volver. En Ocean Kids cuidamos cada primera visita para que sea una experiencia positiva, explicándole todo con palabras que entiende y a su ritmo.",
              "Trabajamos la <strong>prevención desde pequeños</strong> (revisiones, sellados, flúor y hábitos) y vigilamos cómo le salen los dientes y la mordida para actuar a tiempo si hace falta. Y tú estás informado en cada paso."],
  "doctor_checks":["Primera visita en positivo, sin agobios.","Trato adaptado a cada edad.","Explicaciones que el niño entiende.","Prevención: revisiones, sellados y flúor.","Control del recambio y la mordida.","Información clara para los padres."],
  "prose_h2":"Odontopediatría en Tenerife Sur con Ocean Kids",
  "intro":["<strong>Ocean Kids</strong> es la odontopediatría de Ocean Clinik en Abades: la odontología infantil pensada para que ir al dentista no dé miedo.",
           "Sabemos que la primera experiencia lo marca todo. Por eso cuidamos la <strong>primera visita</strong> para que sea positiva: vamos a su ritmo, le enseñamos las cosas poco a poco y se lo explicamos con palabras que entiende.",
           "Apostamos por la <strong>prevención desde pequeños</strong>: revisiones, sellados de fisuras, flúor y consejos de higiene y alimentación para evitar caries y detectar a tiempo cualquier problema.",
           "Y vigilamos cómo le salen los dientes y cómo cierra la mordida, para guiar el crecimiento si hiciera falta. Tú estás informado en cada paso y decides con tranquilidad."],
  "cards":[("ic-heart","Primera visita sin miedo","Preparamos la primera cita en positivo para que tu hijo/a coja confianza desde el principio.","la primera visita al dentista de mi hijo/a"),
           ("ic-shield","Caries y molestias con cuidado","Tratamos caries y pequeñas urgencias con mucho tacto y explicándoselo a su ritmo.","una caries o molestia de mi hijo/a"),
           ("ic-search","Revisiones y prevención","Revisiones, sellados y flúor para prevenir problemas y detectarlos a tiempo.","una revisión de prevención para mi hijo/a"),
           ("ic-tooth","Control del crecimiento","Vigilamos cómo le salen los dientes y la mordida para guiar el crecimiento si hace falta.","una valoración de la mordida de mi hijo/a")],
  "faqs":[("¿A qué edad debe ir mi hijo al dentista por primera vez?","Lo ideal es una primera visita temprana, normalmente alrededor del primer año o cuando salen los primeros dientes, para acostumbrarle y prevenir. Si tu hijo ya es mayor y nunca ha ido, también es buen momento."),
          ("¿Y si mi hijo tiene miedo al dentista?","Es muy normal. Por eso cuidamos especialmente la primera visita: vamos a su ritmo, le explicamos las cosas con palabras que entiende y buscamos que salga con una experiencia positiva."),
          ("¿Hacéis revisiones y prevención?","Sí. Revisiones, sellados de fisuras, flúor y consejos de higiene y alimentación para prevenir caries y detectar a tiempo cualquier problema."),
          ("¿Tratáis las caries en dientes de leche?","Sí. Aunque sean dientes de leche, conviene tratarlos para evitar dolor e infecciones y para no afectar a los dientes definitivos. Te explicamos cada caso."),
          ("¿Vigiláis si necesitará ortodoncia?","Sí. Controlamos el recambio de dientes y la mordida; si vemos que conviene guiar el crecimiento, te lo explicamos y valoramos las opciones a su debido tiempo.")]},

 {"slug":"odontopediatria-la-palma","city":"la-palma","type":"Dentist","img":"foto-clinica.jpg",
  "kw":"odontopediatría La Palma","service":"Odontopediatría · Ocean Kids",
  "title":"Odontopediatría en La Palma · Ocean Kids | Dentista de niños sin miedo",
  "desc":"Odontopediatría en La Palma con Ocean Kids: dentista de niños con trato amable para que tu hijo vaya sin miedo. Primera visita en positivo, prevención y revisiones. Pide cita en Ocean Clinik.",
  "h1":"<span class=\"accent\">Ocean Kids</span>: que tu hijo vaya al dentista en La Palma sin miedo y con una buena experiencia",
  "sub":"Odontopediatría en Ocean Clinik, en Santa Cruz de La Palma, pensada para los más peques. Cuidamos especialmente la primera visita para que sea positiva, vamos a su ritmo y le explicamos todo con palabras que entiende, para que coja confianza desde el principio.",
  "cta":"Quiero pedir cita para mi hijo/a",
  "promesas":["Sin miedo, en positivo","Trato adaptado a cada edad","Prevención desde pequeños"],
  "intent_title":"¿Qué necesita tu hijo o hija?",
  "intent":[("ic-smile","Es su primera visita al dentista","La preparamos en positivo para que sea una buena experiencia y no coja miedo.","#cita"),
            ("ic-shield","Tiene una caries o le duele","Lo valoramos con cuidado y te explicamos el tratamiento y cómo se lo contamos a tu hijo/a.","#cita"),
            ("ic-search","Quiero una revisión y prevención","Revisiones, sellados y flúor para prevenir y detectar a tiempo.","#cita"),
            ("ic-tooth","Me preocupa cómo le salen los dientes","Vigilamos el recambio y la mordida para guiar el crecimiento si hace falta.","#cita")],
  "doctor_kicker":"Ocean Kids","doctor_badge":"Ocean Kids · Ocean Clinik La Palma",
  "doctor_h2":"Ocean Kids: odontología infantil sin miedo",
  "doctor_p":["Para un niño, la clave no es solo tratar la caries: es que <strong>salga contento y sin miedo</strong> para querer volver. En Ocean Kids cuidamos cada primera visita para que sea una experiencia positiva, explicándole todo con palabras que entiende y a su ritmo.",
              "Trabajamos la <strong>prevención desde pequeños</strong> (revisiones, sellados, flúor y hábitos) y vigilamos cómo le salen los dientes y la mordida para actuar a tiempo si hace falta. Y tú estás informado en cada paso."],
  "doctor_checks":["Primera visita en positivo, sin agobios.","Trato adaptado a cada edad.","Explicaciones que el niño entiende.","Prevención: revisiones, sellados y flúor.","Control del recambio y la mordida.","Información clara para los padres."],
  "prose_h2":"Odontopediatría en La Palma con Ocean Kids",
  "intro":["<strong>Ocean Kids</strong> es la odontopediatría de Ocean Clinik en Santa Cruz de La Palma: la odontología infantil pensada para que ir al dentista no dé miedo.",
           "Sabemos que la primera experiencia lo marca todo. Por eso cuidamos la <strong>primera visita</strong> para que sea positiva: vamos a su ritmo, le enseñamos las cosas poco a poco y se lo explicamos con palabras que entiende.",
           "Apostamos por la <strong>prevención desde pequeños</strong>: revisiones, sellados de fisuras, flúor y consejos de higiene y alimentación para evitar caries y detectar a tiempo cualquier problema.",
           "Y vigilamos cómo le salen los dientes y cómo cierra la mordida, para guiar el crecimiento si hiciera falta. Tú estás informado en cada paso y decides con tranquilidad."],
  "cards":[("ic-heart","Primera visita sin miedo","Preparamos la primera cita en positivo para que tu hijo/a coja confianza desde el principio.","la primera visita al dentista de mi hijo/a"),
           ("ic-shield","Caries y molestias con cuidado","Tratamos caries y pequeñas urgencias con mucho tacto y explicándoselo a su ritmo.","una caries o molestia de mi hijo/a"),
           ("ic-search","Revisiones y prevención","Revisiones, sellados y flúor para prevenir problemas y detectarlos a tiempo.","una revisión de prevención para mi hijo/a"),
           ("ic-tooth","Control del crecimiento","Vigilamos cómo le salen los dientes y la mordida para guiar el crecimiento si hace falta.","una valoración de la mordida de mi hijo/a")],
  "faqs":[("¿A qué edad debe ir mi hijo al dentista por primera vez?","Lo ideal es una primera visita temprana, normalmente alrededor del primer año o cuando salen los primeros dientes, para acostumbrarle y prevenir. Si tu hijo ya es mayor y nunca ha ido, también es buen momento."),
          ("¿Y si mi hijo tiene miedo al dentista?","Es muy normal. Por eso cuidamos especialmente la primera visita: vamos a su ritmo, le explicamos las cosas con palabras que entiende y buscamos que salga con una experiencia positiva."),
          ("¿Hacéis revisiones y prevención?","Sí. Revisiones, sellados de fisuras, flúor y consejos de higiene y alimentación para prevenir caries y detectar a tiempo cualquier problema."),
          ("¿Tratáis las caries en dientes de leche?","Sí. Aunque sean dientes de leche, conviene tratarlos para evitar dolor e infecciones y para no afectar a los dientes definitivos. Te explicamos cada caso."),
          ("¿Vigiláis si necesitará ortodoncia?","Sí. Controlamos el recambio de dientes y la mordida; si vemos que conviene guiar el crecimiento, te lo explicamos y valoramos las opciones a su debido tiempo.")]},

 {"slug":"medicina-estetica-la-palma","city":"la-palma","type":"MedicalClinic","img":"foto-facial.jpg",
  "kw":"medicina estética La Palma","service":"Medicina estética facial",
  "title":"Medicina estética en La Palma | Ocean Clinik",
  "desc":"Medicina estética facial en La Palma: tratamientos para verte mejor sin perder naturalidad, con valoración médica previa. Pide tu consulta.",
  "h1":"Medicina estética en <span class=\"accent\">La Palma</span> para verte mejor sin perder naturalidad",
  "sub":"Tratamientos faciales realizados con criterio médico en Santa Cruz de La Palma. Primero valoramos tu rostro y tus expectativas; después te proponemos lo que de verdad encaja contigo.",
  "promesas":["Valoración médica","Resultado natural","Plan personalizado"],
  "intro":["La <strong>medicina estética en La Palma</strong> de Ocean Clinik se centra en mejorar tu aspecto de forma natural, con un enfoque médico y prudente.",
           "No todos los rostros necesitan lo mismo. Por eso hacemos una valoración facial personalizada antes de recomendar ningún tratamiento, priorizando siempre la naturalidad y la seguridad."],
  "cards":[("ic-sparkle","Toxina botulínica","Suavizar arrugas de expresión, según valoración médica."),
           ("ic-heart","Ácido hialurónico","Hidratación y volumen facial con resultado natural."),
           ("ic-shield","Criterio médico","Te recomendamos solo lo que tenga sentido para tu caso.")],
  "faqs":[("¿Los tratamientos son seguros?","Se realizan con criterio médico y tras una valoración previa. Te explicamos beneficios y cuidados antes de empezar."),
          ("¿Se nota mucho el resultado?","Buscamos un resultado natural, no artificial, adaptado a tu rostro."),
          ("¿Necesito una consulta previa?","Sí, siempre valoramos tu caso antes de proponerte cualquier tratamiento.")]},

 {"slug":"botox-la-palma","city":"la-palma","type":"MedicalClinic","img":"foto-facial.jpg",
  "kw":"botox La Palma","service":"Bótox (toxina botulínica)",
  "title":"Bótox en La Palma | Ocean Clinik · Medicina estética",
  "desc":"Bótox (toxina botulínica) en La Palma para suavizar arrugas de expresión con un resultado natural y valoración médica previa. Pide tu consulta.",
  "h1":"Bótox en <span class=\"accent\">La Palma</span> para suavizar las arrugas de expresión",
  "sub":"Tratamiento con toxina botulínica realizado con criterio médico en Santa Cruz de La Palma. Buscamos suavizar la expresión sin perder naturalidad.",
  "promesas":["Valoración médica","Resultado natural","Profesionales cualificados"],
  "intro":["El <strong>bótox en La Palma</strong> (toxina botulínica) es un tratamiento para suavizar arrugas de expresión como las de la frente, el entrecejo o la zona de los ojos.",
           "En Ocean Clinik lo aplicamos con criterio médico y tras una valoración previa de tu rostro y tus expectativas, priorizando un resultado natural y la seguridad."],
  "cards":[("ic-sparkle","Arrugas de expresión","Frente, entrecejo y contorno de ojos, según valoración."),
           ("ic-shield","Criterio médico","Valoración previa y profesionales cualificados."),
           ("ic-heart","Naturalidad","Suavizar la expresión sin congelar el gesto.")],
  "faqs":[("¿El bótox congela la cara?","No es el objetivo. Buscamos suavizar la expresión manteniendo la naturalidad del gesto."),
          ("¿Cuánto dura el efecto?","El efecto es temporal y varía según la persona; te lo explicamos en la valoración."),
          ("¿Es seguro?","Se aplica con criterio médico tras una valoración previa. Te explicamos cuidados y recomendaciones.")]},

 {"slug":"acido-hialuronico-la-palma","city":"la-palma","type":"MedicalClinic","img":"foto-facial.jpg",
  "kw":"ácido hialurónico La Palma","service":"Ácido hialurónico",
  "title":"Ácido hialurónico en La Palma | Ocean Clinik",
  "desc":"Ácido hialurónico en La Palma para hidratar y dar volumen al rostro con resultado natural y valoración médica previa. Pide tu consulta.",
  "h1":"Ácido hialurónico en <span class=\"accent\">La Palma</span> para un rostro hidratado y armónico",
  "sub":"Tratamientos con ácido hialurónico realizados con criterio médico en Santa Cruz de La Palma. Hidratación, volumen y armonía facial con un acabado natural.",
  "promesas":["Valoración médica","Resultado natural","Plan personalizado"],
  "intro":["El <strong>ácido hialurónico en La Palma</strong> permite hidratar la piel, recuperar volumen y armonizar rasgos faciales de forma natural.",
           "Antes de cualquier tratamiento valoramos tu rostro y tus expectativas, y te explicamos qué se puede conseguir de forma realista, priorizando la naturalidad y la seguridad."],
  "cards":[("ic-heart","Hidratación y volumen","Recupera frescura y armonía facial."),
           ("ic-sparkle","Zonas faciales","Labios, surcos y contorno, según valoración médica."),
           ("ic-shield","Criterio médico","Valoración previa y resultado natural.")],
  "faqs":[("¿Se ve natural?","Sí, es nuestro objetivo: armonizar sin que se note artificial."),
          ("¿Cuánto dura?","El efecto es temporal y depende de la zona y la persona; te lo explicamos en la consulta."),
          ("¿Necesito valoración previa?","Sí, siempre valoramos tu caso antes de proponerte el tratamiento.")]},

 {"slug":"carillas-dentales-la-palma","city":"la-palma","type":"Dentist","img":"foto-sonrisa.jpg",
  "kw":"carillas dentales La Palma","service":"Carillas dentales",
  "title":"Carillas dentales en La Palma | Ocean Clinik",
  "desc":"Carillas dentales en La Palma para mejorar el color y la forma de tu sonrisa con un resultado natural. Pide tu valoración de estética dental.",
  "h1":"Carillas dentales en <span class=\"accent\">La Palma</span> para una sonrisa natural",
  "sub":"Mejora el color, la forma y la armonía de tu sonrisa con carillas en Santa Cruz de La Palma. Diseñamos el resultado contigo, buscando un acabado natural.",
  "promesas":["Resultado natural","Diseño de sonrisa","Según diagnóstico"],
  "intro":["Las <strong>carillas dentales en La Palma</strong> son una opción para mejorar la estética de tu sonrisa cuando te molestan el color, la forma o pequeñas imperfecciones.",
           "Valoramos tu caso y te explicamos qué tipo de tratamiento encaja mejor contigo (carillas u otras opciones), siempre según diagnóstico y buscando la naturalidad."],
  "cards":[("ic-smile","Estética natural","Un resultado armónico con tu rostro y tu sonrisa."),
           ("ic-search","Diseño previo","Planificamos la sonrisa antes de tocar tus dientes."),
           ("ic-shield","Criterio clínico","Solo te recomendamos lo que tiene sentido para tu caso.")],
  "faqs":[("¿Las carillas se notan?","Buscamos un resultado natural, adaptado al resto de tus dientes."),
          ("¿Cuánto duran?","Son un tratamiento duradero con los cuidados adecuados; te explicamos su mantenimiento."),
          ("¿Cuánto cuestan las carillas en La Palma?","Depende del número y el tipo. Te damos un presupuesto claro tras valorar tu caso.")]},
]

# Páginas que se publican (4 temas × 2 sedes). El resto quedan en PAGES pero no se generan.
ACTIVE_SLUGS = {
  "clinica-dental-la-palma","clinica-dental-tenerife-sur",
  "implantes-dentales-la-palma","implantes-dentales-tenerife-sur",
  "ortodoncia-invisible-la-palma","ortodoncia-invisible-tenerife-sur",
  "odontopediatria-la-palma","odontopediatria-tenerife-sur",
}

# ====== PLANTILLA ======
def build(p):
    c = CITIES[p["city"]]
    canonical = f"{BASE_URL}/{p['slug']}/"
    og_img = f"{BASE_URL}/assets/fotos/{p['img']}"
    tel_href = "tel:+34" + "".join(ch for ch in c["tel"] if ch.isdigit())[-9:]
    wa_link = f"https://wa.me/{c.get('wa', WA)}?text=" + ("Hola%2C%20quiero%20pedir%20cita%20de%20"+p['service']+"%20en%20"+c['name']).replace(" ","%20")

    promesas = "".join(f'<span><svg class="ico"><use href="#ic-check"/></svg> {x}</span>' for x in p["promesas"])
    wa_base = f"https://wa.me/{c.get('wa', WA)}"
    cards = "".join(card(x[0],x[1],x[2],(x[3] if len(x)>3 else None),wa_base) for x in p["cards"])
    cards_cls = f"cards cards-n{len(p['cards'])}"
    intro = "".join(f"<p>{x}</p>" for x in p["intro"])
    prose_h2 = p.get("prose_h2", f'{p["service"]} en {c["name"]}')
    cta_text = p.get("cta", "Quiero valorar mi caso")

    # --- Bloque "¿Qué necesitas solucionar?" (configurable por página) ---
    default_intent = [
      ("ic-tooth","Me falta una pieza o necesito implantes","Valoramos si puedes llevar dientes fijos, con planificación digital y opciones de financiación.","#cita"),
      ("ic-smile","Quiero mejorar mi sonrisa","Ortodoncia invisible, carillas, blanqueamiento y estética dental según tu caso.","#cita"),
      ("ic-phone","Tengo dolor o una urgencia","Te orientamos rápido y buscamos el primer hueco disponible.","tel"),
      ("ic-search","Vengo de otra clínica y quiero una segunda opinión","Revisamos tu caso y te explicamos alternativas con claridad.","#cita"),
    ]
    intent_title = p.get("intent_title","¿Qué necesitas solucionar?")
    intent_html = ""
    for it in p.get("intent", default_intent):
        ic,t,d,h = it[0],it[1],it[2],it[3]
        ictcrta = it[4] if len(it)>4 else None
        href = tel_href if h=="tel" else h
        cta_span = f'<span class="intent-cta">{ictcrta} <svg class="ico"><use href="#ic-arrow"/></svg></span>' if ictcrta else ""
        intent_html += f'<a href="{href}"><span class="icbox"><svg class="ico"><use href="#{ic}"/></svg></span><b>{t}</b><span>{d}</span>{cta_span}</a>'
    intent_cls = f"grid4 grid4-n{len(p.get('intent', default_intent))}"

    # --- Stats (configurable: ej. ortodoncia +30 años) ---
    default_stats = [("+15","años de experiencia"),("+5.000","pacientes atendidos"),("4,9★","valoración media"),("Sí","financiación a medida")]
    stats_html = "".join(f'<div class="stat"><div class="n">{n}</div><div class="l">{l}</div></div>' for n,l in p.get("stats", default_stats))

    # --- Sección del equipo / doctor (configurable: ej. Ocean Kids) ---
    doc_kicker = p.get("doctor_kicker","Quién te atiende")
    doc_h2 = p.get("doctor_h2","Tratamientos dirigidos por el Dr. Claudio Vázquez")
    doc_ps = p.get("doctor_p",[
      f"Antes de proponerte un tratamiento, necesitamos entender bien tu caso. El <strong>Dr. Claudio Vázquez</strong>, especialista en implantología, cirugía oral y rehabilitación dental, dirige los casos de implantes, cirugía guiada y tratamientos complejos en Ocean Clinik {c['name']}.",
      "Su forma de trabajar se basa en tres cosas: <strong>diagnóstico preciso, planificación digital y explicación clara al paciente</strong> antes de empezar. En la primera valoración revisaremos tu caso, te mostraremos lo que vemos y te explicaremos qué opciones tienes, qué recomendamos y qué puede pasar si lo dejas avanzar.",
    ])
    doc_checks = p.get("doctor_checks",[
      "Diagnóstico individual.","Estudio con tecnología digital.","Planificación de implantes y cirugía guiada.",
      "Explicación visual del caso.","Plan de tratamiento por escrito.","Opciones de financiación.","Seguimiento durante todo el proceso."])
    doc_badge = p.get("doctor_badge", f"Dirección clínica · Ocean Clinik {c['name']}")
    doc_ps_html = "".join(f"<p>{x}</p>" for x in doc_ps)
    doc_checks_html = "".join('<li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="20 6 9 17 4 12"/></svg><span>'+x+'</span></li>' for x in doc_checks)

    # --- Hero extra (refuerzo, microcopy, etiqueta WhatsApp) ---
    refuerzo_html = f'<p class="refuerzo">{p["refuerzo"]}</p>' if p.get("refuerzo") else ""
    hero_micro_html = f'<p class="hero-micro"><svg class="ico"><use href="#ic-chat"/></svg> {p["hero_micro"]}</p>' if p.get("hero_micro") else ""
    wa_label = p.get("wa_label","WhatsApp")

    # --- Sección "Por qué" (título configurable) ---
    cards_kicker = p.get("cards_kicker","Por qué Ocean Clinik")
    cards_h2 = p.get("cards_h2","Qué encontrarás en Ocean Clinik")

    # --- Pasos "Cómo será tu primera valoración" (configurable) ---
    default_pasos = [
      ("Nos cuentas qué te preocupa","Dolor, estética, falta de piezas, miedo, presupuesto anterior o segunda opinión."),
      ("Revisamos tu boca y tu caso","Usamos pruebas diagnósticas si son necesarias para entender bien el problema."),
      ("Te explicamos lo que vemos","Sin tecnicismos innecesarios. Queremos que entiendas tu situación antes de decidir."),
      ("Te damos un plan claro","Con fases, opciones y presupuesto por escrito."),
      ("Decides sin presión","Te resolvemos dudas y puedes valorar la mejor opción para ti."),
    ]
    pasos_html = "".join(f'<div class="paso"><div class="n">{i+1}</div><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(p.get("pasos", default_pasos)))
    pasos_cta_html = f'<p style="text-align:center;margin-top:30px"><a class="btn" href="#cita">{p["pasos_cta"]} <svg class="ico"><use href="#ic-arrow"/></svg></a></p>' if p.get("pasos_cta") else ""

    # --- Formulario: opciones del select de tratamiento + microcopy ---
    default_treatments = ["Implantes dentales","Ortodoncia invisible","Estética dental","Odontología general","Dolor o urgencia","Segunda opinión","No lo sé, quiero que me orienten"]
    treat_opts = "".join(f"<option>{t}</option>" for t in p.get("form_treatments", default_treatments))
    form_micro = p.get("form_micro","Solo usaremos tus datos para gestionar tu solicitud de cita.")

    # --- Barra fija móvil ---
    sticky_left = p.get("sticky_left","Llamar")
    sticky_right = p.get("sticky_right","Pedir valoración")

    mid_block = ""
    if p.get("mid_img"):
        mid_block = (f'<section class="midimg soft"><div class="wrap"><figure>'
                     f'<div class="ph"><img src="/assets/fotos/{p["mid_img"]}" alt="{p.get("mid_caption","")}" loading="lazy" width="880" height="550"></div>'
                     f'<figcaption>{p.get("mid_caption","")}</figcaption></figure></div></section>')
    faqs_html = "".join(f'<details><summary>{q}</summary><div class="ans">{a}</div></details>' for q,a in p["faqs"])
    testi = testi_html()

    # related = otras páginas de la misma ciudad
    rel = [x for x in PAGES if x["city"]==p["city"] and x["slug"]!=p["slug"] and x["slug"] in ACTIVE_SLUGS]
    related = "".join(f'<a href="/{x["slug"]}/">{x["service"]} en {CITIES[x["city"]]["name"]}</a>' for x in rel)
    treat = "".join(
        f'<a class="tcard-img" href="/{x["slug"]}/"><div class="ph"><img src="/assets/fotos/{x["img"]}" alt="{x["service"]} en {CITIES[x["city"]]["name"]}" loading="lazy" width="380" height="285"></div>'
        f'<div class="b"><h3>{x["service"]}</h3><span class="go"><svg class="ico"><use href="#ic-arrow"/></svg></span></div></a>'
        for x in rel[:3])

    # JSON-LD @graph
    biz = {
      "@type": p["type"],
      "@id": canonical + "#business",
      "name": f"Ocean Clinik — {p['service']} en {c['name']}",
      "image": og_img,
      "url": canonical,
      "telephone": c["tel"],
      "email": EMAIL,
      "priceRange": "€€",
      "address": {"@type":"PostalAddress","streetAddress":c["addr"],"addressLocality":c["locality"],"addressRegion":c.get("region",""),"postalCode":c["pc"],"addressCountry":"ES"},
      "areaServed": [{"@type":"City","name":a} for a in c["area"]],
      "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":x["d"],"opens":x["o"],"closes":x["c"]} for x in c["ohs"]],
      "sameAs": ["https://CAMBIAR-perfil-google-business"]
    }
    faqpage = {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p["faqs"]]}
    crumbs = {"@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Inicio","item":BASE_URL+"/"},
        {"@type":"ListItem","position":2,"name":f"{p['service']} en {c['name']}","item":canonical}]}
    graph = {"@context":"https://schema.org","@graph":[biz,faqpage,crumbs]}
    jsonld = json.dumps(graph, ensure_ascii=False, indent=2)

    nap_note = f'<br><em>{c["nap_note"]}</em>' if c["nap_note"] else ""

    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p["title"]}</title>
<meta name="description" content="{p["desc"]}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index,follow">
<meta property="og:type" content="website">
<meta property="og:title" content="{p["title"]}">
<meta property="og:description" content="{p["desc"]}">
<meta property="og:image" content="{og_img}">
<meta property="og:url" content="{canonical}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/landings.css">
<script type="application/ld+json">
{jsonld}
</script>
</head>
<body>
{SPRITE}

<header class="topbar">
  <div class="wrap">
    <a class="brand-lock" href="/" aria-label="Ocean Clinik inicio">
      <img src="/assets/logo-color.png" alt="Ocean Clinik · Estudio Dental" width="120" height="44">
      <span class="dr"><b>Dr. Claudio Vázquez</b>Dirección clínica</span>
    </a>
    <div class="topbar-cta">
      <a class="tellink" href="{tel_href}"><svg class="ico"><use href="#ic-phone"/></svg><span>{c["tel"]}</span></a>
      <a class="btn" href="#cita">Pedir cita</a>
    </div>
  </div>
</header>

<main>
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="rating"><span class="st">{STARS}</span> 4,9 · valoración de pacientes</span>
      <h1>{p["h1"]}</h1>
      <p class="sub">{p["sub"]}</p>
      {refuerzo_html}
      <div class="hero-cta">
        <a class="btn btn-lg" href="#cita">{cta_text} <svg class="ico"><use href="#ic-arrow"/></svg></a>
        <a class="btn wa btn-lg" href="{wa_link}" target="_blank" rel="noopener">{WA_SVG} {wa_label}</a>
      </div>
      {hero_micro_html}
      <div class="promesas">{promesas}</div>
      <div class="social"><span class="avatars"><span>M</span><span>J</span><span>L</span><span>+</span></span> <span><b>+5.000 pacientes</b> ya confían en Ocean Clinik</span></div>
    </div>
    <div class="hero-art">
      <div class="main"><img src="/assets/fotos/{p["img"]}" alt="{p["service"]} en {c['name']} — Ocean Clinik" width="540" height="560" fetchpriority="high"></div>
      <div class="glass rate"><span class="st">{STARS}</span><div><div class="big">4,9</div><small>en Google</small></div></div>
      <div class="glass nap"><b><svg class="ico"><use href="#ic-map"/></svg> {c["addr"]}</b><span>{c["locality"]} {c["pc"]} · {c["hours"]}{nap_note}</span></div>
      <a class="dr-chip" href="#doctor" aria-label="Conoce al Dr. Claudio Vázquez"><img src="/assets/fotos/foto-doctor.jpg" alt="Dr. Claudio Vázquez"><div><b>Dr. Claudio Vázquez</b><span>Conócelo →</span></div></a>
    </div>
  </div>
</section>

<section class="intent">
  <div class="wrap">
    <div class="sec-head" style="margin-bottom:22px"><h2>{intent_title}</h2></div>
    <div class="{intent_cls}">{intent_html}</div>
  </div>
</section>

<section class="stats">
  <div class="wrap">{stats_html}</div>
</section>

<section>
  <div class="wrap prose">
    <span class="eyebrow">{p["service"]} · {c['name']}</span>
    <h2>{prose_h2}</h2>
    {intro}
  </div>
</section>
{mid_block}
<section class="soft">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow"><svg class="ico"><use href="#ic-shield"/></svg> {cards_kicker}</span><h2>{cards_h2}</h2></div>
    <div class="{cards_cls}">{cards}</div>
  </div>
</section>

<section class="feature" id="doctor">
  <div class="wrap grid">
    <div class="ph">
      <img src="/assets/fotos/foto-doctor.jpg" alt="Dr. Claudio Vázquez, dirección clínica de Ocean Clinik" loading="lazy" width="520" height="650">
      <div class="badge"><b>Dr. Claudio Vázquez</b><span>{doc_badge}</span></div>
    </div>
    <div>
      <span class="eyebrow"><svg class="ico"><use href="#ic-team"/></svg> {doc_kicker}</span>
      <h2>{doc_h2}</h2>
      {doc_ps_html}
      <ul class="checks">{doc_checks_html}</ul>
      <p style="margin-top:18px"><a class="btn" href="#cita">{cta_text} <svg class="ico"><use href="#ic-arrow"/></svg></a></p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow"><svg class="ico"><use href="#ic-plan"/></svg> Sin sorpresas</span><h2>Cómo será tu primera valoración</h2></div>
    <div class="pasos">{pasos_html}</div>
    {pasos_cta_html}
  </div>
</section>

<section class="form-sec" id="cita">
  <div class="wrap form-grid">
    <div>
      <span class="eyebrow"><svg class="ico"><use href="#ic-calendar"/></svg> Pide tu valoración</span>
      <h2>Pide tu valoración dental en {c['name']}</h2>
      <p class="lead">Déjanos tus datos y te contactamos por WhatsApp o teléfono para buscar el mejor hueco.</p>
      <p style="color:#fff;font-weight:700;margin-bottom:8px">Ideal si necesitas:</p>
      <ul>
        <li><svg class="ico"><use href="#ic-check"/></svg> Implantes dentales</li>
        <li><svg class="ico"><use href="#ic-check"/></svg> Ortodoncia invisible</li>
        <li><svg class="ico"><use href="#ic-check"/></svg> Estética dental</li>
        <li><svg class="ico"><use href="#ic-check"/></svg> Dolor o urgencia</li>
        <li><svg class="ico"><use href="#ic-check"/></svg> Segunda opinión</li>
        <li><svg class="ico"><use href="#ic-check"/></svg> Presupuesto claro</li>
      </ul>
    </div>
    <div class="form-card">
      <h3>Pide tu valoración</h3>
      <p class="intro">Te contactamos por WhatsApp o teléfono.</p>
      <form id="lead-form" novalidate>
        <label for="nombre">Nombre</label>
        <input id="nombre" name="name" type="text" autocomplete="name" placeholder="Tu nombre" required>
        <label for="tel">Teléfono móvil</label>
        <input id="tel" name="tel" type="tel" inputmode="tel" autocomplete="tel" placeholder="600 000 000" required>
        <p class="err" data-for="tel">Revisa el número: necesitamos un móvil válido para poder confirmar tu cita.</p>
        <label for="treat">Tratamiento que te interesa</label>
        <select id="treat" name="treat" required>
          <option value="" selected disabled>Selecciona</option>
          {treat_opts}
        </select>
        <label for="pref">¿Cuándo te viene mejor?</label>
        <select id="pref" name="pref" required>
          <option value="" selected disabled>Selecciona</option>
          <option>Hoy</option><option>Mañana</option><option>Esta semana</option><option>Me da igual</option>
        </select>
        <label class="consent"><input type="checkbox" id="consent" required> He leído la <a href="/politica-privacidad/" style="color:var(--blue);font-weight:700">política de privacidad</a> y acepto el tratamiento de mis datos para gestionar mi cita.</label>
        <p class="err" data-for="consent">Debes aceptar la política de privacidad para que podamos gestionar tu solicitud.</p>
        <button type="submit" class="btn">Quiero que valoren mi caso</button>
        <p class="microcopy" style="text-align:center">{form_micro}</p>
        <p class="alt">¿Prefieres otra vía? <a href="{wa_link}" target="_blank" rel="noopener">WhatsApp</a> · <a href="mailto:{EMAIL}?subject=Valoraci%C3%B3n%20Ocean%20Clinik%20{c['name'].replace(' ','%20')}">Enviar email</a></p>
      </form>
      <div class="form-ok" id="form-ok" hidden><b>Gracias. Hemos recibido tu solicitud.</b><br>Te contactaremos por WhatsApp o teléfono para confirmar el mejor hueco disponible.</div>
    </div>
  </div>
</section>

<section class="testi soft">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow"><svg class="ico"><use href="#ic-star"/></svg> Opiniones reales</span><h2>Pacientes que ya confiaron en Ocean Clinik</h2><p>Antes de decidir, es normal querer saber cómo ha sido la experiencia de otros pacientes. Aquí puedes ver opiniones reales de personas que ya han venido a Ocean Clinik.</p></div>
    <!-- PROGRAMADOR: sustituye el bloque .rw-ph por el widget EN VIVO de Google
         (Trustindex / Elfsight / EmbedSocial) conectado a la ficha de Ocean Clinik.
         Mostrar mínimo 6 reseñas, priorizando trato, confianza, implantes, miedo al dentista y explicación clara. -->
    <div class="reviews-widget" id="resenas-google">
      <div class="rw-ph">
        <span class="st">{STARS}</span>
        <b>Valoración media 4,9★ en Google</b>
        <span class="note">Opiniones reales de pacientes que ya han confiado en Ocean Clinik.</span>
      </div>
    </div>
    <p style="text-align:center;margin-top:22px"><a class="btn ghost" href="{REVIEWS}" target="_blank" rel="noopener">Ver reseñas en Google <svg class="ico"><use href="#ic-arrow"/></svg></a></p>
  </div>
</section>

<section class="faq">
  <div class="wrap" style="max-width:820px">
    <div class="sec-head"><span class="eyebrow"><svg class="ico"><use href="#ic-chat"/></svg> Preguntas frecuentes</span><h2>{p["service"]} en {c['name']}: dudas frecuentes</h2></div>
    {faqs_html}
  </div>
</section>

<section class="treat soft">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow"><svg class="ico"><use href="#ic-tooth"/></svg> Más tratamientos</span><h2>Otros tratamientos en {c['name']}</h2></div>
    <div class="grid3">{treat}</div>
    <div class="related" style="margin-top:26px"><div class="links">{related}</div></div>
  </div>
</section>
</main>

<footer>
  <div class="wrap">
    <div>
      <img class="logo" src="/assets/logo-blanco.png" alt="Ocean Clinik · Estudio Dental" width="106" height="59">
      <p><b>Ocean Clinik</b> · {c["addr"]}, {c["pc"]} {c["locality"]}</p>
      <p>Dirección clínica: Dr. Claudio Vázquez y equipo</p>
    </div>
    <div>
      <h4>Contacto</h4>
      <ul>
        <li><a href="{tel_href}">Teléfono: {c["tel"]}</a></li>
        <li><a href="{wa_link}" target="_blank" rel="noopener">WhatsApp: {("+"+c.get("wa",WA)[:2]+" "+c.get("wa",WA)[2:]) if c.get("wa") else "consultar"}</a></li>
        <li><a href="mailto:{EMAIL}">Email: {EMAIL}</a></li>
        <li><a href="{REVIEWS}" target="_blank" rel="noopener">Reseñas en Google</a></li>
      </ul>
    </div>
    <div>
      <h4>Tratamientos</h4>
      <ul>{"".join(f'<li><a href="/{x["slug"]}/">{x["service"]} · {CITIES[x["city"]]["name"]}</a></li>' for x in rel[:5])}</ul>
    </div>
    <div class="legalbar wrap" style="grid-column:1/-1">
      © Ocean Clinik · {c["locality"]} · <a href="/politica-privacidad/">Política de privacidad</a> · <a href="/aviso-legal/">Aviso legal</a>
    </div>
  </div>
</footer>

<div class="sticky-cta">
  <a class="btn tel" href="{tel_href}"><svg class="ico"><use href="#ic-phone"/></svg> {sticky_left}</a>
  <a class="btn" href="#cita">{sticky_right}</a>
</div>
{FORM_SCRIPT}
</body>
</html>'''
    return html

# ====== ESCRIBIR ======
slugs=[]
ACTIVE=[x for x in PAGES if x["slug"] in ACTIVE_SLUGS]   # 4 temas × 2 sedes (La Palma + Abades)
for p in ACTIVE:
    d=os.path.join(ROOT,p["slug"])
    os.makedirs(d,exist_ok=True)
    with open(os.path.join(d,"index.html"),"w",encoding="utf-8") as f:
        f.write(build(p))
    slugs.append(p["slug"])
    print("OK",p["slug"])

# sitemap.xml
urls = [f"{BASE_URL}/"] + [f"{BASE_URL}/{s}/" for s in slugs]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemap.org/schemas/sitemap/0.9">\n'.replace("sitemap.org","sitemaps.org")
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls:
    sm += f"  <url><loc>{u}</loc><changefreq>monthly</changefreq><priority>0.8</priority></url>\n"
sm += "</urlset>\n"
open(os.path.join(ROOT,"sitemap.xml"),"w",encoding="utf-8").write(sm)
print("OK sitemap.xml")

# robots.txt
robots = f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml\n"
open(os.path.join(ROOT,"robots.txt"),"w",encoding="utf-8").write(robots)
print("OK robots.txt")
print("TOTAL páginas:", len(PAGES))
