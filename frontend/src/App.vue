<template>
  <div id="app">
    <button v-on:click="startRequest()">Speichern nächsten Datensatz holen</button>
<table>
<tr>
  <th></th>
  <th></th>
  <th></th>
  <th></th>
</tr>
<tr>
  <td>Inhaber: </td>
  <td><input v-model="message1" placeholder="edit me1"></td>
  <td><input v-model="message1" placeholder="edit me1"></td>
  <td><input v-model="message1" placeholder="edit me1"></td>
</tr>
<tr>
  <td>Firma</td>
  <td><input v-model="message1" placeholder="Name"></td>
  <td><input v-model="message1" placeholder="Art"></td>
  <td></td>
</tr>
<tr>
  <td>Standort:</td>
  <td><input v-model="message1" placeholder="edit me3"></td>
  <td></td>
  <td></td>
</tr>
<tr>
  <td></td>
  <td><input v-model="message1" placeholder="edit me4"></td>
  <td></td>
  <td></td>
</tr>
</table>

 <textarea rows="4" cols="50">
At w3schools.com you will learn how to make a website. We offer free tutorials in all web development technologies.
</textarea> 


  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "app",
  data() {
    return {
      message1: " App1",
      message2: " App2",
      message3: " App3",
      message4: " App4",
      posts: ""
    };
  },
  created() {},
  methods: {
    startRequest: function() {
      axios
        .get(`http://jsonplaceholder.typicode.com/users`)
        .then(response => {
          // JSON responses are automatically parsed.
          this.posts = response.data;
          console.dir(this.posts[0]);
          this.message1 = this.posts[0]["name"];
          this.message2 = this.posts[0]["website"];
          this.message3 = this.posts[0]["email"];
          this.message4 = this.posts[0]["phone"];
        })
        .catch(e => {
          this.errors.push(e);
        });
    }
  }
};
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
