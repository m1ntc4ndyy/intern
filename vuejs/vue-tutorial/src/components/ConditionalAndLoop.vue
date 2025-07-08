<script setup>
import { ref } from 'vue'

const show = ref(true)
const list = ref([1, 2, 3])
</script>

<template>
<div class="container">
    <button @click="show = !show">Toggle List</button>
    <button @click="list.push(list.length + 1)">Push Number</button>
    <button @click="list.pop()">Pop Number</button>
    <button @click="list.reverse()">Reverse List</button>
  
    <ul v-if="show && list.length">
      <li v-for="item of list">{{ item }}</li>
    </ul>
    <p v-else-if="list.length">List is not empty, but hidden.</p>
    <p v-else>List is empty.</p>
</div>
</template>


<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #eee;
  border-radius: 5px;
  background-color: #f9f9f9;
}

button {
  margin-right: 10px;
}
</style>