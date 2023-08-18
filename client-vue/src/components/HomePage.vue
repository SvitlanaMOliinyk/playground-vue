<template>
  <div class="container">
    <div class="d-flex justify-content-around">
    <button @click="handleClick" class="btn btn-secondary">
      <span v-if="!isSelected">Choose location</span>
      <span v-else>Hide location</span>
    </button>
    <button @click="handleUsersClick" class="btn btn-outline-secondary">Show users</button>
    </div>
    <StartMap
      v-if="!isSelectedSecond || responseData.length <= 0"
      @position-updated="handlePositionUpdated"
    />
    <SelectPlaces
      v-if="isSelected"
      @response-updated="handleResponseData"
      :position="position"
    />
    <MapRender
      v-if="responseData.length > 0"
      :position="position"
      :markers="responseData"
      @close="handleCloseMap"
    />
    <!-- <UserTemplate
    v-if="isUsersClicked"
    /> -->
  </div>
</template>


<script lang="ts">
import { defineComponent } from "vue";
import router from "../router";
import SelectPlaces from "./SelectPlaces.vue";
import StartMap from "./StartMap.vue";
import MapRender from "./MapRender.vue";
import UserTemplate from "./UsersTemplate.vue";


interface ResponseObject {
  referencePosition: {
    latitude: number;
    longitude: number;
  };
  name: string;
}

export default defineComponent({
  name: "HomePage",
  components: {
    SelectPlaces,
    StartMap,
    MapRender,
  },
  data() {
    return {
      isSelected: false,
      isSelectedSecond: false,
      isUsersClicked: false,
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
      console.log("Position", position);
    },
    handleResponseData(data: ResponseObject[]) {
      this.responseData = data;
      console.log("responseData", this.responseData);
      this.isSelectedSecond = true;
    },
    handleCloseMap() {
      this.responseData = [];
    },
    handleUsersClick() {
      // this.isUsersClicked = !this.isUsersClicked
      router.push('/users');
    }
  },
});
</script>
<style>
.select-button {
  padding: 5px 10px;
  background-color: gray;
  color: white;
  border: none;
  cursor: pointer;
  font-size: 12px;
  border-radius: 4px;
}

.select-button:hover {
  background-color: blue;
}
</style>