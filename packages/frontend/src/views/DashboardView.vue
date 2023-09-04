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
const data = ref([]);

// Graph the data
const graph = async () => {
  // Prepare the from-to range
  const from = `${date.value[0].getFullYear()}-${date.value[0].getMonth() + 1}-${date.value[0].getDate()}`;
  const to = `${date.value[1].getFullYear()}-${date.value[1].getMonth() + 1}-${date.value[1].getDate()}`;

  // Get data from the RestAPI
  data.value = await fetchData(from, to)
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
const fetchData = async (from: string, to: string): Promise<Array<any>> => {
  const searchParams = new URLSearchParams({ from, to });
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
            <VueDatePicker v-model="date" :min-date="new Date(2020, 0, 1)" :max-date="new Date()"
              :enableTimePicker="false" locale="es-MX" :format-locale="es" format="dd/MM/yyyy" range></VueDatePicker>
          </div>
          <button @click="graph">
            graficar
          </button>
          <DownloadData :date="date" />
        </div>
        <LinearGraph :data="data" />
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

  & .no-data {
    text-align: center;
  }
}
</style>
