<script setup>
import { ref, watch } from 'vue'

const todoData = ref(null)
const choices = ['todos', 'users', 'posts', 'comments']
const limit = ref(10)
const fetchChoice = ref(choices[0])
const page = ref(1)

async function fetchData() {
  todoData.value = null
  const res = await fetch(
    `https://jsonplaceholder.typicode.com/${fetchChoice.value}?_page=${page.value}&_limit=${limit.value}`
  )
  todoData.value = await res.json()
}

watch([fetchChoice, limit, page], fetchData)

fetchData()
</script>

<template>
  <div class="container">
    <p>Fetch type:</p>
    <select v-model="fetchChoice">
      <option v-for="choice in choices" :key="choice" :value="choice">{{ choice }}</option>
    </select>

    <p>Limit:</p>
    <input type="number" v-model="limit" min="1" />

    <p>Page:</p>
    <input type="number" v-model="page" min="1" />

    <button @click="page--" :disabled="page <= 1">Previous</button>
    <button @click="page++">Next</button>

    <p v-if="!todoData">Loading...</p>
    <pre v-else>{{ todoData }}</pre>
  </div>
</template>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #eee;
  border-radius: 5px;
  background-color: #f9f9f9;
}

h2 {
  text-align: center;
}

button {
  margin: 5px;
}
</style>