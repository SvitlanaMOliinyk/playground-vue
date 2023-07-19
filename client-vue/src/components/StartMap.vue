<template>
  <div id="map">
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import L, { LatLng } from 'leaflet';

export default defineComponent({
  name: "StartMap",
  components: {
  },
  data() {
    return {
    };
  },
  methods: {
    
    initializeMap() {
      // Initialize the map
      const map = L.map('map').setView([0, 0], 13);

      // Create a Tile Layer for the map and assign it to the tileLayer variable
      const tileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors'
      });

      // Add the tile layer to the map
      tileLayer.addTo(map);

      // Get the user's current location using the Geolocation API
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            const { latitude, longitude } = position.coords;

            // Create a marker at the user's location
            const marker = L.marker([latitude, longitude]).addTo(map);

            // Update the map view to the user's location
            map.setView(new LatLng(latitude, longitude), 13);
             this.$emit("position-updated", { latitude, longitude });
          },
          (error) => {
            console.error('Error retrieving location:', error);
          }
        );
      } else {
        console.error('Geolocation is not supported by this browser');
      }
    },
  },
  mounted() {
    this.initializeMap();
  },
});
</script>
