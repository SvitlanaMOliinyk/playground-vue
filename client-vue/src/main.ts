import { createApp } from "vue";
import App from "./App.vue";
import "./assets/global.css";
import router from "./router";
import store from "./store/index";

store.dispatch('checkAuthStatus');

createApp(App).use(router).use(store).mount("#app");
