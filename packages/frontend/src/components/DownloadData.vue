<script setup lang="ts">
const props = defineProps({
    date: Array<Date>,
});

const downloadFile = async () => {
    const filters: any = {
        from: '',
        to: '',
    };

    // Prepare the from-to range
    if (props.date[0]) {
        filters.from = `${props.date[0].getFullYear()}-${props.date[0].getMonth() + 1}-${props.date[0].getDate()}`
    }
    if (props.date[1]) {
        filters.to = `${props.date[1].getFullYear()}-${props.date[1].getMonth() + 1}-${props.date[1].getDate()}`;
    }

    // Prepare the query
    const searchParams = new URLSearchParams(filters);
    const request = new Request(`${import.meta.env.VITE_REST_API}/document?${searchParams.toString()}`);
    const response = await fetch(request);

    if (response.status) {
        const text = await response.text();
        const blob = new Blob([text], { type: 'application/csv' });

        const today = new Date();

        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = `admetricks_${today.getTime()}_${filters.from}-${filters.to}.csv`;
        link.click();
        URL.revokeObjectURL(link.href);
    }
}
</script>

<template>
    <button class="download-file" @click="downloadFile">
        Descargar en formato Excel
    </button>
</template>

<style lang="scss">
.download-file {}
</style>
