import { ref } from 'vue'

const API = 'http://localhost:8000/api/todos/'

export function useTodos() {
  const todos = ref([])
  const loading = ref(false)

  const fetchTodos = async () => {
    loading.value = true
    const res = await fetch(API)
    todos.value = await res.json()
    loading.value = false
  }

  const addTodo = async (title: string, description: string) => {
    await fetch(API, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, description, completed: false })
    })
    await fetchTodos()
  }

  const toggleTodo = async (todo: any) => {
    await fetch(`${API}${todo.id}/`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ...todo, completed: !todo.completed })
    })
    await fetchTodos()
  }

  const deleteTodo = async (id: number) => {
    await fetch(`${API}${id}/`, {
      method: 'DELETE'
    })
    await fetchTodos()
  }

  return { todos, loading, fetchTodos, addTodo, toggleTodo, deleteTodo }
}
