import { createRouter, createWebHistory } from 'vue-router'
import Todo from '../components/Todo.vue'
const routes = [

  {
    path: '/todo',
    name: 'Todo',
    component: Todo
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router