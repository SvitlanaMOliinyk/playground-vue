<template>
  <div class="app">
    <button @click="handleClick" class="select-button">Choose location</button>
    <StartMap @position-updated="handlePositionUpdated" />
    <SelectPlaces v-if="isSelected" @response-updated="handleResponseData" :position="position"/>
    <MapRender
      v-if="isSelectedSecond && responseData.length > 0"
      :position="position"
      :markers="responseData"
    />
  </div>
</template>


<script lang="ts">
import { defineComponent } from "vue";
import SelectPlaces from "./components/SelectPlaces.vue";
import StartMap from "./components/StartMap.vue";
import MapRender from "./components/MapRender.vue";

interface ResponseObject {
  referencePosition: {
    latitude: number;
    longitude: number;
  };
  name: string;
}

export default defineComponent({
  name: "App",
  components: {
    SelectPlaces,
    StartMap,
    MapRender,
  },
  data() {
    return {
      isSelected: false,
      isSelectedSecond: false,
      responseData: [] as ResponseObject[],
      position: { latitude: 0, longitude: 0 },
    };
  },
  methods: {
    handleClick() {
      this.isSelected = !this.isSelected;
    },
    handlePositionUpdated(position: { latitude: number; longitude: number }) {
      this.position = position;
      console.log("Position", position)
    },
    handleResponseData(data: ResponseObject[]) {
      this.responseData = data;
      console.log("responseData", this.responseData)
      this.isSelectedSecond = true;
    },
  },
});
</script>
