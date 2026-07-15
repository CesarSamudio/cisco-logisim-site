# Guía de imágenes — Dónde va cada foto

Esta lista mapea **cada placeholder `IMG`** del sitio con la imagen que debe ir ahí.
Usa esta guía cuando tengas las capturas listas.

## 📂 Convención de nombres sugerida

```
public/images/
├── cisco/
│   ├── hero.jpg                 # 21:9 - pantalla completa del simulador
│   ├── interface.jpg            # 4:3 - menú principal
│   ├── paso-1-descarga.jpg      # 16:9 - paso 1 descarga
│   ├── paso-2-extraccion.jpg    # 16:9
│   ├── paso-3-ruffle.jpg        # 16:9
│   ├── paso-4-primer-launch.jpg # 16:9
│   ├── gal-01-pantalla.jpg      # 4:3 - galería manual
│   ├── gal-02-motherboard.jpg   # 4:3
│   ├── gal-03-cpu.jpg           # 4:3
│   ├── gal-04-pasta.jpg         # 4:3
│   ├── gal-05-ram.jpg           # 4:3
│   ├── gal-06-disco.jpg         # 4:3
│   ├── gal-07-fuente.jpg        # 4:3
│   └── gal-08-completo.jpg      # 4:3
├── logisim/
│   ├── hero.jpg
│   ├── canvas.jpg
│   ├── paso-1-plataforma.jpg
│   ├── paso-2-instala.jpg
│   ├── paso-3-java.jpg
│   ├── paso-4-primer.jpg
│   ├── gal-01-new.jpg
│   ├── gal-02-panel.jpg
│   ├── gal-03-input.jpg
│   ├── gal-04-and.jpg
│   ├── gal-05-cable.jpg
│   ├── gal-06-toggle.jpg
│   ├── gal-07-led.jpg
│   └── gal-08-cronograma.jpg
└── equipo.jpg                   # 4:3 - foto/logo equipo (portada)
```

## 🗺️ Mapa de placeholders por página

### `src/pages/index.astro` (Portada)

| Línea aprox | Label del placeholder | Imagen a colocar |
|---|---|---|
| ~80 | `IMG - captura` (en card Cisco IT) | Captura del simulador Cisco IT |
| ~80 | `IMG - captura` (en card Logisim) | Captura de Logisim |
| ~110 | `IMG - equipo` | Foto o logo del equipo (variante purple) |

### `src/pages/cisco-it.astro`

| Sección | Label | Imagen |
|---|---|---|
| Hero | `IMG - hero Cisco IT` | Captura de pantalla completa (21:9) |
| Introducción | `IMG - interfaz` | Vista del menú principal |
| Instalación | `IMG - paso 1` a `IMG - paso 4` | Capturas de cada paso |
| Manual | `IMG - Pantalla principal` a `IMG - Ensamblaje completo` | 8 capturas del proceso |
| Videos | `VIDEO 1`, `VIDEO 2`, `VIDEO 3` (variante purple) | Screenshots/thumbnails de videos |

### `src/pages/logisim.astro`

| Sección | Label | Imagen |
|---|---|---|
| Hero | `IMG - hero Logisim` | Captura de pantalla con circuito AND |
| Introducción | `IMG - canvas principal` | Canvas vacío al iniciar |
| Instalación | `IMG - paso 1` a `IMG - paso 4` | Capturas de cada paso |
| Manual | `IMG - File New` a `IMG - Cronograma` | 8 capturas construyendo circuito |
| Videos | `VIDEO 1`, `VIDEO 2`, `VIDEO 3` (variante purple) | Screenshots/thumbnails de videos |

## 🔧 Cómo reemplazar un placeholder

Edita el archivo `.astro` correspondiente. Busca el `<ImgPlaceholder label="..." />` y reemplázalo por:

```astro
<img
  src="/images/cisco/paso-1.jpg"
  alt="Paso 1: descarga segura del simulador"
  style="width: 100%; aspect-ratio: 16/9; object-fit: cover; border-radius: 16px;"
/>
```

Para videos, reemplaza por:

```astro
<video controls style="width: 100%; aspect-ratio: 16/9; border-radius: 16px;">
  <source src="/videos/instalacion.mp4" type="video/mp4" />
</video>
```

## 💡 Tips de captura

- **Cisco IT**: capturas a 1920×1080 o superior. Asegúrate de que se vean las acciones (drag & drop, hover).
- **Logisim**: capturas con componentes visibles. Usa "View → Zoom to Fit" antes de capturar.
- **Videos**: graba en 1080p mínimo. Audio opcional. Sube el `.mp4` a `public/videos/`.