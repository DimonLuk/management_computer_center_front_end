<template>
  <v-container fluid>
    <v-textarea
      solo
      label="Write your sql"
      v-model='sqlQuery'
      @change='getResultOfQuery'
    ></v-textarea>
    <v-btn
      color="success"
      @click='getResultOfQuery'
    >Обработать запрос</v-btn>
    <v-data-table
      :headers='headers'  
      :items='result'
      class='elevation-1'
    >
      <template
        slot='items'  
        slot-scope='props'
      >
        <td
          v-for='i in headers'
          class='text-xs-right'
        >
          {{ props.item[i.text] }}
        </td>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
export default {
  name: 'CustomSqlPage',
  data() {
    return {
      sqlQuery: '',
      result: [],
      headers: [],
    }
  },
  methods: {
    async getResultOfQuery() {
      if(this.sqlQuery === '') {
        this.result = [];
        this.headers = [];
      }
      const tmp = await fetch('http://localhost:5000/custom/customsql', {
        headers: {
          'Accept': 'applications/json',
          'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify({ sql_query: this.sqlQuery })
      });
      const result = await tmp.json();
      const headers = []
      for(let i of result.column_names) {
        headers.push({ text: i, align: 'right', value: i })
      }
      this.headers = headers;
      this.result = result.column_values;
    }
  }
}
</script>

<style scoped>
</style
