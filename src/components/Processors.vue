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
        <td class='text-xs-right'>{{ props.item.componentMetaInfo.manufacturerId }}</td>
        <td class='text-xs-right'>{{ props.item.componentMetaInfo.warrantyId }}</td>
        <td class='text-xs-right'>{{ props.item.componentMetaInfo.status }}</td>
        <td class='text-xs-right'>{{ props.item.cores }}</td>
        <td class='text-xs-right'>{{ props.item.l1Cache }}</td>
        <td class='text-xs-right'>{{ props.item.l2Cache }}</td>
        <td class='text-xs-right'>{{ props.item.l3Cache }}</td>
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
              :items='processors'
              item-text='id'
              item-value='id'
              solo
              v-if='mode === "update" || mode === "delete"'
              @change='prefill()'
            >
            </v-select>
          <v-text-field
  :rules="rules.notMoreThanTen"
  mask="NNNNNNNNNN"
  v-model="formData.serialNumber"
  label="Серийный номер"
  required
  v-if='mode === "create" || mode === "update"'
></v-text-field>
<v-select
  :items="manufacturers"
  solo
  :rules="rules.notEmptySelector"
  item-text="title"
  item-value="id"
  v-model="formData.manufacturerId"
  label="Производитель"
  required
  v-if='mode === "create" || mode === "update"'
></v-select>
<v-select
  :items="warrantys"
  solo
  :rules="rules.notEmptySelector"
  item-text="combineDates"
  item-value="id"
  v-model="formData.warrantyId"
  label="Гарантия"
  required
  v-if='mode === "create" || mode === "update"'
></v-select>
<v-select
  :items="['Ready','Working','Broken','Reparing','Repared']"
  solo
  :rules="rules.notEmptySelector"
  v-model="formData.status"
  label="Статус"
  required
  v-if='mode === "create" || mode === "update"'
></v-select>
<v-text-field
  :rules="rules.notMoreThanTen"
  mask="##"
  v-model="formData.cores"
  label="Ядра"
  required
  v-if='mode === "create" || mode === "update"'
></v-text-field>
<v-text-field
  :rules="rules.notMoreThanTen"
  mask="######"
  v-model="formData.l1Cache"
  label="Кэш 1-го уровня(Kb)"
  required
  v-if='mode === "create" || mode === "update"'
></v-text-field>
<v-text-field
  :rules="rules.notMoreThanTen"
  mask="######"
  v-model="formData.l2Cache"
  label="Кэш 2-го уровня(Kb)"
  required
  v-if='mode === "create" || mode === "update"'
