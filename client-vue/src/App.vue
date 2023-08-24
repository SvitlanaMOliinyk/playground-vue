<template>
  <div>
    <div
      class="navbar bg-dark border-bottom border-body justify-content-around"
      data-bs-theme="dark"
    >
      <router-link to="/" class="btn btn-outline-light">Home Page</router-link>
      <router-link v-if="!isLoggedIn" to="/register" class="btn btn-outline-light"
        >Register</router-link
      >
      <router-link to="/login" class="btn btn-outline-light"
        >Log in</router-link
      >
      <button v-if="isLoggedIn" class="btn btn-outline-light" @click="handleClick">Log out</button>
      <router-link v-if="isLoggedIn" to="/favorites" class="btn btn-outline-light"
        >Favorite places</router-link
      >
    </div>
    <router-view />
  </div>
</template>

<script lang="ts">
import { computed } from 'vue';
import { useStore } from 'vuex';

export default {
  setup() {
    const store = useStore();
    const isLoggedIn = computed(() => store.state.isLoggedIn);

    const handleClick = async () => {
      store.dispatch('logout')
    }

    return {
      isLoggedIn,
      handleClick
    };
  },
};
</script>

<style></style>
