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
  "title":"Clínica dental en Tenerife Sur | Ocean Clinik",
  "desc":"Clínica dental en Tenerife Sur con todos los tratamientos en un mismo centro: implantes, ortodoncia invisible, estética dental y más. Pide cita.",
  "h1":"Clínica dental en <span class=\"accent\">Tenerife Sur</span>: todo tu tratamiento en un solo sitio",
  "sub":"Implantes, ortodoncia invisible, estética dental y odontología general bajo un mismo equipo. Plan claro, presupuesto cerrado y opciones de financiación.",
  "promesas":["Todos los tratamientos","Presupuesto claro","Financiación a medida"],
  "intro":["Ocean Clinik es una <strong>clínica dental en Tenerife Sur</strong> donde resuelves tu boca completa en un mismo centro y con un mismo equipo, sin ir de un sitio a otro.",
           "Desde una limpieza hasta una rehabilitación completa sobre implantes: estudiamos tu caso, te damos un plan por fases y te acompañamos en todo el proceso."],
  "cards":[("ic-tooth","Odontología general","Revisiones, limpiezas, empastes y cuidado del día a día."),
           ("ic-shield","Implantes y rehabilitación","Soluciones fijas para recuperar dientes y función masticatoria."),
           ("ic-smile","Estética y ortodoncia","Ortodoncia invisible, carillas y blanqueamiento, según diagnóstico.")],
  "faqs":[("¿Tienen todos los tratamientos en la misma clínica?","Sí, integramos odontología general, implantes, ortodoncia y estética para que no tengas que desplazarte."),
          ("¿Ofrecen financiación?","Si procede, te explicamos las opciones de pago disponibles para adaptar el plan a tu situación."),
          ("¿Cómo pido cita?","Rellena el formulario o escríbenos por WhatsApp y te confirmamos tu cita.")]},

 {"slug":"implantes-dentales-tenerife-sur","city":"tenerife-sur","type":"Dentist","img":"foto-clinica.jpg",
  "kw":"implantes dentales Tenerife Sur","service":"Implantes dentales",
  "title":"Implantes dentales en Tenerife Sur | Ocean Clinik",
  "desc":"Implantes dentales en Tenerife Sur con diagnóstico previo y plan claro. También casos complejos. Pide tu valoración de implantes en Ocean Clinik.",
  "h1":"¿Te han dicho que necesitas implantes o que tu caso es <span class=\"accent\">complicado</span>?",
  "sub":"<strong>Implantes dentales en Tenerife Sur</strong>, para casos simples y complejos. Estudiamos tu caso antes de proponerte nada, según diagnóstico.",
  "cta":"Quiero valorar mi caso de implantes",
  "promesas":["Tecnología 3D y cirugía guiada","Casos simples y complejos","Materiales de alta calidad"],
  "prose_h2":"Implantes dentales en Tenerife Sur, para casos simples y complejos",
  "intro":["En Ocean Clinik Abades valoramos casos de <strong>implantología avanzada, cirugía oral y rehabilitación dental</strong> con tecnología 3D, cirugía guiada y materiales de alta calidad.",
           "Estudiamos tu <strong>hueso, encía, mordida y estética</strong> antes de proponerte nada. Después te explicamos con claridad qué opciones tienes, qué solución recomendamos y cómo podemos ayudarte a recuperar tus dientes con seguridad.",
           "<strong>Implantes dentales en Tenerife Sur</strong> para casos simples y complejos."],
  "cards":[("ic-search","Estudio previo","Valoración de hueso, encía y mordida antes de decidir."),
           ("ic-shield","Casos complejos","Soluciones para pacientes con poco hueso o rechazados en otras clínicas."),
           ("ic-tooth","Solución fija","Recupera la mordida y la estética con dientes fijos.")],
  "faqs":[("¿Cuánto cuesta un implante dental?","Depende del diagnóstico y del plan recomendado para tu caso. Te lo explicamos con claridad en la valoración."),
          ("¿Y si me han dicho que no tengo hueso?","Pide una segunda opinión: existen técnicas para casos con poco hueso que valoramos según tu situación."),
          ("¿Duele ponerse un implante?","El tratamiento se realiza con anestesia y un protocolo cuidadoso; te explicamos cada fase antes de empezar.")]},

 {"slug":"ortodoncia-invisible-tenerife-sur","city":"tenerife-sur","type":"Dentist","img":"foto-clinica.jpg",
  "kw":"ortodoncia invisible Tenerife Sur","service":"Ortodoncia invisible",
  "title":"Ortodoncia invisible en Tenerife Sur | Ocean Clinik",
  "desc":"Ortodoncia invisible en Tenerife Sur: alinea tu sonrisa de forma discreta con alineadores transparentes. Pide tu valoración de ortodoncia.",
  "h1":"Ortodoncia invisible en <span class=\"accent\">Tenerife Sur</span> para alinear tu sonrisa sin que se note",
  "sub":"Alineadores transparentes, cómodos y removibles. Corrige la posición de tus dientes de forma discreta, con un plan que ves desde el principio.",
  "promesas":["Discreta y removible","Plan visual del caso","Revisiones de seguimiento"],
  "intro":["La <strong>ortodoncia invisible en Tenerife Sur</strong> te permite alinear los dientes sin brackets metálicos, con férulas transparentes que apenas se notan y puedes quitarte para comer y cepillarte.",
           "Antes de empezar valoramos mordida, encías y expectativas, y te explicamos el plan y la duración estimada según tu caso."],
  "cards":[("ic-smile","Casi invisible","Alineadores transparentes que pasan desapercibidos."),
           ("ic-plan","Plan claro","Sabes desde el inicio qué movimientos se buscan."),
           ("ic-heart","Cómoda","Removible para comer y mantener tu higiene de siempre.")],
  "faqs":[("¿La ortodoncia invisible sirve para todos los casos?","Es adecuada para muchos casos, pero no todos. Por eso valoramos tu mordida y encías antes de recomendarla."),
          ("¿Cuánto dura el tratamiento?","Depende de cada caso. Tras el estudio te damos una estimación realista de la duración."),
          ("¿Cuánto cuesta?","El precio depende de la complejidad. Te damos un presupuesto claro tras la valoración.")]},

 {"slug":"carillas-dentales-tenerife","city":"tenerife-sur","type":"Dentist","img":"foto-clinica.jpg",
  "kw":"carillas dentales Tenerife","service":"Carillas dentales",
  "title":"Carillas dentales en Tenerife | Ocean Clinik",
  "desc":"Carillas dentales en Tenerife para mejorar el color y la forma de tu sonrisa con un resultado natural. Pide tu valoración estética.",
  "h1":"Carillas dentales en <span class=\"accent\">Tenerife</span> para una sonrisa natural",
  "sub":"Mejora el color, la forma y la armonía de tu sonrisa con carillas. Diseñamos el resultado contigo, buscando siempre un acabado natural.",
  "promesas":["Resultado natural","Diseño de sonrisa","Según diagnóstico"],
  "intro":["Las <strong>carillas dentales en Tenerife</strong> son una opción para mejorar la estética de tu sonrisa cuando te molestan el color, la forma o pequeñas imperfecciones de los dientes.",
           "No todas las sonrisas necesitan lo mismo: por eso valoramos tu caso y te explicamos qué tipo de tratamiento (carillas u otras opciones) encaja mejor contigo, según diagnóstico."],
  "cards":[("ic-smile","Estética natural","Buscamos un resultado armónico, no artificial."),
           ("ic-search","Diseño previo","Planificamos la sonrisa antes de tocar tus dientes."),
           ("ic-shield","Criterio clínico","Te recomendamos solo lo que tiene sentido para tu caso.")],
  "faqs":[("¿Las carillas se notan?","El objetivo es un resultado natural, adaptado a tu rostro y al resto de tus dientes."),
          ("¿Son para siempre?","Son un tratamiento duradero con los cuidados adecuados; te explicamos su mantenimiento."),
          ("¿Cuánto cuestan las carillas?","Depende del número y del tipo. Te damos un presupuesto claro tras valorar tu caso.")]},

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
  "title":"Clínica dental en La Palma | Ocean Clinik",
  "desc":"Clínica dental en La Palma con todos los tratamientos en un mismo centro: implantes, ortodoncia invisible, estética dental y medicina estética. Pide cita.",
  "h1":"Clínica dental en <span class=\"accent\">La Palma</span>: tu boca completa en un solo centro",
  "sub":"Implantes, ortodoncia invisible, estética dental y medicina estética facial bajo un mismo equipo en Santa Cruz de La Palma. Plan claro y financiación.",
  "promesas":["Todos los tratamientos","Presupuesto claro","Financiación a medida"],
  "intro":["Ocean Clinik es una <strong>clínica dental en La Palma</strong> donde resuelves tu boca completa y también la estética facial, en el mismo centro y con el mismo equipo.",
           "Estudiamos tu caso, te damos un plan por fases y te acompañamos en todo el proceso, con criterio clínico y sin promesas irreales."],
  "cards":[("ic-tooth","Odontología general","Revisiones, limpiezas y cuidado del día a día."),
           ("ic-shield","Implantes y rehabilitación","Soluciones fijas, también para casos complejos."),
           ("ic-sparkle","Estética dental y facial","Carillas, blanqueamiento y medicina estética facial.")],
  "faqs":[("¿Qué tratamientos ofrecéis?","Odontología general, implantes, ortodoncia invisible, estética dental y medicina estética facial."),
          ("¿Dónde está la clínica?","En Avda. El Puente 41, 38700 Santa Cruz de La Palma."),
          ("¿Ofrecéis financiación?","Si procede, te explicamos las opciones de pago para adaptar el plan a tu situación.")]},

 {"slug":"implantes-dentales-la-palma","city":"la-palma","type":"Dentist","img":"foto-tratamiento.jpg",
  "kw":"implantes dentales La Palma","service":"Implantes dentales",
  "title":"Implantes dentales en La Palma | Ocean Clinik",
  "desc":"Implantes dentales en La Palma con diagnóstico previo y plan claro. Especialistas en casos complejos y poco hueso. Pide tu valoración de implantes.",
  "h1":"Implantes dentales en <span class=\"accent\">La Palma</span>, también en casos complejos",
  "sub":"Recupera tus dientes fijos con un plan basado en tu diagnóstico. Estudiamos hueso, mordida y estética. Si te dijeron que “no tienes hueso”, pide una segunda opinión.",
  "promesas":["Valoración con diagnóstico","Casos complejos","Financiación si procede"],
  "intro":["Los <strong>implantes dentales en La Palma</strong> te permiten recuperar la función y la seguridad al sonreír. En Ocean Clinik empezamos por tu diagnóstico, no por el precio.",
           "Estamos centrados también en casos complejos: pacientes con poco hueso, portadores de prótesis o que han sido rechazados en otras clínicas. Valoramos técnicas avanzadas según tu situación."],
  "cards":[("ic-search","Estudio previo","Valoración de hueso, encía y mordida."),
           ("ic-shield","Casos complejos","Soluciones cuando falta hueso o hay prótesis antigua."),
           ("ic-tooth","Solución fija","Recupera la mordida y la estética con dientes fijos.")],
  "faqs":[("¿Cuánto cuesta un implante en La Palma?","Depende del diagnóstico y del plan recomendado. Te lo explicamos con claridad en la valoración."),
          ("¿Tratáis casos con poco hueso?","Sí, es una de nuestras áreas. Pide una valoración aunque te hayan dicho que no en otro sitio."),
          ("¿Puedo dejar la dentadura por algo fijo?","En muchos casos sí. Valoramos tu situación y te explicamos las opciones fijas sobre implantes.")]},

 {"slug":"ortodoncia-invisible-la-palma","city":"la-palma","type":"Dentist","img":"foto-ortodoncia.jpg",
  "kw":"ortodoncia invisible La Palma","service":"Ortodoncia invisible",
  "title":"Ortodoncia invisible en La Palma | Ocean Clinik",
  "desc":"Ortodoncia invisible en La Palma con alineadores transparentes para alinear tu sonrisa de forma discreta. Pide tu valoración de ortodoncia.",
  "h1":"Ortodoncia invisible en <span class=\"accent\">La Palma</span> para alinear tu sonrisa sin que se note",
  "sub":"Alineadores transparentes, cómodos y removibles en Santa Cruz de La Palma. Corrige la posición de tus dientes de forma discreta, con un plan claro.",
  "promesas":["Discreta y removible","Plan visual del caso","Revisiones de seguimiento"],
  "intro":["La <strong>ortodoncia invisible en La Palma</strong> alinea los dientes sin brackets metálicos, con férulas transparentes que apenas se notan y te puedes quitar para comer y cepillarte.",
           "Antes de empezar valoramos mordida, encías y expectativas, y te explicamos el plan y la duración estimada para tu caso."],
  "cards":[("ic-smile","Casi invisible","Alineadores transparentes y discretos."),
           ("ic-plan","Plan claro","Sabes qué se busca desde el principio."),
           ("ic-heart","Cómoda","Removible para comer y tu higiene diaria.")],
  "faqs":[("¿Sirve para todos los casos?","Para muchos, pero no todos. Valoramos tu mordida y encías antes de recomendarla."),
          ("¿Cuánto dura?","Depende del caso; tras el estudio te damos una estimación realista."),
          ("¿Cuánto cuesta la ortodoncia invisible?","El precio depende de la complejidad. Te damos un presupuesto claro tras la valoración.")]},

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
    intro = "".join(f"<p>{x}</p>" for x in p["intro"])
    prose_h2 = p.get("prose_h2", f'{p["service"]} en {c["name"]}')
    cta_text = p.get("cta", "Quiero valorar mi caso")
    mid_block = ""
    if p.get("mid_img"):
        mid_block = (f'<section class="midimg soft"><div class="wrap"><figure>'
                     f'<div class="ph"><img src="/assets/fotos/{p["mid_img"]}" alt="{p.get("mid_caption","")}" loading="lazy" width="880" height="550"></div>'
                     f'<figcaption>{p.get("mid_caption","")}</figcaption></figure></div></section>')
    faqs_html = "".join(f'<details><summary>{q}</summary><div class="ans">{a}</div></details>' for q,a in p["faqs"])
    testi = testi_html()

    # related = otras páginas de la misma ciudad
    rel = [x for x in PAGES if x["city"]==p["city"] and x["slug"]!=p["slug"]]
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
      <div class="hero-cta">
        <a class="btn btn-lg" href="#cita">{cta_text} <svg class="ico"><use href="#ic-arrow"/></svg></a>
        <a class="btn wa btn-lg" href="{wa_link}" target="_blank" rel="noopener">{WA_SVG} WhatsApp</a>
      </div>
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
    <div class="sec-head" style="margin-bottom:22px"><h2>¿Qué necesitas solucionar?</h2></div>
    <div class="grid4">
      <a href="#cita"><span class="icbox"><svg class="ico"><use href="#ic-tooth"/></svg></span><b>Me falta una pieza o necesito implantes</b><span>Valoramos si puedes llevar dientes fijos, con planificación digital y opciones de financiación.</span></a>
      <a href="#cita"><span class="icbox"><svg class="ico"><use href="#ic-smile"/></svg></span><b>Quiero mejorar mi sonrisa</b><span>Ortodoncia invisible, carillas, blanqueamiento y estética dental según tu caso.</span></a>
      <a href="{tel_href}"><span class="icbox"><svg class="ico"><use href="#ic-phone"/></svg></span><b>Tengo dolor o una urgencia</b><span>Te orientamos rápido y buscamos el primer hueco disponible.</span></a>
      <a href="#cita"><span class="icbox"><svg class="ico"><use href="#ic-search"/></svg></span><b>Vengo de otra clínica y quiero una segunda opinión</b><span>Revisamos tu caso y te explicamos alternativas con claridad.</span></a>
    </div>
  </div>
