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
        v-model='isDisplayForm'
        width='500'  
      >
        <v-btn
          slot='activator'
          color='green lighten-2'
          @click='prefill("create")'
        >
          Добавить
        </v-btn>
        <v-btn
          slot='activator'
          color='yellow lighten-2'
          @click='mode = "update"'
        >
          Редактировать
        </v-btn>
        <v-btn
          slot='activator'
          color='red lighten-2'
          @click='mode = "delete"'
        >
          Удалить
        </v-btn>
        <v-card>
          <v-card-title
            class="headline grey lighten-2"
            primary-title
          >
            {{ getDialogHeader() }}
          </v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-select
              v-model='formData.id' 
              label='id'
              :items='computers'
              item-text='id'
              item-value='id'
              solo
              v-if='mode === "update" || mode === "delete"'
              @change='prefill()'
            >
            </v-select>
          <v-text-field
  :rules="rules.notMoreThanTen"
  v-model="formData.room"
  label="Комната"
  required
  v-if='mode === "create" || mode === "update"'
></v-text-field>
<v-select
  :items="trunks"
  solo
  :rules="rules.notEmptySelector"
  :item-text="combineComponent"
  item-value="id"
  v-model="formData.trunkId"
  label="Корпус"
  required
  v-if='mode === "create" || mode === "update"'
></v-select>
<v-select
  :items="motherboards"
  solo
  :rules="rules.notEmptySelector"
  :item-text="combineComponent"
  item-value="id"
  v-model="formData.motherboardId"
  label="Материнская плата"
  required
  v-if='mode === "create" || mode === "update"'
></v-select>
<v-select
  :items="rams"
  solo
  :rules="rules.notEmptySelector"
  :item-text="combineComponent"
  item-value="id"
  v-model="formData.ramId"
  label="Оперативная память"
  required
  v-if='mode === "create" || mode === "update"'
></v-select>
<v-select
  :items="processors"
  solo
  :rules="rules.notEmptySelector"
  :item-text="combineComponent"
  item-value="id"
  v-model="formData.processorId"
  label="Процессор"
  required
  v-if='mode === "create" || mode === "update"'
></v-select>

          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-spacer></v-spacer>
             <v-btn
               color="primary"
               flat
               @click='validateAndMutate()'
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
import gql from 'graphql-tag';
import { find } from 'lodash';

export default {
  name: 'Motherboards',
  data() {
    return {
      search: '',
      mode: 'create',
      prevMode: '',
      headers: [
        { text: 'id', align: 'right', value: 'id' },
        
    { text: 'Комната', align: 'right', value: 'room' },
    { text: 'Корпус', align: 'right', value: 'trunkId' },
    { text: 'Материнская плата', align: 'right', value: 'motherboardId' },
    { text: 'Оперативная память', align: 'right', value: 'ramId' },
    { text: 'Процессор', align: 'right', value: 'processorId' },
      ],
      isDisplayForm: false,
      valid: false,
      formData: {
        id: '',
        
    room: '',
    trunkId: '',
    motherboardId: '',
    ramId: '',
    processorId: '',
      },
      rules: {
        notMoreThanTen: [
          v => !!v || 'Введите значение',
          v => v.length <= 10 || 'Не должно быть длинее 10 сиволов' ],
        notEmptySelector: [
          v => !!v || 'Выберите вариант',
        ],
      }
    }
  },
  methods: {
    prefill(mode) {
      if(mode)
        this.mode = mode;
      if(this.mode === 'update') {
        this.prevMode = 'update'
        const data = find(this.computers, el => el.id === this.formData.id);
        for (let key in this.formData) {
          if (data[key]) {
            this.formData[key] = '' + data[key];
          } else if(data.componentMetaInfo[key]) {
            this.formData[key] = '' + data.componentMetaInfo[key];
          }
        }
      } else if(this.mode === 'create' && this.prevMode === 'update') {
        this.prevMode = 'create'
        for (let key in this.formData) {
          this.formData[key] = '';
        }
      }
    },
    getDialogHeader() {
      if(this.mode === 'create') return 'Добавить'  
      if(this.mode === 'update') return 'Редактировать'  
      if(this.mode === 'delete') return 'Удалить'  
    },
    combineComponent(component) {
      return `${component.id} ${component.componentMetaInfo.serialNumber}`
    },
    combineDates(warranty) {
      return `${warranty.startDate}   ${warranty.endDate}`;
    },
    async validateAndMutate() {
      Object.keys(this.formData).map(el => {
        if(this.mode !== 'delete' && !this.formData[el]) return;
      })
      this.isDisplayForm = false;
      if(this.mode === 'create') await this.createModel();
      if(this.mode === 'update') await this.updateModel();
      if(this.mode === 'delete') await this.deleteModel();
      this.$apollo.queries.computers.refetch();
    },
    async deleteModel() {
      await this.$apollo.mutate({
        mutation: gql`
          mutation($id: Int!) {
            deleteComputer(input: {
              id: $id
            }) {
              computer {
                id
              }
            }
          }
        `,
        variables: {
          id: this.formData.id
        }
      });
    },
    async updateModel() {
      const data = find(this.computers, el => el.id === this.formData.id);
      
      const result = await this.$apollo.mutate({
        mutation: gql`
          mutation ($id: Int!, $room: String!, $trunkId: Int!, $motherboardId: Int!, $ramId: Int!, $processorId: Int!) {
            updateComputer(input: {
              id: $id,
              room: $room,
trunkId: $trunkId,
motherboardId: $motherboardId,
ramId: $ramId,
processorId: $processorId
            }) {
              computer {
                id
              }    
            }
          }
        `,
        variables: {
          id: Number(data.id),
          room: this.formData.room,
trunkId: Number(this.formData.trunkId),
motherboardId: Number(this.formData.motherboardId),
ramId: Number(this.formData.ramId),
processorId: Number(this.formData.processorId)
        }
      });
    },
    async createModel() {
      
      const result = await this.$apollo.mutate({
        mutation: gql`
          mutation ($room: String!, $trunkId: Int!, $motherboardId: Int!, $ramId: Int!, $processorId: Int!) {
            createComputer(input: {
              room: $room,
trunkId: $trunkId,
motherboardId: $motherboardId,
ramId: $ramId,
processorId: $processorId
            }) {
              computer {
                id
              }    
            }
          }
        `,
        variables: {
          room: this.formData.room,
trunkId: Number(this.formData.trunkId),
motherboardId: Number(this.formData.motherboardId),
ramId: Number(this.formData.ramId),
processorId: Number(this.formData.processorId)
        }
      });
    }
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
        trunks (unused: true) {
          id,
          componentMetaInfo {
            serialNumber
          }
        }
      }
    `,
    motherboards: gql`
      query {
        motherboards (unused: true){
          id,
          componentMetaInfo {
            serialNumber
          }
        }
      }
    `,
    rams: gql`
      query {
        rams (unused: true) {
          id,
          componentMetaInfo {
            serialNumber
          }
        }
      }
    `,
    processors: gql`
      query {
        processors (unused: true) {
          id,
          componentMetaInfo {
            serialNumber
          }
        }
      }
    `,
    
  }
}
</script>

<style scoped>
</style>
