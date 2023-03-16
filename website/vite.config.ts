import vue from '@vitejs/plugin-vue'
import { UserConfig, ConfigEnv, loadEnv } from 'vite';
// import { createSvgIconsPlugin } from 'vite-plugin-svg-icons';
import path from 'path';

// 自动导入 element-plus 组件
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'

// https://vitejs.dev/config/
export default ({ mode }: ConfigEnv): UserConfig => {
  // 获取 .env 环境配置文件
  const env = loadEnv(mode, process.cwd());

  return {
    plugins: [
      vue(),
      AutoImport({
        resolvers: [ElementPlusResolver()],
      }),
      Components({
        resolvers: [ElementPlusResolver()],
      }),
    ],
    resolve: {
      alias: {
        '@': path.resolve('./src')
      }
    },
  
    server: {
      proxy: {
        '/api': {
          // 线上API地址
          // target: 'http://vapi.youlai.tech',
          // 本地API地址
          target: 'http://localhost:8989',
          changeOrigin: true,
          rewrite: path =>
            path.replace(new RegExp('^' + env.VITE_APP_BASE_API), '')
        }
      }
    },
  }

}
