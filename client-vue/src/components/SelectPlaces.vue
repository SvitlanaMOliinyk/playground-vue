<template>
  <div>
    <select id="places" class="forms" @change="handleChange">
      <option v-for="(place, i) in places" :key="i" :value="place">
        {{ place }}
      </option>
    </select>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "SelectPlaces",
  props: {
    position: {
      type: Object as () => { latitude: number; longitude: number },
      required: true,
    },
  },

  data() {
    return {
      places: ["playground", "park", "museum"],
    };
  },
  components: {},
  methods: {
    handleChange(e: MouseEvent) {
      const target = e.target as HTMLSelectElement;
      if (target) {
        console.log(target.value);

        const place = target.value;
        const { latitude, longitude } = this.position;
        const url = `http://localhost:5000/selected?query=${place}&lat=${latitude}&lon=${longitude}`;
        console.log("URL", url);
        this.handleFetch(url);
      }
    },

    async handleFetch(
      url: string
    ): Promise<{ latitude: number; longitude: number }[]> {
      try {
        console.log("Fetching data from:", url);
        const response: Response = await fetch(url);
        console.log("Response status:", response.status);
        if (!response.ok) {
          throw new Error("Failed to fetch objects");
        }
        const data = await response.json();
        console.log("Data received:", data);
        const coordinates = data.coordinates.map(
          (item: { lat: number; lon: number; name: string }) => ({
            referencePosition: { latitude: item.lat, longitude: item.lon },
            name: item.name
          })
        );
        console.log("Coordinates:", coordinates);
        this.$emit("response-updated", coordinates);
        return coordinates;
      } catch (error) {
        console.error("Error fetching objects:", error);
        throw error;
      }
    },
  },
});
</script>

<style></style>
