# Guía SEO para el programador — Ocean Clinik

Cómo trabajar el SEO de las 13 landings locales. Resumen accionable basado en la estrategia
del documento de referencia (web dental que capta y lleva a reservar) y en las keywords objetivo.

---

## 1. Keywords → URL (1 landing por keyword)

| Keyword prioritaria | URL |
|---|---|
| dentista Tenerife Sur | `/dentista-tenerife-sur/` |
| clínica dental Tenerife Sur | `/clinica-dental-tenerife-sur/` |
| implantes dentales Tenerife Sur | `/implantes-dentales-tenerife-sur/` |
| ortodoncia invisible Tenerife Sur | `/ortodoncia-invisible-tenerife-sur/` |
| carillas dentales Tenerife | `/carillas-dentales-tenerife/` |
| dentista La Palma | `/dentista-la-palma/` |
| clínica dental La Palma | `/clinica-dental-la-palma/` |
| implantes dentales La Palma | `/implantes-dentales-la-palma/` |
| ortodoncia invisible La Palma | `/ortodoncia-invisible-la-palma/` |
| medicina estética La Palma | `/medicina-estetica-la-palma/` |
| botox La Palma | `/botox-la-palma/` |
| ácido hialurónico La Palma | `/acido-hialuronico-la-palma/` |
| carillas dentales La Palma | `/carillas-dentales-la-palma/` |

**Regla:** 1 keyword principal = 1 URL = 1 H1. No mezclar dos keywords principales en la misma página
(evita canibalización). Cada página ya trae su keyword en `title`, `meta description`, `H1`, primer
párrafo y `<h2>`.

---

## 2. On-page que ya viene hecho (no romper)

- `<title>` único por página con `keyword + ciudad + marca`.
- `meta description` única (~150–160 car.) con keyword + llamada a la acción.
- Un solo `<h1>` con la keyword y la ciudad. Jerarquía H2/H3 coherente.
- `<link rel="canonical">` absoluto en cada página.
- `robots: index,follow` en las 13 landings. `noindex` en legales y en `index.html` (preview).
- Open Graph (título, descripción, imagen, url).
- **Schema JSON-LD** por página: `Dentist`/`MedicalClinic` + `FAQPage` + `BreadcrumbList`.
- `sitemap.xml` y `robots.txt` en la raíz.
- Imágenes con `width`/`height` (evita CLS) y `alt` descriptivo; hero con `fetchpriority="high"`.
- Enlazado interno entre páginas de la misma ciudad (sección "Otros tratamientos" + footer).

---

## 3. Lo que el programador DEBE completar

Editar `seo-build/generate.py` (bloque `CONFIG`) y **regenerar** con `python3 seo-build/generate.py`,
o editar a mano en cada página:

1. `BASE_URL` → dominio final real (ahora `https://www.oceanclinik.es`). Afecta a canonical, OG, sitemap, schema.
2. `WA` → número de WhatsApp real (ahora `34600000000`).
3. `REVIEWS` → enlace real de reseñas de Google (ahora placeholder).
4. `TEL_LP` / `TEL_TF` → teléfonos reales de cada sede.
5. Dirección de **Tenerife Sur** (en `CITIES["tenerife-sur"]`): falta la dirección real (NAP).
6. `sameAs` del schema → URL del Perfil de Empresa de Google de cada sede.
7. Páginas legales (`/politica-privacidad/`, `/aviso-legal/`): redacción por un profesional (RGPD/AEPD).

> **NAP consistente:** Nombre, Dirección y Teléfono deben ser IDÉNTICOS en la web, en Google Business
> Profile y en directorios. Es un factor de SEO local.

---

## 4. SEO local (lo que más mueve el ranking local)

Según el documento, el ranking local depende de **relevancia, distancia y popularidad**. Acciones:

