<template>
 <div class="hello"> 
   <pre style="text-align: left">
     {{JSON.stringify(classificated, null, 4)}}
     </pre>
    <button @click="tableCreate()">refreshTable</button> 
    <table>
    <tbody>
    <tr v-for="(part, key) in splitedString" :key="key">
    <td>{{part}}</td>
    <td>
      <select>
      <option v-for="(clas, ckey) in classifications" :value="clas" :key="ckey">{{clas}}</option>
      </select>
    </td>
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
        classifications:['a','b','c'],
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
    refreshTable: function() {
      console.log("xxx");
    },
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
    tableCreate: function() {
      var body = document.body,
      tbl = document.createElement("table");
      tbl.style.width = "100px";
      tbl.style.border = "1px solid black";

      for (var i = 0; i < 3; i++) {
        var tr = tbl.insertRow();
        var td = tr.insertCell();
        td.appendChild(document.createElement("<tr><td>5</td><td>2</td><td>10</td><td>500</td></tr>"));
/*         for (var j = 0; j < 2; j++) {
          if (i == 2 && j == 1) {
            break;
          } else {
            var td = tr.insertCell();
            td.appendChild(document.createTextNode("Cell"));
            td.style.border = "1px solid black";
            if (i == 1 && j == 1) {
              td.setAttribute("rowSpan", "2");
            }
          }
        } */
      }
      body.appendChild(tbl);
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
