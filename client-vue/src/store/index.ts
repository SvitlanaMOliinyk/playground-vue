import { createStore } from "vuex";

const store = createStore({
  state: {
    user: null,
    isLoggedIn: false,
  },
  mutations: {
    setUser(state, payload) {
      state.user = payload;
      console.log("user state changed:", state.user);
    },
    setLoggedIn(state, value) {
      state.isLoggedIn = value;
    },
  },
  actions: {
    async register (context, { name, password, email }) {
      const response = await fetch("http://localhost:5000/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: name,
          password: password,
          email: email,
        }),
        credentials: "include",
      });
      console.log("Response:", response);
      if (!response.ok) {
        throw new Error("Failed to register user");
      }
      const data = await response.json();
      if (data) {
        context.commit("setUser", data);
        context.commit("setLoggedIn", true);
      } else {
        throw new Error("login is failed");
      }
    },

    async login(context, { password, email }) {
      const response = await fetch("http://localhost:5000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          password: password,
          email: email,
        }),
        credentials: "include",
      });
      console.log("Response:", response);
      if (!response.ok) {
        throw new Error("Failed to login user");
      }
      const data = await response.json();
      if (data) {
        context.commit("setUser", data);
        context.commit("setLoggedIn", true);
      } else {
        throw new Error("login is failed");
      }
    },
    async logout(context){
      const response = await fetch("http://localhost:5000/logout", {
        method: "POST",
        credentials: "include",
      });
      if (!response.ok) {
        throw new Error("Failed to logout user");
      } else {
        context.commit("setUser", null);
        context.commit("setLoggedIn", false);
      }
    }
  },
});

export default store;
