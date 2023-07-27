<template>
  <div className="mapWrapper" @click.self="closeMap">
    <div id="mapContainer" style="width: 100%; height: 400px"></div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import L from "leaflet";

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
      console.log("RenderMap component");

      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: "Map data &copy; OpenStreetMap contributors",
        maxZoom: 18,
      }).addTo(map);

      const userMarkerStyle = L.divIcon({
        className: "user-marker-style",
      });

      const userMarker = L.marker(
        [this.position.latitude, this.position.longitude],
        { icon: userMarkerStyle }
      )
        .addTo(map)
        .bindPopup("Here I am");

      this.markers.forEach((marker: ResponseObject) => {
        const { latitude, longitude } = marker.referencePosition;
        const markerPopupContent = `<b>${marker.name}</b>`;
        L.marker([latitude, longitude])
          .addTo(map)
          .bindPopup(markerPopupContent);
      });
    },
    closeMap() {
      this.$emit("close");
    },
  },
});
</script>

<style>
.mapWrapper {
  max-width: 100%;
  max-height: 80vh;
  padding-top:15vh;
  background-clip: padding-box; 
}

.user-marker-style {
  position: relative;
  background-color: red;
  border-radius: 50%;
  animation: background-animation 3s infinite; /* Animation for the marker background */
}

.user-marker-style::after {
  content: "";
  position: absolute;
  top: -5px;
  left: -5px;
  right: -5px;
  bottom: -5px;
  border: 10px solid orange;
  border-radius: inherit;
  opacity: 0;
  animation: border-animation 3s infinite;
}

@keyframes background-animation {
  0%,
  100% {
    opacity: 1;
  }
  50% {
    opacity: 0.6;
  }
}

@keyframes border-animation {
  0%,
  100% {
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
}
</style>
