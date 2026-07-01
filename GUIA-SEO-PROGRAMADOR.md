# Guía para el programador — Ocean Clinik (Abades + La Palma)

**8 landing pages SEO locales** (4 temas × 2 sedes), estáticas (**HTML + CSS**, sin frameworks), responsive (mobile-first).
Todo el contenido y los datos reales ya están puestos. Tu trabajo: revisarlas, hacer 2 activaciones, poner el dominio final y subirlas.

Repo: **https://github.com/JSD1984/ocean-clinik-landings** · Demo: **https://ocean-clinik-landings.vercel.app**

---

## 1. Estructura de archivos (todo va incluido en el repo, imágenes también)

```
/index.html                      ← índice de previsualización (NO subir a producción, o ponle noindex)
/landings.css                    ← estilos compartidos por todas las páginas
/sitemap.xml  /robots.txt
/assets/                         ← logos + /assets/fotos/ (fotos). NO separar de los HTML
/seo-build/generate.py           ← generador: TODO el contenido y los datos viven aquí
/GUIA-SEO-PROGRAMADOR.md

# Sede Abades (Tenerife Sur)
/clinica-dental-tenerife-sur/index.html
/implantes-dentales-tenerife-sur/index.html
/ortodoncia-invisible-tenerife-sur/index.html
/odontopediatria-tenerife-sur/index.html      ← Ocean Kids
# Sede La Palma
/clinica-dental-la-palma/index.html
/implantes-dentales-la-palma/index.html
/ortodoncia-invisible-la-palma/index.html
/odontopediatria-la-palma/index.html          ← Ocean Kids
/politica-privacidad/index.html  /aviso-legal/index.html
```

| Tema | Abades (Tenerife Sur) | La Palma |
|---|---|---|
| Clínica dental | `/clinica-dental-tenerife-sur/` | `/clinica-dental-la-palma/` |
| Implantes + casos complejos (Khoury, cigomáticos, subperiósticos) | `/implantes-dentales-tenerife-sur/` | `/implantes-dentales-la-palma/` |
| Ortodoncia invisible | `/ortodoncia-invisible-tenerife-sur/` | `/ortodoncia-invisible-la-palma/` |
| Odontopediatría · Ocean Kids | `/odontopediatria-tenerife-sur/` | `/odontopediatria-la-palma/` |

---

## 2. CÓMO DESPLEGAR (importante)

- **Servir desde la RAÍZ del dominio.** Las páginas usan rutas **absolutas** (`/landings.css`, `/assets/...`).
  En subcarpeta no cargarán estilos ni imágenes (o cambia las rutas / usa `<base>`).
- Cada slug es una **carpeta con `index.html`** → URLs limpias. El servidor debe servir `index.html` por defecto.
- Es **100% estático**: cualquier hosting (Apache/Nginx/CDN/Vercel). No necesita Node ni build en el server.
- HTTPS obligatorio. Caché larga en `/assets/`, compresión gzip/brotli. Convertir fotos a WebP/AVIF (Core Web Vitals).

---

## 3. Datos reales por sede (YA puestos)

**Abades (Tenerife Sur)** — email `info@theoceanclinik.com`
- Teléfono **922 41 71 95** · WhatsApp **+34 624 50 65 03**
- Dirección: **C. 16 de Mayo, C.C. Abades, Local 5 · 38588 Abades (Arico)**
- Horario: **Lun–Vie 10:00–14:00 y 15:00–19:00 · Sáb 10:00–14:00 · Dom cerrado**
- Google (reseñas + schema): **https://share.google/ND29C2uiRdIEbzk7M**

**La Palma** — email `lapalma@theoceanclinik.com`
- Teléfono/fijo **922 41 13 23** · WhatsApp **+34 626 09 41 10**
- Dirección: **Av. El Puente 41, Bajo, Local 9 · 38700 Santa Cruz de La Palma**
- Horario: **Lun 11:00–19:00 · Mar–Vie 9:00–19:00 · Sáb 10:00–14:00 · Dom cerrado**
- Google (reseñas + schema): **https://share.google/ZxzG4VIILkrBaGKI0**

