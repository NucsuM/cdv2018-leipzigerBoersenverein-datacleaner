<template>
 <div class="hello"> 
    <button @click="getNextLine()">get new Line</button>
    <button @click="sendToApi()">send to api</button>    
    <pre>
    {{line}}
    </pre>
    <table>
    <tbody>
    <tr v-for="(part, key) in splitedString" :key="key">
    <td>{{part}}</td>
<!--     <td>
      <select>
      <option v-for="(clas, ckey) in classifications" :value="clas" :key="ckey">{{clas}}</option>
      </select>
    </td> -->
      <td>
      <button @click="addToClassification(part,clas)" v-for="(clas, ckey) in classifications" :value="clas" :key="ckey">{{clas}}</button>
    </td>
    </tr>
    </tbody>
    </table>
       <pre style="text-align: left">
     {{JSON.stringify(classificated, null, 4)}}
     </pre>
 </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "HelloWorld",
  data() {
    return {
      line:
        "Hallwig, Hugo, Buchhandlung, Marburg",
        lineIndex:1,
        classifications:['Name','Inhaber','Titel','Stadt', 'Stadt (früher)'],
        classificated: {},
        classificatedMap: [],
        errors:[]
    };
  },
  computed: {
    splitedString: function() {
      /* eslint-disable */
      this.classificated = {'Name': [], 'Inhaber':[], 'Titel':[], 'Stadt' :[], 'Stadt (früher)':[]}
      this.classificatedMap = []
      let splitedString = this.line.split(', ');
      return splitedString;
      /* eslint-enable */
    }
  },
  methods: {
    addToClassification: function(part, clas){
      console.dir(this)
      if (this.classificatedMap.indexOf(part) === -1)
      {
        
        this.classificated[clas].push(part)
        this.classificatedMap.push(part)
      }
      else {
        console.log('exists - not added')
      }

    },
    getNextLine: function() {
        axios.get('http://localhost:5000/robert').then(response => {
          this.line = response.data.file
          })
          .catch(e => {
            this.errors.push(e)
          })
    },
    sendToApi: function() {
      axios.post('/save', this.classificated)
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        });
      }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
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