></v-text-field>
<v-text-field
  :rules="rules.notMoreThanTen"
  mask="######"
  v-model="formData.l3Cache"
  label="Кэш 3-го уровня(Kb)"
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
        
    { text: 'Серийный номер', align: 'right', value: 'serialNumber' },
    { text: 'Производитель', align: 'right', value: 'manufacturerId' },
    { text: 'Гарантия', align: 'right', value: 'warrantyId' },
    { text: 'Статус', align: 'right', value: 'status' },
    { text: 'Ядра', align: 'right', value: 'cores' },
    { text: 'Кэш 1-го уровня(Kb)', align: 'right', value: 'l1Cache' },
    { text: 'Кэш 2-го уровня(Kb)', align: 'right', value: 'l2Cache' },
    { text: 'Кэш 3-го уровня(Kb)', align: 'right', value: 'l3Cache' },
      ],
      isDisplayForm: false,
      valid: false,
      formData: {
        id: '',
        
    serialNumber: '',
    manufacturerId: '',
    warrantyId: '',
    status: '',
    cores: '0',
    l1Cache: '0',
    l2Cache: '0',
    l3Cache: '0',
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
        const data = find(this.processors, el => el.id === this.formData.id);
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
      this.$apollo.queries.processors.refetch();
    },
    async deleteModel() {
      await this.$apollo.mutate({
        mutation: gql`
          mutation($id: Int!) {
            deleteProcessor(input: {
              id: $id
            }) {
              processor {
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
      const data = find(this.processors, el => el.id === this.formData.id);
      
      let componentMetaInfoId;
      componentMetaInfoId = await this.$apollo.mutate({
        mutation: gql`
          mutation($id: Int!, $manufacturerId: Int!, $warrantyId: Int!, $status: String!, $serialNumber: String!) {
            updateComponentmetainfo(input : {
              id: $id
              manufacturerId: $manufacturerId,
              warrantyId: $warrantyId,
              status: $status,
              serialNumber: $serialNumber
            }) {
              componentmetainfo {
                id
              }
            }
          }
        `,
        variables: {
          id: Number(data.componentMetaInfoId),
          manufacturerId: Number(this.formData.manufacturerId),
          warrantyId: Number(this.formData.warrantyId),
          status: this.formData.status,
          serialNumber: this.formData.serialNumber,
        }
      })
      componentMetaInfoId = componentMetaInfoId.data.updateComponentmetainfo.componentmetainfo.id;

      const result = await this.$apollo.mutate({
        mutation: gql`
          mutation ($id: Int!, $cores: Int!, $l1Cache: Int!, $l2Cache: Int!, $l3Cache: Int!, $componentMetaInfoId: Int!) {
            updateProcessor(input: {
              id: $id,
              cores: $cores,
l1Cache: $l1Cache,
l2Cache: $l2Cache,
l3Cache: $l3Cache,
componentMetaInfoId: $componentMetaInfoId
            }) {
              processor {
                id
              }    
            }
          }
        `,
        variables: {
          id: Number(data.id),
          cores: Number(this.formData.cores),
l1Cache: Number(this.formData.l1Cache),
l2Cache: Number(this.formData.l2Cache),
l3Cache: Number(this.formData.l3Cache),
componentMetaInfoId: Number(componentMetaInfoId)
        }
      });
    },
    async createModel() {
      
      let componentMetaInfoId;
      componentMetaInfoId = await this.$apollo.mutate({
        mutation: gql`
          mutation($manufacturerId: Int!, $warrantyId: Int!, $status: String!, $serialNumber: String!) {
            createComponentmetainfo(input : {
              manufacturerId: $manufacturerId,
              warrantyId: $warrantyId,
              status: $status,
              serialNumber: $serialNumber
            }) {
              componentmetainfo {
                id
              }
            }
          }
        `,
        variables: {
          manufacturerId: Number(this.formData.manufacturerId),
          warrantyId: Number(this.formData.warrantyId),
          status: this.formData.status,
          serialNumber: this.formData.serialNumber,
        }
      })
      componentMetaInfoId = componentMetaInfoId.data.createComponentmetainfo.componentmetainfo.id;

      const result = await this.$apollo.mutate({
        mutation: gql`
          mutation ($cores: Int!, $l1Cache: Int!, $l2Cache: Int!, $l3Cache: Int!, $componentMetaInfoId: Int!) {
            createProcessor(input: {
              cores: $cores,
l1Cache: $l1Cache,
l2Cache: $l2Cache,
l3Cache: $l3Cache,
componentMetaInfoId: $componentMetaInfoId
            }) {
              processor {
                id
              }    
            }
          }
        `,
        variables: {
          cores: Number(this.formData.cores),
l1Cache: Number(this.formData.l1Cache),
l2Cache: Number(this.formData.l2Cache),
l3Cache: Number(this.formData.l3Cache),
componentMetaInfoId: Number(componentMetaInfoId)
        }
      });
    }
  },
  apollo: {
    processors: gql`
      query {
      processors {
          
          componentMetaInfo {
            serialNumber,
            manufacturerId,
            warrantyId,
            status
          }

          id,
          cores,
l1Cache,
l2Cache,
l3Cache,
componentMetaInfoId
        }
      }
    `,
    
    manufacturers: gql`
      query {
        manufacturers {
          id,
          title
        }
      }
    `,

    
    warrantys: gql`
      query {
        warrantys {
          id,
          startDate,
          endDate
        }
      }
    `,

  }
}
</script>

<style scoped>
</style>
