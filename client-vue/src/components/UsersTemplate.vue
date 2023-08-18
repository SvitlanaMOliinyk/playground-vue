<template>
<div>
<h2>All Users</h2>
    <ul v-if="usersArray">
      <li v-for="(user, index) in usersArray" :key="index">{{ user}}</li>
    </ul>
</div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

interface UserObject {
    userName: string;
}

export default defineComponent({
name: "UsersTemplate",
components: {
  },
  data() {
    return {
      usersArray: [] as UserObject[]
    };
  },
  
    async mounted() {
      try {
        const response: Response = await fetch('http://localhost:5000/users');
        console.log("Response status:", response.status);
        if (!response.ok) {
          throw new Error("Failed to fetch objects");
        }
        const data = await response.json();
        console.log("Data received:", data);
        this.usersArray = data.users_names;
      } catch (error) {
        console.error("Error fetching objects:", error);
        throw error;
      }

    }

})
</script>

<style>

</style>