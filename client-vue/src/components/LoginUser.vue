<template>
  <div class="container d-grid gap-3">
    <form id="login-form" class="mb-3 mt-4" @submit.prevent>
      <label for="email" class="form-label fw-bold">Email</label>
      <input
        type="email"
        class="form-control mb-3"
        id="email"
        v-model="email"
        placeholder="name@example.com"
      />
      <label for="password" class="form-label fw-bold">Password</label>
      <input
        type="password"
        id="password"
        v-model="password"
        class="form-control"
        aria-describedby="passwordHelpBlock"
      />
    </form>
    <button
      type="submit"
      form="login-form"
      class="btn btn-secondary"
      @click="handleClick"
    >
      Log in
    </button>
    <div v-if="error">{{error}}</div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import router from "../router";
import { useStore } from "vuex";
export default defineComponent({
  name: "LoginUser",
  setup() {
    const password = ref("");
    const email = ref("");
    const error = ref(null);
    const store = useStore();

    const handleClick = async () => {
      try {
        await store.dispatch("login", {
          password: password.value,
          email: email.value,
        });
        router.push({ path: "/" });
      } catch (err: any) {
        error.value = err.message;
      }
    };

    return {
      password,
      email,
      handleClick,
      error
    };
  },
});
</script>

<style></style>
