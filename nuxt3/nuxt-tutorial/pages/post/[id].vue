<script setup>
const route = useRoute()
const { data } = await useFetch(`https://jsonplaceholder.typicode.com/posts/${route.params.id}`)
console.log(route.params.id)
</script>
<template>
    <div class="container mx-auto p-4">
        <span class=" text-3xl">Title</span>
        <h1 class="text-2xl font-bold mb-4">{{ data.title }}</h1>
        <span class="text-3xl">Body</span>
        <p>{{ data.body }}</p>
    </div>
</template>