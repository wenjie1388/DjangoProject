import { createPinia } from 'pinia';

const store = createPinia();

// 全局挂载store
export function setupStore(app) {
  app.use(store);
}

export { store };
