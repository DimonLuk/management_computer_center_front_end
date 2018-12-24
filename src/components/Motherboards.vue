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
        <td class='text-xs-right'>{{ props.item.form_factor }}</td>
        <td class='text-xs-right'>{{ props.item.chipset }}</td>
        <td class='text-xs-right'>{{ props.item.pci_slots }}</td>
        <td class='text-xs-right'>{{ props.item.used_pci_slots }}</td>
        <td class='text-xs-right'>{{ props.item.ram_slots }}</td>
        <td class='text-xs-right'>{{ props.item.used_ram_slots }}</td>
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
        { text: 'Форм-фактор', align: 'right', value: 'form_factor' },
        { text: 'Чипсет', align: 'right', value: 'chipset' },
        { text: 'PCI-слоты', align: 'right', value: 'pci_slots' },
        { text: 'Занятые PCI-слоты', align: 'right', value: 'used_pci_slots' },
        { text: 'RAM слоты', align: 'right', value: 'ram_slots' },
        { text: 'Занятые RAM слоты', align: 'right', value: 'used_ram_slots' },
      ],
      data: [
        {
          id: 2,
          serial_number: 'AAA',
          manufacturer_id: 1,
          warranty_id: 1,
          status: 'Working',
          form_factor: 'ATX',
          chipset: 'H77',
          pci_slots: 4,
          used_pci_slots: 2,
          ram_slots: 4,
          used_ram_slots: 2
        },
        {
          id: 1,
          serial_number: 'CCC',
          manufacturer_id: 2,
          warranty_id: 2,
          status: 'Broken',
          form_factor: 'mATX',
          chipset: 'H78',
          pci_slots: 6,
          used_pci_slots: 2,
          ram_slots: 6,
          used_ram_slots: 2
        },
        {
          id: 3,
          serial_number: 'BBB',
          manufacturer_id: 3,
          warranty_id: 4,
          status: 'Reparing',
          form_factor: 'l-ATX',
          chipset: 'Z92',
          pci_slots: 8,
          used_pci_slots: 4,
          ram_slots: 8,
          used_ram_slots: 5
        },
      ]
    }
  }
}
</script>

<style scoped>
</style>
