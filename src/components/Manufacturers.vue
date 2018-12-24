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
        <td class='text-xs-right'>{{ props.item.title }}</td>
        <td class='text-xs-right'>{{ props.item.address }}</td>
        <td class='text-xs-right'>{{ props.item.phone_number }}</td>
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
        { text: 'Название', align: 'right', value: 'title' },
        { text: 'Адресс', align: 'right', value: 'address' },
        { text: 'Номер телефона', align: 'right', value: 'phone_number' },
      ],
      data: [
        {
          id: 2,
          title: 'AAA',
          address: 'Test',
          phone_number: '+38096777777',
        },
        {
          id: 1,
          title: 'CCC',
          address: 'Test 2',
          phone_number: '+38098777777',
        },
        {
          id: 3,
          title: 'Test 3',
          address: 'Tesssssst',
          phone_number: '+38099999999',
        },
      ]
    }
  }
}
</script>

<style scoped>
</style>
