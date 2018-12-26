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
      :items='|model_s|'
      :search='search'
      class='elevation-1'
    >
      <template slot='items' slot-scope='props'>
        <td class='text-xs-right'>{{ props.item.id }}</td>
        |form_columns|
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
              :items='|model_s|'
              item-text='id'
              item-value='id'
              solo
              v-if='mode === "update" || mode === "delete"'
              @change='prefill()'
            >
            </v-select>
          |form_fields|
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
        |table_headers|
      ],
      isDisplayForm: false,
      valid: false,
      formData: {
        id: '',
        |form_field_data|
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
        const data = find(this.|model_s|, el => el.id === this.formData.id);
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
      window.location.reload();
    },
    async deleteModel() {
      await this.$apollo.mutate({
        mutation: gql`
          mutation($id: Int!) {
            delete|model_c_f|(input: {
              id: $id
            }) {
              |model| {
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
      const data = find(this.|model_s|, el => el.id === this.formData.id);
      |update_component_meta_info|
      const result = await this.$apollo.mutate({
        mutation: gql`
          mutation ($id: Int!, |main_params|) {
            update|model_c_f|(input: {
              id: $id,
              |main_params_and_values|
            }) {
              |model| {
                id
              }    
            }
          }
        `,
        variables: {
          id: Number(data.id),
          |main_values|
        }
      });
    },
    async createModel() {
      |create_component_meta_info|
      const result = await this.$apollo.mutate({
        mutation: gql`
          mutation (|main_params|) {
            create|model_c_f|(input: {
              |main_params_and_values|
            }) {
              |model| {
                id
              }    
            }
          }
        `,
        variables: {
          |main_values|
        }
      });
    }
  },
  apollo: {
    |model_s|: gql`
      query {
      |model_s| {
          |component_meta_info_query|
          id,
          |model_fields|
        }
      }
    `,
    |manufacturers_query|
    |warrantys_query|
  }
}
</script>

<style scoped>
</style>
