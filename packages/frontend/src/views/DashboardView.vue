<script setup lang="ts">
import { ref } from 'vue';

import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';
import { es } from 'date-fns/locale';

import LinearGraph from '../components/LinearGraph.vue';
import DownloadData from '../components/DownloadData.vue';

// Setup data
const date = ref([
  new Date(new Date().setDate(new Date().getDate() - 7)),
  new Date(),
]);

// Default data
const data = ref([] as Array<any>);

// Graph the data
const graph = async () => {
  // Get data from the RestAPI
  data.value = await fetchData(date.value[0], date.value[1])
    .then(data => data.sort((a, b) => {
      // Sort by date
      const dateA = new Date(a.date);
      const dateB = new Date(b.date);
      if (dateA < dateB) {
        return -1;
      } else if (dateA > dateB) {
        return 1;
      }

      return 0;
    }))
    .catch(err => {
      console.error('error', err);
      return [];
    });
};

// Get the data of the API
const fetchData = async (from: Date | null, to: Date | null): Promise<Array<any>> => {
  const filters: any = {};

  // Prepare the from-to range
  if (from) {
    filters.from = `${from.getFullYear()}-${from.getMonth() + 1}-${from.getDate()}`
  }
  if (to) {
    filters.to = `${to.getFullYear()}-${to.getMonth() + 1}-${to.getDate()}`;
  }

  const searchParams = new URLSearchParams(filters);
  const request = new Request(`${import.meta.env.VITE_REST_API}?${searchParams.toString()}`);
  const response = await fetch(request);

  if (response.status) {
    const dataFromAPI = await response.json();
    return Promise.resolve(dataFromAPI);
  }

  return Promise.resolve([]);
};
</script>

<template>
  <main>
    <div class="dashboard">
      <h1>dashboard</h1>
      <div class="chart">
        <div class="filters">
          <div>
            <VueDatePicker class="datepicker" v-model="date" :min-date="new Date(2020, 0, 1)" :max-date="new Date()"
              :enableTimePicker="false" locale="es-MX" :format-locale="es" format="dd/MM/yyyy" range></VueDatePicker>
          </div>
          <button class="graph" @click="graph">
            Obtener datos
          </button>
          <DownloadData class="download" :date="date" />
        </div>
        <LinearGraph class="linear-graph" :data="data" />
      </div>
    </div>
  </main>
</template>

<style lang="scss">
main {
  display: flex;
  justify-content: center;

  & h1 {
    font-size: 2rem;
    font-weight: bold;
    text-align: center;
    text-transform: uppercase;
    padding: 1rem 0;
  }

  & .dashboard {
    background-color: #fff;
    padding: 0 15px;
    width: 800px;
    padding-bottom: 1rem;
  }

  & .filters {
    display: flex;
    justify-content: center;
    margin-bottom: 1rem;

    &>* {
      margin-right: 5px;
    }

    &>button {
      text-transform: uppercase;
    }
  }
}
</style>