</section>

<section class="stats">
  <div class="wrap">
    <div class="stat"><div class="n">+15</div><div class="l">años de experiencia</div></div>
    <div class="stat"><div class="n">+5.000</div><div class="l">pacientes atendidos</div></div>
    <div class="stat"><div class="n">4,9★</div><div class="l">valoración media</div></div>
    <div class="stat"><div class="n">Sí</div><div class="l">financiación a medida</div></div>
  </div>
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
    <div class="sec-head"><span class="eyebrow"><svg class="ico"><use href="#ic-shield"/></svg> Por qué Ocean Clinik</span><h2>Qué encontrarás en Ocean Clinik</h2></div>
    <div class="cards">{cards}</div>
  </div>
</section>

<section class="feature" id="doctor">
  <div class="wrap grid">
    <div class="ph">
      <img src="/assets/fotos/foto-doctor.jpg" alt="Dr. Claudio Vázquez, dirección clínica de Ocean Clinik" loading="lazy" width="520" height="650">
      <div class="badge"><b>Dr. Claudio Vázquez</b><span>Dirección clínica · Ocean Clinik {c['name']}</span></div>
    </div>
    <div>
      <span class="eyebrow"><svg class="ico"><use href="#ic-award"/></svg> Quién te atiende</span>
      <h2>Tratamientos dirigidos por el Dr. Claudio Vázquez</h2>
      <p>Antes de proponerte un tratamiento, necesitamos entender bien tu caso. El <strong>Dr. Claudio Vázquez</strong>, especialista en implantología, cirugía oral y rehabilitación dental, dirige los casos de implantes, cirugía guiada y tratamientos complejos en Ocean Clinik {c['name']}.</p>
      <p>Su forma de trabajar se basa en tres cosas: <strong>diagnóstico preciso, planificación digital y explicación clara al paciente</strong> antes de empezar. En la primera valoración revisaremos tu caso, te mostraremos lo que vemos y te explicaremos qué opciones tienes, qué recomendamos y qué puede pasar si lo dejas avanzar.</p>
      <ul class="checks">
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="20 6 9 17 4 12"/></svg><span>Diagnóstico individual.</span></li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="20 6 9 17 4 12"/></svg><span>Estudio con tecnología digital.</span></li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="20 6 9 17 4 12"/></svg><span>Planificación de implantes y cirugía guiada.</span></li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="20 6 9 17 4 12"/></svg><span>Explicación visual del caso.</span></li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="20 6 9 17 4 12"/></svg><span>Plan de tratamiento por escrito.</span></li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="20 6 9 17 4 12"/></svg><span>Opciones de financiación.</span></li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><polyline points="20 6 9 17 4 12"/></svg><span>Seguimiento durante todo el proceso.</span></li>
      </ul>
      <p style="margin-top:18px"><a class="btn" href="#cita">Quiero valorar mi caso <svg class="ico"><use href="#ic-arrow"/></svg></a></p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow"><svg class="ico"><use href="#ic-plan"/></svg> Sin sorpresas</span><h2>Cómo será tu primera valoración</h2></div>
    <div class="pasos">
      <div class="paso"><div class="n">1</div><h3>Nos cuentas qué te preocupa</h3><p>Dolor, estética, falta de piezas, miedo, presupuesto anterior o segunda opinión.</p></div>
      <div class="paso"><div class="n">2</div><h3>Revisamos tu boca y tu caso</h3><p>Usamos pruebas diagnósticas si son necesarias para entender bien el problema.</p></div>
      <div class="paso"><div class="n">3</div><h3>Te explicamos lo que vemos</h3><p>Sin tecnicismos innecesarios. Queremos que entiendas tu situación antes de decidir.</p></div>
      <div class="paso"><div class="n">4</div><h3>Te damos un plan claro</h3><p>Con fases, opciones y presupuesto por escrito.</p></div>
      <div class="paso"><div class="n">5</div><h3>Decides sin presión</h3><p>Te resolvemos dudas y puedes valorar la mejor opción para ti.</p></div>
    </div>
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
      <form onsubmit="event.preventDefault();this.querySelector('.btn').textContent='Solicitud enviada';">
        <label for="nombre">Nombre</label>
        <input id="nombre" name="name" type="text" autocomplete="name" placeholder="Tu nombre" required>
        <label for="tel">Teléfono móvil</label>
        <input id="tel" name="tel" type="tel" autocomplete="tel" placeholder="600 000 000" required>
        <p class="microcopy">Solo te contactaremos para gestionar tu cita.</p>
        <label for="email">Email <span style="color:#9aa6af;font-weight:400">(opcional)</span></label>
        <input id="email" name="email" type="email" autocomplete="email" placeholder="tucorreo@email.com">
        <label for="pref">¿Cuándo te viene mejor?</label>
        <select id="pref" name="pref" required>
          <option value="" selected disabled>Selecciona</option>
          <option>Hoy</option><option>Mañana</option><option>Esta semana</option><option>Me da igual</option>
        </select>
        <label class="consent"><input type="checkbox" required> He leído la <a href="/politica-privacidad/" style="color:var(--blue);font-weight:700">política de privacidad</a> y acepto el tratamiento de mis datos para gestionar mi cita.</label>
        <button type="submit" class="btn">Quiero que valoren mi caso</button>
        <p class="alt">¿Prefieres otra vía? <a href="{wa_link}" target="_blank" rel="noopener">WhatsApp</a> · <a href="mailto:{EMAIL}?subject=Valoraci%C3%B3n%20Ocean%20Clinik%20Tenerife%20Sur">Enviar email</a></p>
      </form>
    </div>
  </div>
