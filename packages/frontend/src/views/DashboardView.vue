<script setup lang="ts">
import { ref, onMounted } from 'vue';
import * as d3 from 'd3';

import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';
import { es } from 'date-fns/locale';

const date = ref();
const noData = ref(true);

onMounted(async () => {
  const endDate = new Date();
  const startDate = new Date(new Date().setDate(endDate.getDate() - 7))

  date.value = [startDate, endDate];
});

// Graph the data
const graph = async () => {
  // Prepare the from-to range
  const from = `${date.value[0].getFullYear()}-${date.value[0].getMonth() + 1}-${date.value[0].getDate()}`;
  const to = `${date.value[1].getFullYear()}-${date.value[1].getMonth() + 1}-${date.value[1].getDate()}`;

  const data = await fetchData(from, to)
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

  updateGraph(data);
};

const downloadFile = async () => {
  // Prepare the from-to range
  const from = `${date.value[0].getFullYear()}-${date.value[0].getMonth() + 1}-${date.value[0].getDate()}`;
  const to = `${date.value[1].getFullYear()}-${date.value[1].getMonth() + 1}-${date.value[1].getDate()}`;

  // Prepare the query
  const searchParams = new URLSearchParams({ from, to });
  const request = new Request(`${import.meta.env.VITE_REST_API}/document?${searchParams.toString()}`);
  const response = await fetch(request);

  if (response.status) {
    const text = await response.text();
    const blob = new Blob([text], { type: 'application/csv' });

    const today = new Date();

    const fromLabel = `${date.value[0].getFullYear()}${String(date.value[0].getMonth() + 1).padStart(2, '0')}${String(date.value[0].getDate()).padStart(2, '0')}`;
    const toLabel = `${date.value[1].getFullYear()}${String(date.value[1].getMonth() + 1).padStart(2, '0')}${String(date.value[1].getDate()).padStart(2, '0')}`;

    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = `admetricks_${today.getTime()}_${fromLabel}-${toLabel}.csv`;
    link.click();
    URL.revokeObjectURL(link.href);
  }
}

// Get the data of the API
const fetchData = async (from: string, to: string): Promise<Array<any>> => {
  const searchParams = new URLSearchParams({ from, to });
  const request = new Request(`${import.meta.env.VITE_REST_API}?${searchParams.toString()}`);
  const response = await fetch(request);

  if (response.status) {
    const data = await response.json();
    return Promise.resolve(data);
  }

  return Promise.resolve([]);
};

// Update the graph
const updateGraph = (aapl: Array<any>) => {
  if (aapl.length > 0) {
    noData.value = false;

    const width = 928;
    const height = 500;
    const marginTop = 20;
    const marginRight = 30;
    const marginBottom = 30;
    const marginLeft = 40;

    const svg = d3
      .select('svg#chart')
      .attr('width', width)
      .attr('height', height)
      .attr("viewBox", [0, 0, width, height])
      .attr("style", "max-width: 100%; height: auto; height: intrinsic;");

    svg.selectAll('*').remove();

    // Declare the x (horizontal position) scale.
    const x = d3.scaleTime(d3.extent(aapl, (d: any) => new Date(d.date)), [marginLeft, width - marginRight]);

    // Declare the y (vertical position) scale.
    const y = d3.scaleLinear([0, d3.max(aapl, (d: any) => {
      return d.close;
    })], [height - marginBottom, marginTop]);

    // Declare the line generator.
    const line = d3.line()
      .x((d: any) => x(new Date(d.date)))
      .y((d: any) => y(d.close));

    // Add the x-axis.
    svg.append("g")
      .attr("transform", `translate(0,${height - marginBottom})`)
      .call(d3.axisBottom(x).ticks(width / 80).tickSizeOuter(0));

    // Add the y-axis, remove the domain line, add grid lines and a label.
    svg.append("g")
      .attr("transform", `translate(${marginLeft},0)`)
      .call(d3.axisLeft(y).ticks(height / 40))
      .call((g: any) => g.select(".domain").remove())
      .call((g: any) => g.selectAll(".tick line").clone()
        .attr("x2", width - marginLeft - marginRight)
        .attr("stroke-opacity", 0.1))
      .call((g: any) => g.append("text")
        .attr("x", -marginLeft)
        .attr("y", 10)
        .attr("fill", "currentColor")
        .attr("text-anchor", "start")
        .text("Pesos Chilenos ($)"));

    // Append a path for the line.
    svg.append("path")
      .attr("fill", "none")
      .attr("stroke", "#550080")
      .attr("stroke-width", 1)
      .style("opacity", 0.5)
      .attr("d", line(aapl));

    svg.selectAll('circle')
      .data(aapl)
      .enter()
      .append("circle")
      .attr("class", "dot")
      .attr("r", 2)
      .attr("cx", function (d) {
        return x(new Date(d.date));
      })
      .attr("cy", function (d) {
        return y(d.close)
      })
      .style("fill", function (d) {
        return '#550080';
      })
      .style("opacity", 1);
  } else {
    noData.value = true;
  }
};
</script>

<template>
  <main>
    <div class="dashboard">
      <h1>dashboard</h1>
      <div class="chart">
        <div class="filters">
          <div>
            <VueDatePicker v-model="date" :min-date="new Date(2020, 0, 1)" :max-date="new Date()" :enableTimePicker="false" locale="es-MX"
              :format-locale="es" format="dd/MM/yyyy" range></VueDatePicker>
          </div>
          <button @click="graph">
            graficar
          </button>
          <button @click="downloadFile">
            descargar csv
          </button>
        </div>
        <div class="no-data" v-if="noData">No ha seleccionadon un rango para graficar.</div>
        <svg id="chart"></svg>
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
