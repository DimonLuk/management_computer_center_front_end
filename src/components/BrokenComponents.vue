<template>
  <v-container fluid>
    <v-layout>
      <v-flex>
        <v-card
          v-for='value in components'
          v-if='value.componentMetaInfo.status === "Broken"'
          style='margin-bottom: 15px;'
        >
          <v-card-title
            primary-title
          >
            <div>
              <h3 class="headline mb-0" style='text-align:left'>Type: {{ value.__typename.slice(0, -4) }}</h3>
              <div
                v-for='(v, k) in value'
                v-if='k[0] !== "_" && k !== "componentMetaInfo"'
                style='text-align: left;'
              >
                {{ k }}: {{ v }}
              </div>
              <div
                style='text-align: left;'  
              >
                Serial Number: {{ value.componentMetaInfo.serialNumber }}
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
  name: 'BrokenComponents',
  data() {
    return {
      components: [],
    };
  },
  mounted() {
    this.$apollo.queries.rams.skip = false;
    this.$apollo.queries.trunks.skip = false;
    this.$apollo.queries.motherboards.skip = false;
    this.$apollo.queries.processors.skip = false;
    this.$apollo.queries.rams.refetch();
    this.$apollo.queries.trunks.refetch();
    this.$apollo.queries.motherboards.refetch();
    this.$apollo.queries.processors.refetch();
    this.components = [...this.rams, ...this.motherboards, ...this.processors, ...this.trunks];
  },
  apollo: {
    rams: {
      query: gql`
        query {
        rams {
            id,
            capacity,
            frequency,
            componentMetaInfo {
              status,
              serialNumber
            }
          }
        }
      `,
      skip() {
        return true;
      }
    },
    motherboards: {
      query: gql`
        query {
        motherboards {
            id,
            formFactor,
            chipset,
            pciSlots,
            usedPciSlots,
            ramSlots,
            usedRamSlots,
            componentMetaInfo {
              status,
              serialNumber
            }
          }
        }
      `,
      skip() {
        return true;
      }
    },
    processors: {
      query: gql`
        query {
        processors {
            id,
            cores,
            l1Cache,
            l2Cache,
            l3Cache,
            componentMetaInfo {
              status,
              serialNumber
            }
          }
        }
      `,
      skip() {
        return true;
      }
    },
    trunks: {
      query: gql`
        query {
          trunks {
            id,
            width,
            height,
            formFactor,
            componentMetaInfoId
            componentMetaInfo {
              status,
              serialNumber
            }
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
