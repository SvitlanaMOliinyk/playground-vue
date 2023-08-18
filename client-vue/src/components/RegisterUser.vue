<template>
  <div class="container d-grid gap-3">
    <form id="register-form" class="mb-3 mt-4" @submit.prevent>
      <label for="name" class="form-label fw-bold">User Name</label>
      <input
        type="text"
        class="form-control mb-3"
        id="name"
        v-model="userName"
      />
      <label for="password" class="form-label fw-bold">Password</label>
      <input
        type="password"
        id="password"
        v-model="password"
        class="form-control"
        aria-describedby="passwordHelpBlock"
      />
      <div id="passwordHelpBlock" class="form-text mb-3">
        Your password must be 8-20 characters long, contain letters and numbers,
        and must not contain spaces, special characters, or emoji.
      </div>
      <label for="email" class="form-label fw-bold">Email address</label>
      <input
        type="email"
        class="form-control"
        id="email"
        v-model="email"
        placeholder="name@example.com"
      />
    </form>
    <button
      type="submit"
      form="register-form"
      class="btn btn-secondary"
      @click="handleClick"
    >
      Sign in
    </button>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import router from "../router";
export default defineComponent({
  name: "RegisterUser",
  setup() {
    const userName = ref("Enter your name");
    const password = ref("");
    const email = ref("");

    const handleClick = async () => {
      try {
        const response = await fetch("http://localhost:5000/register", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            name: userName.value,
            password: password.value,
            email: email.value,
          }),
          credentials: "include",
        });
        console.log("Response:", response);
        if (!response.ok) {
          throw new Error("Failed to register user");
        }
        const data = await response.json();
        if (data) {
          router.push({ path: "/" });
        }
      } catch (error) {
        console.error("Error posting objects:", error);
        throw error;
      }
    };

    return {
      userName,
      password,
      email,
      handleClick,
    };
  },
});
</script>

<style></style>
