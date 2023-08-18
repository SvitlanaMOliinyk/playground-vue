import { createRouter, createWebHashHistory } from "vue-router";
import HomePage from "../components/HomePage.vue";
import RegisterUser from "../components/RegisterUser.vue";
import MyFavorites from "../components/MyFavorites.vue";
import UsersTemplate from "../components/UsersTemplate.vue";

const routes = [
  { path: "/", component: HomePage },
  { path: "/register", component: RegisterUser },
  { path: "/favorites", component: MyFavorites },
  { path: "/users", component: UsersTemplate },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
