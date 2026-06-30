# Guía para el programador — Ocean Clinik Tenerife Sur (Abades)

5 landing pages SEO locales, estáticas (**HTML + CSS**, sin frameworks), responsive (mobile-first).
Tu trabajo: revisarlas, completar lo pendiente y subirlas al servidor.

---

## 1. Qué es y estructura de archivos

```
/index.html                      ← índice de previsualización (NO subir a producción, o ponle noindex)
/landings.css                    ← estilos compartidos por las 5 páginas
/sitemap.xml  /robots.txt
/assets/                         ← logos, fondos e imágenes (NO separar de los HTML)
/seo-build/generate.py           ← generador: todo el contenido vive aquí
/GUIA-SEO-PROGRAMADOR.md

/dentista-tenerife-sur/index.html
/clinica-dental-tenerife-sur/index.html
/implantes-dentales-tenerife-sur/index.html
/ortodoncia-invisible-tenerife-sur/index.html
/carillas-dentales-tenerife/index.html
/politica-privacidad/index.html  /aviso-legal/index.html
```

Keyword → URL (1 keyword = 1 URL = 1 H1):

| Keyword | URL |
|---|---|
| dentista Tenerife Sur | `/dentista-tenerife-sur/` |
| clínica dental Tenerife Sur | `/clinica-dental-tenerife-sur/` |
| implantes dentales Tenerife Sur | `/implantes-dentales-tenerife-sur/` |
| ortodoncia invisible Tenerife Sur | `/ortodoncia-invisible-tenerife-sur/` |
| carillas dentales Tenerife | `/carillas-dentales-tenerife/` |

---

## 2. CÓMO DESPLEGAR (importante)

- **Servir desde la RAÍZ del dominio.** Las páginas usan rutas **absolutas** (`/landings.css`, `/assets/...`).
  Si lo cuelgas en un subdirectorio, no cargarán estilos ni imágenes. Si tiene que ir en subcarpeta,
  cambia esas rutas a relativas o ajusta el `<base>`.
- Cada slug es una **carpeta con `index.html`** → URLs limpias (`/dentista-tenerife-sur/`).
  Asegúrate de que el servidor sirve `index.html` por defecto en cada carpeta.
- Es **estático**: sirve con cualquier hosting (Apache/Nginx/CDN). No necesita Node ni build en el server.
- HTTPS obligatorio. Caché larga en `/assets/` y compresión gzip/brotli.

---

## 3. Datos reales YA puestos (sede de Abades)

- Teléfono: **922 41 71 95** · WhatsApp: **+34 624 50 65 03**
- Dirección: **C. 16 de Mayo, C.C. Abades, Local 5 · 38588 Abades (Arico), Santa Cruz de Tenerife**
- Horario: **Lun–Vie 10:00–14:00 y 15:00–19:00 · Sáb 10:00–14:00 · Dom cerrado** (en hero, footer y schema)

---

## 4. PENDIENTE de configurar (antes de publicar)

Todo lo editable está en `seo-build/generate.py` (bloque `CONFIG`). Edita y **regenera** (`python3 seo-build/generate.py`),
o edita a mano en los HTML.

1. **Dominio final** → variable `BASE_URL` (ahora `https://www.oceanclinik.es`). Afecta a canonical, Open Graph, sitemap y schema.
2. **Reseñas de Google**:
   - `REVIEWS` → enlace real de la ficha de Google.
   - Widget en vivo (recomendado): crear en **Trustindex** o **Elfsight** ("Google Reviews"), conectar la ficha y
     pegar el `<script>` donde está el bloque `.reviews-widget` (marcado en el HTML/plantilla). Lleva cookies → añadir aviso de cookies.
3. **Email** de contacto → `EMAIL` (ahora `info@theoceanclinik.com`, confirmar).
4. **Cifras del hero** (`4,9`, `+15 años`, `+5.000 pacientes`) → poner las reales o quitarlas (están en la plantilla).
5. **Formularios**: ahora solo muestran confirmación visual. Conectar a CRM/agenda. Consentimiento RGPD
   (casilla desmarcada, info por capas — ya está enlazada a la política).
6. **Legales**: redactar `política de privacidad` y `aviso legal` (ahora son plantilla).
7. Convertir imágenes de `/assets/` a **WebP/AVIF** y comprimir (Core Web Vitals).

---

## 5. SEO técnico que YA viene hecho (no romper)

- 1 solo `<h1>` por página con keyword · jerarquía H2/H3 · HTML semántico.
- `title` y `meta description` únicas · `<link rel="canonical">` absoluto · Open Graph.
- **Schema JSON-LD** por página: `Dentist` + `FAQPage` + `BreadcrumbList`.
- `sitemap.xml` y `robots.txt` en la raíz (regenerar si cambia el dominio).
- Imágenes con `width`/`height` (evita CLS); hero con `fetchpriority="high"`.
- Enlazado interno entre las páginas (sección "Otros tratamientos" + footer).
- CTA `tel:` y WhatsApp · barra fija "Llamar / Pedir cita" en móvil.
- Responsive verificado en móvil (375px).

---

## 6. Regenerar las páginas

Todo el contenido (textos, tarjetas, FAQ, CONFIG) está en `seo-build/generate.py`. Tras editar:

```bash
python3 seo-build/generate.py
```

Genera las 5 carpetas `/<slug>/index.html`, `sitemap.xml` y `robots.txt`.

---

## 7. SEO local (lo que más mueve el ranking)

- **Google Business Profile** de Abades completo y verificado (categoría correcta, horarios, fotos, enlace a la web).
- Pedir **reseñas** de forma sistemática y responderlas.
- **NAP idéntico** en web, Google y directorios.

---

## 8. Checklist de publicación

- [ ] Poner `BASE_URL` con el dominio real y regenerar.
- [ ] Enlace/widget de reseñas de Google + email real.
- [ ] Decidir cifras del hero (reales o quitar).
- [ ] Conectar formularios al CRM/agenda (+ consentimiento).
- [ ] Redactar política de privacidad y aviso legal.
- [ ] Imágenes a WebP/AVIF.
- [ ] Subir a la **raíz** del dominio con HTTPS.
- [ ] Enviar `sitemap.xml` a Google Search Console.
- [ ] Revisar Core Web Vitals en PageSpeed (móvil).
