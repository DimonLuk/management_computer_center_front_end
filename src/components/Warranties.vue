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
      :items='data'
      :search='search'
      class='elevation-1'
    >
      <template slot='items' slot-scope='props'>
        <td class='text-xs-right'>{{ props.item.id }}</td>
        <td class='text-xs-right'>{{ props.item.start_date }}</td>
        <td class='text-xs-right'>{{ props.item.end_date }}</td>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
export default {
  name: 'Computers',
  data() {
    return {
      search: '',
      headers: [
        { text: 'id', align: 'right', value: 'id' },
        { text: 'Дата начала', align: 'right', value: 'start_date' },
        { text: 'Дата конца', align: 'right', value: 'end_date' },
      ],
      data: [
        {
          id: 2,
          start_date: 'AAA',
          end_date: 'AAA',
        },
        {
          id: 1,
          start_date: 'CCC',
          end_date: 'CCC',
        },
        {
          id: 3,
          start_date: 'BBB',
          end_date: 'BBB',
        },
      ]
    }
  }
}
</script>

<style scoped>
</style>
