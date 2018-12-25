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
      :items='computers'
      :search='search'
      class='elevation-1'
    >
      <template slot='items' slot-scope='props'>
        <td class='text-xs-right'>{{ props.item.id }}</td>
        <td class='text-xs-right'>{{ props.item.room }}</td>
        <td class='text-xs-right'>{{ props.item.trunkId }}</td>
        <td class='text-xs-right'>{{ props.item.motherboardId }}</td>
        <td class='text-xs-right'>{{ props.item.ramId }}</td>
        <td class='text-xs-right'>{{ props.item.processorId }}</td>
      </template>
    </v-data-table>
    <v-form v-model='valid'>
      <v-dialog
        v-model='dialog'
        width='500'  
      >
        <v-btn
          slot='activator'
          color='green lighten-2'
        >
          Добавить
        </v-btn>
        <v-card>
          <v-card-title
            class="headline grey lighten-2"
            primary-title
          >
            Добавить
          </v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-select
              required
              v-model='trunk'
              :items='getTrunkIds()'  
              label='Достпные корпуса (id)'
              solo
            >
            </v-select>
            <v-select
              required
              v-model='motherboard'
              :items='getMotherboardIds()'  
              label='Доступные материнские платы (id)'
              solo
            >
            </v-select>
            <v-select
              required
              v-model='ram'
              :items='getRamIds()'  
              label='Доступные оперативные памяти (id)'
              solo
            >
            </v-select>
            <v-select
              required
              v-model='processor'
              :items='getProcessorIds()'  
              label='Доступные процессоры (id)'
              solo
            >
            </v-select>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-spacer></v-spacer>
             <v-btn
               color="primary"
               flat
               @click='dialog = !(trunk && motherboard && ram && processor)'
             >
             Ok
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-form>
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
        { text: 'Комната(id)', align: 'right', value: 'room' },
        { text: 'Корпус(id)', align: 'right', value: 'trunkId' },
        { text: 'Материнская плата(id)', align: 'right', value: 'motherboardId' },
        { text: 'Оперативная память(id)', align: 'right', value: 'ramId' },
        { text: 'Процессор', align: 'right', value: 'processorId' },
      ],
      dialog: false,
      valid: false,
      trunk: undefined,
      motherboard: undefined,
      ram: undefined,
      processor: undefined
    }
  },
  methods: {
    getTrunkIds() {
      return this.trunks.map(el => el.id);
    },
    getMotherboardIds() {
      return this.motherboards.map(el => el.id);
    },
    getRamIds() {
      return this.rams.map(el => el.id);
    },
    getProcessorIds() {
      return this.processors.map(el => el.id);
    },
  },
  apollo: {
    computers: gql`
      query {
        computers {
          id,
          room,
          trunkId,
          motherboardId,
          ramId,
          processorId
        }
      }
    `,
    trunks: gql`
      query {
        trunks {
          id
        }
      }
    `,
    motherboards: gql`
      query {
        motherboards {
          id
        }
      }
    `,
    rams: gql`
      query {
        rams {
          id
        }
      }
    `,
    processors: gql`
      query {
        processors {
          id
        }
      }
    `
  }
}
</script>

<style scoped>
</style>
