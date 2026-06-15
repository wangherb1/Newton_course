// @ts-check
import { defineConfig } from 'astro/config';

import react from '@astrojs/react';
import mdx from '@astrojs/mdx';

// https://astro.build/config
export default defineConfig({
  base: process.env.BASE_PATH || '/',
  site: process.env.SITE || undefined,
  integrations: [react(), mdx()]
});
