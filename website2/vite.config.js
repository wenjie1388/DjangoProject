import { fileURLToPath, URL } from 'node:url'
import path from 'path';

// import { resolve } from 'path';

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    AutoImport({
      resolvers: [ElementPlusResolver()],
    }),
    Components({
      resolvers: [ElementPlusResolver()],
    }),
  ],
  server: {
    proxy: {
      '/api/v1': {
        // target: process.env.VUE_APP_Proxy_url,
        target: 'http://127.0.0.1:8000/',
        changeOrigin: true,
        // rewrite: path => path.replace(/^\/api/, '1')
      },
    }
  },
  // resolve: {
  //   // Vite路径别名配置
  //   alias: {
  //       '@': path.resolve('D:/blog/ui/src')
  //       // @': path.resolve('./src')
  //   }
  // }
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
