<template>
  <div>
    <p class="">{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "Ping",
  data() {
    return {
      msg: "Pong",
    };
  },
  methods: {
    getResponse() {
      const path = "http://127.0.0.1:5000/ping";
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error.message);
        });
    },
  },
  created(){
    this.getResponse()
  }
};
</script>
