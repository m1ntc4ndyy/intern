<script setup>
import { ref, watch } from 'vue'

const todoData = ref(null)
const limit = ref(10)
const page = ref(1)


async function fetchData() {
  todoData.value = null
  const res = await fetch(
    `https://jsonplaceholder.typicode.com/posts?_page=${page.value}&_limit=${limit.value}`
  )
  todoData.value = await res.json()
}

watch([limit, page], fetchData)

fetchData()

</script>

<template>
  <div class="container mx-auto p-6 bg-gray-100 rounded-lg shadow-md">
    <h1 class="text-2xl font-bold text-center mb-6">Fetch Data</h1>

    <div class="mb-4">
      <label class="block text-gray-700 font-medium mb-2">Limit:</label>
      <input
        type="number"
        v-model="limit"
        min="1"
        class="w-full p-2 border rounded-md"
      />
    </div>

    <div class="mb-4">
      <label class="block text-gray-700 font-medium mb-2">Page:</label>
      <input
        type="number"
        v-model="page"
        min="1"
        class="w-full p-2 border rounded-md"
      />
    </div>

    <div class="flex justify-between mb-6">
      <button
        @click="page--"
        :disabled="page <= 1"
        class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 disabled:bg-gray-300"
      >
        Previous
      </button>
      <button
        @click="page++"
        class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
      >
        Next
      </button>
    </div>

    <div v-if="!todoData" class="text-center text-gray-500">
      Loading...
    </div>
    <ul v-else class="space-y-4">
      <li
        v-for="item in todoData"
        :key="item.id"
        class="p-4 bg-white rounded-md shadow-md cursor-pointer hover:bg-gray-100"
      >
        <NuxtLink :to="`/post/${item.id}`" class="text-blue-500 hover:underline">
          <p class="font-medium text-gray-800">ID: {{ item.id }}</p>
          <p class="text-gray-600">{{ item.title || item.name }}</p>
        </NuxtLink>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.container {
  max-width: 800px;
}
</style>