<script setup lang="ts">
import { ref, computed } from 'vue'
interface Todo {
  id: number
  text: string
  status: boolean
}
let id = 0
const newTodo = ref('')
const todos = ref<Todo[]>([])
const hideCompleted = ref(false)

const addTodo = () => {
  todos.value.push({
    id: id++,
    text: newTodo.value,
    status: false
  })
  newTodo.value = ''
}

const deleteTodo = (id: number) => {
  todos.value = todos.value.filter(item => item.id !== id)
  
}
const filteredTodos = computed(() => {
  return hideCompleted.value ? todos.value.filter(todo => !todo.status) : todos.value
})
</script>

<template>
  <div class="container">
    <form @submit.prevent="addTodo">
      <input type="text" v-model="newTodo" placeholder="Add a new todo" required />
      <button type="submit">Add</button>
    </form>
    <br />
    <ul>
      <li v-for="todo in filteredTodos" :key="todo.id">
        <input type="checkbox" v-model="todo.status" />
        <span :class="{'todo-text': todo.status}">{{ todo.text }}</span>
        <button @click="deleteTodo(todo.id)">X</button>
        <br />
      </li>
    </ul>

    <button @click="hideCompleted = !hideCompleted">
      {{ hideCompleted ? "Show all" : "Hide Completed" }}
    </button>
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 2rem;
  background-color: #f9f9f9;
}

h1 {
  font-size: 2rem;
  margin-top: 1rem;
}

span {
  margin: 0 5px;
  font-size: large;
}
.todo-text {
  text-decoration: line-through;
  color: gray;
}
</style>
