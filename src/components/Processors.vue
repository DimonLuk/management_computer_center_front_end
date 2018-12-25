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
      :items='processors'
      :search='search'
      class='elevation-1'
    >
      <template slot='items' slot-scope='props'>
        <td class='text-xs-right'>{{ props.item.id }}</td>
        <td class='text-xs-right'>{{ props.item.componentMetaInfo.serialNumber }}</td>
        <td class='text-xs-right'>{{ props.item.componentMetaInfo.manufaTurer_id }}</td>
        <td class='text-xs-right'>{{ props.item.componentMetaInfo.warrantyId }}</td>
        <td class='text-xs-right'>{{ props.item.componentMetaInfo.status }}</td>
        <td class='text-xs-right'>{{ props.item.cores }}</td>
        <td class='text-xs-right'>{{ props.item.l1Cache }}</td>
        <td class='text-xs-right'>{{ props.item.l2Cache }}</td>
        <td class='text-xs-right'>{{ props.item.l3Cache }}</td>
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
        { text: 'Серийный номер', align: 'right', value: 'serialNumber' },
        { text: 'Производитель(id)', align: 'right', value: 'manufacturerId' },
        { text: 'Гарантия(id)', align: 'right', value: 'warrantyId' },
        { text: 'Статус(id)', align: 'right', value: 'status' },
        { text: 'Ядра', align: 'right', value: 'cores' },
        { text: 'l1-кэш(Kb)', align: 'right', value: 'l1Cache' },
        { text: 'l2-кэш(Kb)', align: 'right', value: 'l2Cache' },
        { text: 'l3-кэш(Kb)', align: 'right', value: 'l3Cache' },
      ],
    }
  },
  apollo: {
    processors: gql`
      query {
        processors {
          id,
          componentMetaInfo {
            serialNumber,
            manufacturerId,
            warrantyId,
            status
          }
          cores,
          l1Cache,
          l2Cache,
          l3Cache
        }
      }
    `
  }
}
</script>

<style scoped>
</style>