> Todo esto vive en `CITIES` (dentro de `seo-build/generate.py`). Cada sede tiene su `tel`, `wa`, `email`, `addr`, `hours`, `reviews`. Se muestra en hero, footer, formulario y JSON-LD.

---

## 4. Formularios → email (IMPORTANTE: 2 activaciones)

Cada formulario **envía el lead por email** con **FormSubmit** (funciona en hosting estático, sin backend):
- Páginas de **Abades** → `info@theoceanclinik.com`
- Páginas de **La Palma** → `lapalma@theoceanclinik.com`
- Incluye validación, mensaje de confirmación y un campo `Origen` (tema · sede) para saber de dónde viene el lead.

⚠️ **FormSubmit pide activar cada email UNA vez.** Haz un envío de prueba desde una página de cada sede y pulsa el enlace de activación que llega a ese correo. Hasta activarlo, los leads no se reenvían.

> Si prefieres tu propio backend/SMTP, cambia `action` y `data-endpoint` del `<form id="lead-form">`. El resto (validación, confirmación, eventos) ya funciona.

---

## 5. Reseñas de Google (por sede)

- El botón **"Ver reseñas en Google"** y el `schema` (`sameAs`) de cada página ya apuntan a **la ficha de su sede** (ver punto 3).
- **Opcional (recomendado):** widget de reseñas EN VIVO por sede (Trustindex / Elfsight / EmbedSocial). Sustituye el bloque `.rw-ph` de cada página por el embed conectado a la ficha correspondiente. Mostrar mínimo 6 reseñas.

---

## 6. SEO técnico que YA viene hecho (no romper)

- 1 `<h1>` por página con keyword · jerarquía H2/H3 · HTML semántico.
- `title` y `meta description` únicas · `<link rel="canonical">` · Open Graph.
- **JSON-LD** por página: `Dentist` + `FAQPage` + `BreadcrumbList` (con NAP, horario y `sameAs` de la ficha de Google).
- `sitemap.xml` y `robots.txt` en la raíz. Enlazado interno entre páginas. CTAs `tel:` y WhatsApp. Sticky móvil.
- Imágenes con `width`/`height`; hero con `fetchpriority="high"`. Responsive verificado a 375–390px.

---

## 7. Analítica (eventos ya emitidos a `dataLayer`)

Los formularios y la web ya hacen `dataLayer.push` de: `form_start`, `select_treatment`/`select_child_need`, `select_time_preference`, `form_submit`, `generate_lead`.
Falta: instalar **GA4/GTM** y mapear conversiones (`generate_lead`, `click_whatsapp`, `click_call`). Añadir listeners de click a WhatsApp/tel si se quieren medir.

---

## 8. Regenerar las páginas

Todo el contenido y los datos están en `seo-build/generate.py`. Tras editar:

```bash
python3 seo-build/generate.py
```

Genera las 8 carpetas `/<slug>/index.html`, `sitemap.xml` y `robots.txt`.

---

## 9. PENDIENTE antes de publicar

- [ ] **Activar FormSubmit** en los 2 correos (envío de prueba + clic de activación). ← imprescindible para recibir leads
- [ ] **Dominio final** → poner en `BASE_URL` (ahora `https://www.oceanclinik.es`) y regenerar (afecta canonical, OG, sitemap, schema).
- [ ] Subir a la **raíz** del dominio con **HTTPS**.
- [ ] Enviar `sitemap.xml` a **Google Search Console**.
- [ ] **GA4/GTM** y conversiones.
- [ ] *(Opcional)* Widget de reseñas en vivo por sede · **fotos reales** (implantología, equipo, niños/familia Ocean Kids, fachada La Palma) en WebP · redactar **política de privacidad** y **aviso legal** (ahora son plantilla).
- [ ] Revisar **Core Web Vitals** en PageSpeed (móvil).

---

## 10. SEO local (lo que más mueve el ranking, gestión de la clínica)

- **Google Business Profile** de cada sede completo y verificado (categoría, horarios, fotos, enlace a la web).
- Pedir **reseñas** de forma sistemática y responderlas · **NAP idéntico** en web, Google y directorios.