</section>

<section class="testi soft">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow"><svg class="ico"><use href="#ic-star"/></svg> Opiniones reales</span><h2>Pacientes que ya confiaron en Ocean Clinik</h2><p>Antes de decidir, es normal querer saber cómo ha sido la experiencia de otros pacientes. Aquí puedes ver opiniones reales de personas que ya han venido a Ocean Clinik.</p></div>
    <!-- WIDGET DE RESEÑAS DE GOOGLE (en vivo): pega aquí el embed de tu proveedor
         (Trustindex / Elfsight / EmbedSocial) conectado a la ficha de Google de Ocean Clinik.
         Sustituye el bloque .rw-ph por el <script>+<div> del widget. -->
    <div class="reviews-widget" id="resenas-google">
      <div class="rw-ph">
        <span class="st">{STARS}</span>
        <b>Aquí se mostrarán vuestras reseñas reales de Google</b>
        <span class="note">Widget en vivo (se actualiza solo). El programador pega aquí el código de Trustindex o Elfsight conectado a vuestra ficha de Google.</span>
      </div>
    </div>
    <p style="text-align:center;margin-top:22px"><a class="btn ghost" href="{REVIEWS}" target="_blank" rel="noopener">Ver todas las reseñas en Google <svg class="ico"><use href="#ic-arrow"/></svg></a></p>
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
      <img class="logo" src="/assets/logo-white.png" alt="Ocean Clinik · Estudio Dental" width="150" height="58">
      <p><b>Ocean Clinik</b> · {c["addr"]}, {c["pc"]} {c["locality"]}</p>
      <p>Dirección clínica: Dr. Claudio Vázquez y equipo</p>
    </div>
    <div>
      <h4>Contacto</h4>
      <ul>
        <li><a href="{tel_href}">Teléfono: {c["tel"]}</a></li>
        <li><a href="{wa_link}" target="_blank" rel="noopener">WhatsApp: {c.get("wa","").replace("34"," +34 ",1).strip()}</a></li>
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
  <a class="btn tel" href="{tel_href}"><svg class="ico"><use href="#ic-phone"/></svg> Llamar</a>
  <a class="btn" href="#cita">Pedir cita</a>
</div>
</body>
</html>'''
    return html

# ====== ESCRIBIR ======
slugs=[]
ACTIVE=[x for x in PAGES if x["city"]=="tenerife-sur"]   # solo clínica de Tenerife Sur (Abades)
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
