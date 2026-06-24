# Proyecto: Landings Ocean Clinik La Palma

Contexto para continuar el proyecto desde cualquier Claude Code. Lee esto entero antes de empezar.

## Qué es
5 landing pages en HTML+CSS (un único archivo cada una, sin frameworks), responsive, para
captar pacientes de **Ocean Clinik La Palma** (clínica dental y medicina estética).

- `index.html` — índice/preview que enlaza las 5 (solo para enseñar; lleva `noindex`)
- `01-landing-captacion.html` — captación de leads (formulario de valoración)
- `02-landing-aplicacion.html` — aplicación para tratamientos high-ticket (cualificación)
- `03-landing-llamada.html` — reservar llamada (hueco para embed Calendly/GHL)
- `04-pagina-ventas-vsl.html` — página de ventas tipo VSL (hueco para vídeo)
- `05-quiz-funnel.html` — quiz de 6 preguntas que segmenta y captura nombre/tel/email
- `assets/` — NO separar de los HTML (rutas relativas `assets/...`)
  - `logo-color.png` (sobre claro), `logo-white.png` (sobre oscuro)
  - `sea-light.jpg`, `sea-dark.jpg` (fondos de mar de marca)
  - `fotos/` (sonrisa, clinica, doctor, diagnostico, tratamiento, ortodoncia, facial)

## Marca (NO cambiar sin permiso)
- Colores: azul `#273B88`, azul cielo `#37ABDD`, navy `#0e1f33`, fondo `#F5FAFC`, texto `#1F2933`.
- Tipografía web: **Source Sans 3** (Google Fonts). El logo original usa Optima.
- Marca = **Ocean Clinik** es la protagonista. El doctor se nombra solo en puntos clave.
- Doctor: **Dr. Claudio Vázquez** (dirección clínica) "y su equipo". Nombre completo siempre.
- Sede: Avda. El Puente 41, 38700 Santa Cruz de La Palma.

## Reglas de estilo (importantes)
- **Sin emoticonos.** Los iconos son un sprite SVG inline (`.ico` + `<use href="#ic-...">`). Si añades
  un icono nuevo, define su `<symbol>` en el sprite de ESE archivo (cada HTML tiene su propio sprite).
- Tono **sanitario y prudente**: nada de "el mejor", "resultado garantizado", "sin dolor asegurado".
  Usar "valoración personalizada", "según diagnóstico", "plan adaptado a tu caso".
- Copy con gancho directo (estilo Isra Bravo) pero honesto, sin promesas absolutas.

## Pendiente de personalizar (buscar y reemplazar en los 5 HTML)
1. WhatsApp: cambiar `wa.me/34600000000` por el número real (botón flotante verde en todas).
2. Reseñas Google: cambiar `https://g.page/r/CAMBIAR-POR-TU-ENLACE-GOOGLE` por el enlace real.
3. Foto/bio del Dr. Claudio Vázquez: sustituir `assets/fotos/foto-doctor.jpg` (ahora es stock) por la real.
4. Calendario (03): pegar embed de Calendly/GHL en el bloque `.cal-embed`.
5. Vídeo (04 VSL): sustituir la imagen del bloque `.vsl` por el reproductor (YouTube/Vimeo).
6. Formularios: ahora solo muestran confirmación visual. Conectar a CRM/GHL (en el quiz, el objeto
   `lead` está listo en `showResult()` con un `console.log`).
7. Reseñas reales: añadir testimonios de pacientes en los bloques marcados.

## Hosting / despliegue
- **GitHub repo (fuente única):** https://github.com/JSD1984/ocean-clinik-landings (público)
- **GitHub Pages (web en vivo):** https://jsd1984.github.io/ocean-clinik-landings/ (se actualiza solo al hacer `git push`)
- **Vercel:** https://ocean-clinik-landings.vercel.app
  - Para redeploy manual en Vercel: `vercel --prod` (requiere `vercel login`).
  - Recomendado: conectar el repo de GitHub a Vercel (Settings → Git) para auto-deploy en cada push.

## Flujo de trabajo
1. Editar el/los HTML.
2. `git add -A && git commit -m "..." && git push`  → GitHub Pages se actualiza solo.
3. (Si Vercel NO está conectado al repo) `vercel --prod` para actualizar Vercel.

## Historial de decisiones (resumen)
- Diseño claro/aireado inspirado en dentalclinicbarcelona.es, con paleta y logo reales de Ocean Clinik.
- Se quitaron todos los emojis y se reemplazaron por iconos SVG.
- Se añadieron fotos reales, fondo de mar, sección/tarjetas del Dr. Claudio Vázquez, WhatsApp flotante
  y enlaces a reseñas de Google.
