<template>
  <v-container fluid>
    <v-text-field
      v-model='search'
      append-icon='search'
      label='Поиск'
      single-line
      hide-details
    >
    </v-text-field>
    <v-data-table
      :headers='headers'
      :items='warrantys'
      :search='search'
      class='elevation-1'
    >
      <template slot='items' slot-scope='props'>
        <td class='text-xs-right'>{{ props.item.id }}</td>
        <td class='text-xs-right'>{{ props.item.startDate }}</td>
        <td class='text-xs-right'>{{ props.item.endDate }}</td>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import gql from 'graphql-tag'

export default {
  name: 'Computers',
  data() {
    return {
      search: '',
      headers: [
        { text: 'id', align: 'right', value: 'id' },
        { text: 'Дата начала', align: 'right', value: 'startDate' },
        { text: 'Дата конца', align: 'right', value: 'endDate' },
      ],
    }
  },
  apollo: {
    warrantys: gql`
      query {
        warrantys {
          id,
          startDate,
          endDate
        }
      }
    `
  }
}
</script>

<style scoped>
</style>
