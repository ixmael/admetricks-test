<script setup lang="ts">
import { watch, toRef } from 'vue';
import * as d3 from 'd3';

const props = defineProps({
    data: Array<any>,
});

const data = toRef(props, 'data');

watch(
    data,
    (newData, _) => {
        updateGraph(newData);
    })

// Update the graph
const updateGraph = (aapl: Array<any>) => {
    if (aapl.length > 0) {
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
        const x = d3.scaleTime(<[Date, Date]>d3.extent(aapl, (d: any) => new Date(d.date)), [marginLeft, width - marginRight]);

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
    }
};
</script>

<template>
    <div class="linear-graph">
        <svg id="chart" width="0" height="0"></svg>
        <div class="no-data" v-if="data.length === 0">No hay datos para graficar</div>
    </div>
</template>

<style lang="scss">
.linear-graph {
    & .no-data {
        color: #e11c1c;
        text-align: center;
        font-weight: bold;
        text-transform: uppercase;
    }
}
</style>
