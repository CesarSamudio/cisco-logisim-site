# Cisco IT · Logisim — Sitio de Investigación

Sitio web educativo construido con **Astro** y diseño inspirado en **Fly.io**, que documenta las dos aplicaciones asignadas en el Tema #1:

1. **Cisco IT Essentials Virtual Desktop** — simulador de ensamblaje de PC (basado en Flash/ActionScript, hoy con Ruffle).
2. **Logisim Evolution** — simulador open source de circuitos lógicos digitales en Java.

## 🚀 Inicio rápido

```bash
# Instalar dependencias (solo la primera vez)
npm install

# Servidor de desarrollo (hot-reload en http://localhost:4321)
npm run dev

# Build de producción (genera carpeta dist/)
npm run build

# Preview del build
npm run preview
```

## 📁 Estructura del proyecto

```
cisco-logisim-site/
├── astro.config.mjs            # Configuración Astro (output: static)
├── package.json
├── public/
│   └── favicon.svg             # Ícono del sitio
└── src/
    ├── layouts/
    │   └── BaseLayout.astro    # HTML shell (Nav + Footer + fuentes)
    ├── components/
    │   ├── Nav.astro           # Barra de navegación con logo + nav pill
    │   ├── Footer.astro        # Footer oscuro multi-columna
    │   ├── Button.astro        # Botón pill (variants: primary, outline, ghost)
    │   ├── ImgPlaceholder.astro  # Caja "IMG" con borde dashed púrpura
    │   ├── SectionHero.astro
    │   ├── SectionFeatureGrid.astro
    │   ├── SectionEnterprise.astro
    │   ├── SectionPurple.astro
    │   ├── SectionSteps.astro
    │   └── SectionGallery.astro
    ├── pages/
    │   ├── index.astro         # Portada
    │   ├── cisco-it.astro      # App 1 — 6 secciones requeridas
    │   └── logisim.astro       # App 2 — 6 secciones requeridas
    └── styles/
        ├── tokens.css          # Variables CSS (colores, fuentes, spacing)
        └── global.css          # Reset + base + utilidades
```

## 🎨 Sistema de diseño

Estilo **Fly.io adaptado a tema educativo**:

| Token | Valor | Uso |
|---|---|---|
| Acento | `#7c5dfa` | Botones, acentos |
| Acento profundo | `#6332f6` | Bloques púrpura |
| Fondo | `#f9f9fb` | Background principal |
| Display | Fraunces (serif italic) | Títulos H1/H2 |
| Body | Inter (sans-serif) | Texto, UI |
| Forma | Pill (999px), cards 16px | Botones y tarjetas |

Las fuentes se cargan desde Google Fonts en `BaseLayout.astro`. Si necesitas servirlas offline, descarga los `.woff2` y reemplaza el `<link>`.

## 🖼️ Reemplazar placeholders por imágenes reales

Cada `<ImgPlaceholder label="..." />` es un cuadrado con texto que indica dónde va una imagen. Cuando tengas las imágenes:

### Opción A: Sustitución directa (rápida)

1. Sube tus imágenes a `public/images/` (por ejemplo, `public/images/cisco/paso-1.jpg`)
2. Reemplaza en el archivo `.astro` correspondiente:
   ```astro
   <!-- Antes -->
   <ImgPlaceholder label="IMG - paso 1" sublabel="Descarga segura" ratio="16/9" />

   <!-- Después -->
   <img src="/images/cisco/paso-1.jpg" alt="Paso 1: descarga segura del simulador" style="width: 100%; aspect-ratio: 16/9; object-fit: cover; border-radius: 16px;" />
   ```

### Opción B: Usar `astro:assets` (más avanzado)

Requiere mover las imágenes a `src/assets/` y usar `<Image>` de `astro:assets`. Mejor para optimización automática (WebP, srcset, lazy loading).

## 📐 Cambiar tipografías, colores o espaciado

Todos los tokens viven en **`src/styles/tokens.css`**. Cambia una variable ahí y se propaga a todo el sitio.

```css
:root {
  --color-accent: #7c5dfa;  /* Cambia el color principal aquí */
  --font-display: 'Fraunces', serif;  /* O usa una serif local */
}
```

## 📦 Build y deploy

El build genera archivos estáticos en `dist/`. Puedes desplegar en:

- **Netlify / Vercel**: drag & drop de `dist/` o conectar el repo
- **GitHub Pages**: subir `dist/` a la rama `gh-pages`
- **Hosting tradicional**: subir contenido de `dist/` por FTP
- **Cloudflare Pages**: conectar repo, build command `npm run build`, output `dist`

## ✅ Cobertura de requisitos del profesor

Cada aplicación cubre las **6 secciones obligatorias** (Portada + 6 secciones = 7 total):

| # | Sección | Cisco IT | Logisim |
|---|---|---|---|
| 1 | Portada | ✓ hero section | ✓ hero section |
| 2 | Introducción y Propósito | ✓ Qué es exactamente | ✓ Qué es y para qué sirve |
| 3 | Ventajas y Desventajas | ✓ 3 ventajas + 2 limitaciones | ✓ 3 ventajas + 2 limitaciones |
| 4 | Guía de Descarga e Instalación | ✓ 4 pasos | ✓ 4 pasos + tabla por OS |
| 5 | Requisitos del sistema y licenciamiento | ✓ Tabla + licencia Cisco Academy | ✓ Tabla + GPL v3 |
| 6 | Manual de Funcionamiento | ✓ Galería 8 pasos | ✓ Galería 8 pasos + tips |
| 7 | Videos del equipo | ✓ 3 slots de video | ✓ 3 slots de video |

## 🛠️ Tech stack

- **Astro 7.0.9** — generador estático, default zero-JS
- **CSS puro** con variables CSS (sin Tailwind ni preprocessors)
- **Fraunces** + **Inter** vía Google Fonts
- **Sin frameworks JS** — sitio 100% HTML+CSS, performance óptimo

## 📄 Licencia

Sitio educativo sin licencia específica. Logisim Evolution se distribuye bajo GPL v3; Cisco IT Essentials Virtual Desktop es propiedad de Cisco Networking Academy para uso educativo.