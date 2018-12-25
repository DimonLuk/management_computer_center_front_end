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
      :items='manufacturers'
      :search='search'
      class='elevation-1'
    >
      <template slot='items' slot-scope='props'>
        <td class='text-xs-right'>{{ props.item.id }}</td>
        <td class='text-xs-right'>{{ props.item.title }}</td>
        <td class='text-xs-right'>{{ props.item.address }}</td>
        <td class='text-xs-right'>{{ props.item.phoneNumber }}</td>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import  gql from 'graphql-tag'
export default {
  name: 'Computers',
  data() {
    return {
      search: '',
      headers: [
        { text: 'id', align: 'right', value: 'id' },
        { text: 'Название', align: 'right', value: 'title' },
        { text: 'Адресс', align: 'right', value: 'address' },
        { text: 'Номер телефона', align: 'right', value: 'phoneNumber' },
      ],
    }
  },
  apollo: {
    manufacturers: gql`query {
      manufacturers {
        id,
        title,
        phoneNumber,
        address
      }
    }`
  }
}
</script>

<style scoped>
</style>
