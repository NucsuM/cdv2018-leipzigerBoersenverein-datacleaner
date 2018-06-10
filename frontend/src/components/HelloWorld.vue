<template>
 <div class="hello"> 
   <pre style="text-align: left">
     {{JSON.stringify(classificated, null, 4)}}
     </pre>
    <button @click="getNextLine()">nextLine</button> 
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
 </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      line:
        "Adlers Erben, Rats- & Universitätsbuchdruckerei und Verlagsanstalt, später GmbH, Inhaber Carl Boldt, Rostock",
        lineIndex:1,
        classifications:['Name1','Name2','Inhaber','Titel','Stadt1','Stadt2'],
        classificated:[]
    };
  },
  computed: {
    splitedString: function() {
      let splitedString = this.line.split(', ');
      return splitedString;
    }
  },
  methods: {
    addToClassification: function(a, b){
      console.log('ADDING ' + a + ' - ' + b)
      let current = this.classificated;
      let tmp = {
        word:a, 
        clas:b
      }
      console.dir(tmp);
      current.push(tmp);
      this.classificated = current
    },
    getNextLine: function() {
        let lines = ["Adlers Erben, Rats- & Universitätsbuchdruckerei und Verlagsanstalt, später GmbH, Inhaber Carl Boldt, Rostock",
        "Ackermann, Friedrich Adolf, Inhaber der Firma Friedrich Adolf Ackermanns Kunstverlag, München",
        "Hampel, Emil, Buchdruckerei, Buch- und Kunsthandlung, Weisswasser"]

        this.classificated = []

        this.line = lines[this.lineIndex]
        this.lineIndex++
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
