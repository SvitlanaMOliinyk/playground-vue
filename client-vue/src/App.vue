<template>
  <div>
    <div
      class="navbar bg-dark border-bottom border-body justify-content-around"
      data-bs-theme="dark"
    >
      <router-link to="/" class="btn btn-outline-light">Home Page</router-link>
      <router-link to="/register" class="btn btn-outline-light"
        >Register</router-link
      >
      <router-link to="/favorites" class="btn btn-outline-light"
        >Favorite places</router-link
      >
    </div>
    <router-view />
  </div>
</template>

<style></style>
