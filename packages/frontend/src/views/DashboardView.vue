<script setup lang="ts">
import * as d3 from 'd3'

const width = 800;
const height = 500;
const svg = d3.select("svg").attr("width", width).attr("height", height);
const g = svg.append("g");
</script>

<template>
  <div class="dashboard">
    dashboard
    <div>
      <svg></svg>
    </div>
  </div>
</template>

<style lang="scss">
</style>
