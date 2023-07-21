<template>
  <div id="mapContainer" style="width: 100%; height: 400px"></div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import L from 'leaflet';

interface ResponseObject {
  name: string;
  referencePosition: {
    latitude: number;
    longitude: number;
  };
}

export default defineComponent({
  name: "MapRender",
  props: {
    position: {
      type: Object as () => { latitude: number; longitude: number },
      required: true,
    },
    markers: {
      type: Array as () => ResponseObject[],
      required: true,
    },
  },
  mounted() {
    this.renderMap();
  },
  methods: {
    renderMap() {
      const map = L.map("mapContainer").setView(
        [this.position.latitude, this.position.longitude],
        13
      );
       console.log("RenderMap component")

      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: "Map data &copy; OpenStreetMap contributors",
        maxZoom: 18,
      }).addTo(map);

      this.markers.forEach((marker: ResponseObject) => {
         const { latitude, longitude } = marker.referencePosition;
        const markerPopupContent = `<b>${marker.name}</b>`;
        L.marker([latitude, longitude])
          .addTo(map)
          .bindPopup(markerPopupContent);
      });
    },
  },
});
</script>

<style>
</style>
