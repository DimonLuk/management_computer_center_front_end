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
        <td class='text-xs-right'>{{ props.item.serial_number }}</td>
        <td class='text-xs-right'>{{ props.item.manufacturer_id }}</td>
        <td class='text-xs-right'>{{ props.item.warranty_id }}</td>
        <td class='text-xs-right'>{{ props.item.status }}</td>
        <td class='text-xs-right'>{{ props.item.width }}</td>
        <td class='text-xs-right'>{{ props.item.height }}</td>
        <td class='text-xs-right'>{{ props.item.form_factor }}</td>
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
        { text: 'Серийный номер', align: 'right', value: 'serial_number' },
        { text: 'Производитель(id)', align: 'right', value: 'manufacturer_id' },
        { text: 'Гарантия(id)', align: 'right', value: 'warranty_id' },
        { text: 'Статус(id)', align: 'right', value: 'status' },
        { text: 'Ширина(Cm)', align: 'right', value: 'width' },
        { text: 'Высота(Cm)', align: 'right', value: 'height' },
        { text: 'Форм-фактор(Cm)', align: 'right', value: 'form_factor' },
      ],
      data: [
        {
          id: 2,
          serial_number: 'AAA',
          manufacturer_id: 1,
          warranty_id: 1,
          status: 'Working',
          width: 8,
          height: 1,
          form_factor: 'ATX',
        },
        {
          id: 1,
          serial_number: 'CCC',
          manufacturer_id: 2,
          warranty_id: 2,
          status: 'Broken',
          width: 8,
          height: 1,
          form_factor: 'mATX',
        },
        {
          id: 3,
          serial_number: 'BBB',
          manufacturer_id: 3,
          warranty_id: 4,
          status: 'Reparing',
          width: 8,
          height: 1,
          form_factor: 'l-ATX',
        },
      ]
    }
  }
}
</script>

<style scoped>
</style>
