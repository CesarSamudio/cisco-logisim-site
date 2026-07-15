import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://CesarSamudio.github.io',
  base: '/cisco-logisim-site',
  output: 'static',
  server: { port: 4321, host: true },
});
