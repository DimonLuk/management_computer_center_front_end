<template>
  <v-container fluid>
    <v-layout>
      <v-flex>
        <v-card>
          <v-card-title primary-title v-for='(value, key) in groupedComputers'>
            <div>
              <h3 class="headline mb-0" style='text-align:left'>Room: {{ key }}</h3>
              <div
                style='text-align: left'
                v-for='element in value'
              >
              <div
                v-for='(v, k) in element'
                v-if='k[0] !== "_"'
              >
                {{ k }}: {{ v }}
              </div>
              </div>
            </div>
          </v-card-title>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import gql from 'graphql-tag';
import { groupBy } from 'lodash';
export default {
  name: 'ComputersPrintPage',
  data() {
    return {
      groupedComputers: {},
    };
  },
  mounted() {
    this.$apollo.queries.computers.skip = false;
    this.$apollo.queries.computers.refetch();
    this.groupComputersByRoom();
  },
  methods: {
    groupComputersByRoom() {
      this.groupedComputers = groupBy(this.computers, 'room');
    }
  },
  apollo: {
    computers: {
      query: gql`
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
      skip() {
        return true;
      }
    },
  }
}
</script>

<style>
</style>