- **Google Business Profile** completo y verificado por sede (categoría correcta: "Dentista" / "Clínica
  dental" / "Médico estético"), horarios actualizados, fotos reales, enlace a la web y a la página de la sede.
- **Reseñas**: pedirlas de forma sistemática y **responderlas todas**. Enlazar a la ficha desde la web.
- Una landing por ciudad/servicio con **NAP + schema + FAQ local** (ya hecho).
- Tenerife Sur: si no hay dirección física verificable, el ranking local del "map pack" será limitado;
  prioriza primero la sede con dirección real (La Palma) y, para Tenerife Sur, trabaja contenido + GBP cuando exista local.

---

## 5. Rendimiento (Core Web Vitals — objetivos de Google)

Medir en p75 (PageSpeed/CrUX/RUM):

- **LCP ≤ 2,5 s** · **INP ≤ 200 ms** · **CLS ≤ 0,1**

Recomendaciones ya aplicadas / a mantener:
- CSS único compartido (`/styles.css`), sin frameworks pesados, JS mínimo.
- Imágenes con dimensiones explícitas; convertir las fotos a **WebP/AVIF** y comprimir (mejora LCP).
- La fuente carga con `display=swap` y `preconnect`. Si se busca LCP máximo, valorar `font-display`
  o fuente del sistema.
- `loading="lazy"` en imágenes below-the-fold (la hero NO debe ser lazy).
- Servir con HTTP/2, caché larga en `assets/` y compresión (gzip/brotli).

---

## 6. Conversión (estructura de la página)

Cada landing sigue el patrón del documento:
1. **Hero claro**: `[servicio] en [ciudad]` + subtítulo de confianza.
2. **CTA primaria única**: "Pedir cita". **CTA secundaria**: WhatsApp.
3. **Trust bar** antes del scroll largo (diagnóstico, presupuesto, criterio clínico, trato).
4. Contenido del servicio + "Cómo es tu primera visita" (4 pasos).
5. **Formulario corto** (modelo "cita rápida"): Nombre, Móvil, Preferencia + consentimiento.
6. FAQ + enlaces internos + footer con NAP.
7. **CTA sticky en móvil** (Llamar / Pedir cita).

Microcopy del formulario y consentimiento ya incluidos. Mantener el formulario corto:
si necesitas más datos, usar un segundo paso, no alargar el primero.

---

## 7. Formularios y captación de lead (conectar backend/CRM)

Ahora los formularios solo muestran confirmación visual. Hay que conectarlos. Recomendación del documento:

- Capa de backend propia con API REST + webhooks; agenda (Google Calendar/Calendly) y CRM desacoplados.
- Endpoint sugerido `POST /api/leads`. Payload con `source`, `flow`, `clinic_id`, `patient`,
  `intent` (treatment, urgency), `consent` (versión política + timestamp), `tracking` (utm/gclid).
- Validación en cliente y servidor; `autocomplete="name"`/`"tel"` (ya puesto); honeypot + rate limiting.
- Consentimiento: casilla **desmarcada por defecto**, separada, con info por capas (ya enlazada a la política).
- Datos de salud = categoría especial: **no** pedir síntomas/detalle clínico en el primer formulario.
- SLA real: si no hay agenda en vivo, el copy promete "te confirmamos por WhatsApp o teléfono" (cumplirlo).

---

## 8. Medición (GA4)

Eventos clave a instrumentar:
- `form_start`, `form_submit` (enhanced measurement) y **`generate_lead`** como evento clave.
- Eventos custom: `click_to_call`, `click_whatsapp`, `click_pedir_cita`.
- Marcar conversiones por landing/keyword para optimizar campañas.

Tests A/B sugeridos: titular beneficio vs servicio · "Pedir cita" vs "Reservar cita" ·
formulario 1 paso vs 2 pasos · CTA secundaria WhatsApp vs "Te llamamos".

---

## 9. Cómo regenerar las páginas

Todo el contenido vive en `seo-build/generate.py` (diccionario `PAGES` + `CONFIG`).
Edita y ejecuta:

```bash
python3 seo-build/generate.py
```

Genera las 13 carpetas `/<slug>/index.html`, `sitemap.xml` y `robots.txt`. Los estilos están en `/styles.css`.

---

## 10. Checklist de publicación

- [ ] Poner `BASE_URL` con el dominio final y regenerar.
- [ ] Teléfonos, WhatsApp, dirección de Tenerife Sur y enlace de reseñas reales.
- [ ] Conectar formularios al CRM/agenda (+ consentimiento registrado).
- [ ] Redactar política de privacidad y aviso legal.
- [ ] Convertir imágenes a WebP/AVIF y comprimir.
- [ ] Subir `sitemap.xml` a Google Search Console; verificar el dominio.
- [ ] Crear/optimizar Google Business Profile por sede y enlazar a su landing.
- [ ] Revisar Core Web Vitals en PageSpeed (móvil) y corregir si hace falta.
