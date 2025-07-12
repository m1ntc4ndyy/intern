<script setup>
    import { ref, onMounted } from 'vue'
    import { useTodos } from '@/composables/useTodos'
    
    const newTodo = ref("")
    const newDesc = ref("")
    const { todos, fetchTodos, addTodo, toggleTodo, deleteTodo } = useTodos()
    
    onMounted(fetchTodos)
    
    const add = async () => {
    if (newTodo.value.trim()) {
        await addTodo(newTodo.value, newDesc.value)
        newTodo.value = ""
        newDesc.value = ""
    }
    }
    
    const toggle = (todo) => toggleTodo(todo)
    const remove = (id) => deleteTodo(id)
</script>
<template>
  <div class="min-h-screen bg-gray-50 py-10">
    <div class="max-w-xl mx-auto bg-white rounded-xl shadow p-8">
      <header class="flex justify-between items-center mb-6">
        <h1 class="text-2xl font-bold">My Todos</h1>
      </header>

      <div class="space-y-2 mb-4">
        <input v-model="newTodo" placeholder="Title"
               class="w-full border rounded p-2" />
        <textarea v-model="newDesc" placeholder="Description (optional)"
               class="w-full border rounded p-2"></textarea>
        <button @click="add"
                class="w-full bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700">
          Add Todo
        </button>
      </div>

      <ul v-if="todos.length" class="space-y-2">
        <li v-for="todo in todos" :key="todo.id"
            class="border-b pb-2">
          <div class="flex justify-between items-center">
            <div @click="toggle(todo)" class="cursor-pointer">
              <h2 :class="{ 'line-through text-gray-400': todo.completed }"
                  class="font-semibold">
                {{ todo.title }}
              </h2>
              <p class="text-sm text-gray-600">{{ todo.description }}</p>
            </div>
            <button @click="remove(todo.id)" class="text-red-500 hover:cursor-pointer transition-transform hover:scale-120">X</button>
          </div>
        </li>
      </ul>

      <p v-else class="text-gray-500 text-center">No todos yet 🙌</p>
    </div>
  </div>
</template>

