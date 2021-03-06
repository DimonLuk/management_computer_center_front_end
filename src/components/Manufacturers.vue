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
              :items='manufacturers'
              item-text='id'
              item-value='id'
              solo
              v-if='mode === "update" || mode === "delete"'
              @change='prefill()'
            >
            </v-select>
          <v-text-field
  :rules="rules.notMoreThanTen"
  v-model="formData.title"
  label="Название"
  required
  v-if='mode === "create" || mode === "update"'
></v-text-field>
<v-text-field
  :rules="rules.notMoreThanTen"
  v-model="formData.address"
  label="Адресс"
  required
  v-if='mode === "create" || mode === "update"'
></v-text-field>
<v-text-field
  :rules="rules.notMoreThanTen"
  mask="+############"
  v-model="formData.phoneNumber"
  label="Номер Телефона"
  required
  v-if='mode === "create" || mode === "update"'
></v-text-field>

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
        
    { text: 'Название', align: 'right', value: 'title' },
    { text: 'Адресс', align: 'right', value: 'address' },
    { text: 'Номер Телефона', align: 'right', value: 'phoneNumber' },
      ],
      isDisplayForm: false,
      valid: false,
      formData: {
        id: '',
        
    title: '',
    address: '',
    phoneNumber: '',
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
        const data = find(this.manufacturers, el => el.id === this.formData.id);
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
      this.$apollo.queries.manufacturers.refetch();
    },
    async deleteModel() {
      await this.$apollo.mutate({
        mutation: gql`
          mutation($id: Int!) {
            deleteManufacturer(input: {
              id: $id
            }) {
              manufacturer {
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
      const data = find(this.manufacturers, el => el.id === this.formData.id);
      
      const result = await this.$apollo.mutate({
        mutation: gql`
          mutation ($id: Int!, $title: String!, $address: String!, $phoneNumber: String!) {
            updateManufacturer(input: {
              id: $id,
              title: $title,
address: $address,
phoneNumber: $phoneNumber
            }) {
              manufacturer {
                id
              }    
            }
          }
        `,
        variables: {
          id: Number(data.id),
          title: this.formData.title,
address: this.formData.address,
phoneNumber: this.formData.phoneNumber
        }
      });
    },
    async createModel() {
      
      const result = await this.$apollo.mutate({
        mutation: gql`
          mutation ($title: String!, $address: String!, $phoneNumber: String!) {
            createManufacturer(input: {
              title: $title,
address: $address,
phoneNumber: $phoneNumber
            }) {
              manufacturer {
                id
              }    
            }
          }
        `,
        variables: {
          title: this.formData.title,
address: this.formData.address,
phoneNumber: this.formData.phoneNumber
        }
      });
    }
  },
  apollo: {
    manufacturers: gql`
      query {
      manufacturers {
          
          id,
          title,
address,
phoneNumber
        }
      }
    `,
    
    
  }
}
</script>

<style scoped>
</style>
