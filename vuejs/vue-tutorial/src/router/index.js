import { createRouter, createWebHistory } from 'vue-router'
import Todo from '../components/Todo.vue'
import ConditionalAndLoop from '../components/ConditionalAndLoop.vue'
import CRUD from '../components/CRUD.vue'
import Form from '../components/Form.vue'
import Fetch from '../components/Fetch.vue'
const routes = [

  {
    path: '/todo',
    name: 'Todo',
    component: Todo
  },
  {
    path: '/conditional',
    name: 'ConditionalAndLoop',
    component: ConditionalAndLoop
  },
  {
    path: '/crud',
    name: 'CRUD',
    component: CRUD
  },
  {
    path: '/form',
    name: 'Form',
    component: Form
  },
  {
    path: '/fetch',
    name: 'Fetch',
    component: Fetch
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router