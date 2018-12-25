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
      :items='trunks'
      :search='search'
      class='elevation-1'
    >
      <template slot='items' slot-scope='props'>
        <td class='text-xs-right'>{{ props.item.id }}</td>
        <td class='text-xs-right'>{{ props.item.componentMetaInfo.serialNumber }}</td>
        <td class='text-xs-right'>{{ props.item.componentMetaInfo.manufacturerId }}</td>
        <td class='text-xs-right'>{{ props.item.componentMetaInfo.warrantyId }}</td>
        <td class='text-xs-right'>{{ props.item.componentMetaInfo.status }}</td>
        <td class='text-xs-right'>{{ props.item.width }}</td>
        <td class='text-xs-right'>{{ props.item.height }}</td>
        <td class='text-xs-right'>{{ props.item.formFactor }}</td>
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
        { text: 'Ширина(Cm)', align: 'right', value: 'width' },
        { text: 'Высота(Cm)', align: 'right', value: 'height' },
        { text: 'Форм-фактор(Cm)', align: 'right', value: 'formFactor' },
      ],
    }
  },
  apollo: {
    trunks: gql`
      query {
        trunks {
          id,
          componentMetaInfo {
            serialNumber,
            manufacturerId,
            warrantyId,
            status
          },
          width,
          height,
          formFactor
        }
      }
    `
  }
}
</script>

<style scoped>
</style>
