<template>
  <v-container>
    <div id="test"></div>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {};
  },
  mounted() {
    this.getSampleJson();
  },
  methods: {
    getSampleJson() {
      let url = "https://hub.docker.com/v2/search/repositories/?query=alpine";
      fetch(url, {
        method: "GET",
        mode: "no-cors",
      })
        .then(function (response) {
          return response.json();
        })
        .then((r) => {
          console.log(r);
        });
    },
  },
};
</script>

<style>
::-webkit-scrollbar {
  width: 0px;
  background: #fff0;
}
::-webkit-scrollbar-thumb {
  color: #2175f3;
}
::-webkit-scrollbar-track {
  background: #fff0;
}
</style>