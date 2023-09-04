<script setup lang="ts">
const props = defineProps({
    date: Array<Date>,
});

const downloadFile = async () => {
    // Prepare the from-to range
    const from = `${props.date[0].getFullYear()}-${props.date[0].getMonth() + 1}-${props.date[0].getDate()}`;
    const to = `${props.date[1].getFullYear()}-${props.date[1].getMonth() + 1}-${props.date[1].getDate()}`;

    // Prepare the query
    const searchParams = new URLSearchParams({ from, to });
    const request = new Request(`${import.meta.env.VITE_REST_API}/document?${searchParams.toString()}`);
    const response = await fetch(request);

    if (response.status) {
        const text = await response.text();
        const blob = new Blob([text], { type: 'application/csv' });

        const today = new Date();

        const fromLabel = `${props.date[0].getFullYear()}${String(props.date[0].getMonth() + 1).padStart(2, '0')}${String(props.date[0].getDate()).padStart(2, '0')}`;
        const toLabel = `${props.date[1].getFullYear()}${String(props.date[1].getMonth() + 1).padStart(2, '0')}${String(props.date[1].getDate()).padStart(2, '0')}`;

        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = `admetricks_${today.getTime()}_${fromLabel}-${toLabel}.csv`;
        link.click();
        URL.revokeObjectURL(link.href);
    }
}
</script>

<template>
    <button class="download-file" @click="downloadFile">
        descargar csv
    </button>
</template>

<style lang="scss">
.download-file {}
</style>
