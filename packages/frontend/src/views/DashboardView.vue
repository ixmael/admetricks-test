<script setup lang="ts">
import { onMounted } from 'vue';
import * as d3 from 'd3';

let aapl = [];

onMounted(async () => {

  aapl = await fetchData()
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
      console.log('error', err);
      return [];
    });

  console.log('appl', aapl);

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
      .text("Precio ($)"));

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
});

const fetchData = async (): Promise<Array<any>> => {
  const searchParams = new URLSearchParams({
    from: '2023-01-01',
    to: '2023-01-20',
  });
  const request = new Request(`${import.meta.env.VITE_REST_API}?${searchParams.toString()}`);
  

  const response = await fetch(request);

  if (response.status) {
    const data = await response.json();
    return Promise.resolve(data);
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
          <div class="initial-date">inicio</div>
          <div class="final-date">fin</div>
          <div>shortcuts</div>
        </div>
        <svg id="chart"></svg>
      </div>
    </div>
  </main>
</template>

<style lang="scss">
main {
  display: flex;
  justify-content: center;

  & .dashboard {
    background-color: #fff;
    padding: 0 15px;
    width: 800px;
  }

  & .filters {
    display: flex;

    & .initial-date {
      background-color: red;
    }

    & .final-date {
      background-color: aliceblue;
    }
  }
}
</style>
