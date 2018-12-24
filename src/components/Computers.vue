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
        <td class='text-xs-right'>{{ props.item.room }}</td>
        <td class='text-xs-right'>{{ props.item.trunk_id }}</td>
        <td class='text-xs-right'>{{ props.item.motherboard_id }}</td>
        <td class='text-xs-right'>{{ props.item.ram_id }}</td>
        <td class='text-xs-right'>{{ props.item.processor_id }}</td>
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
        { text: 'Комната(id)', align: 'right', value: 'room' },
        { text: 'Корпус(id)', align: 'right', value: 'trunk_id' },
        { text: 'Материнская плата(id)', align: 'right', value: 'motherboard_id' },
        { text: 'Оперативная память(id)', align: 'right', value: 'ram_id' },
        { text: 'Процессор', align: 'right', value: 'processor_id' },
      ],
      data: [
        {
          id: 2,
          room: 'AAA',
          trunk_id: 1,
          motherboard_id: 1,
          ram_id: 1,
          processor_id: 1
        },
        {
          id: 3,
          room: 'AAA',
          trunk_id: 1,
          motherboard_id: 1,
          ram_id: 1,
          processor_id: 1
        },
        {
          id: 1,
          room: 'AAA',
          trunk_id: 1,
          motherboard_id: 1,
          ram_id: 1,
          processor_id: 1
        },
        {
          id: 6,
          room: 'AAA',
          trunk_id: 2,
          motherboard_id: 1,
          ram_id: 1,
          processor_id: 1
        },
      ]
    }
  }
}
</script>

<style scoped>
</style>
