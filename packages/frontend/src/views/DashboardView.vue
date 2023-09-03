<script setup lang="ts">
import { onMounted } from 'vue';
import * as d3 from 'd3';

const aapl = [
  {
    date: 1,
    close: 93.24
  },
  {
    date: 2,
    close: 94.35
  },
  {
    date: 3,
    close: 98.84
  },
  {
    date: 4,
    close: 70,
  },
];

onMounted(() => {
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
  // const x = d3.scaleUtc(d3.extent(aapl, (d: any) => d.date), [marginLeft, width - marginRight]);
  const x = d3.scaleLinear(d3.extent(aapl, (d: any) => {
    //const x = d3.scaleUtc(d3.extent(aapl, (d: any) => {
    return d.date;
  }), [marginLeft, width - marginRight]);

  // Declare the y (vertical position) scale.
  // const y = d3.scaleLinear([0, d3.max(aapl, (d: any) => d.close)], [height - marginBottom, marginTop]);
  const y = d3.scaleLinear([0, d3.max(aapl, (d: any) => {
    return d.close;
  })], [height - marginBottom, marginTop]);

  // Declare the line generator.
  const line = d3.line()
    .x((d: any) => {
      return x(d.date);
    })
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
      .text("Monto ($)"));

  // Append a path for the line.
  console.log('aapl', line(aapl));
  svg.append("path")
    .attr("fill", "none")
    .attr("stroke", "steelblue")
    .attr("stroke-width", 1.5)
    .attr("d", line(aapl));
});
</script>

<template>
  <main>
    <div class="dashboard">
      <h1>dashboard</h1>
      <div class="chart">
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
}
</style>
