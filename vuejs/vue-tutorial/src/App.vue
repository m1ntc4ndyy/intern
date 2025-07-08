<template>
  <div id="app">
    <nav>
      <router-link to="/todo">Todo</router-link>
      <router-link to="/conditional">Conditional and Loop</router-link>
      <router-link to="/crud">CRUD</router-link>
      <router-link to="/form">Form</router-link>
      <router-link to="/fetch">Fetch</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script setup lang="ts">
</script>

<style>
nav {
  margin-bottom: 20px;
  padding: 10px;
  background-color: #f8f9fa;  
  border-bottom: 1px solid #dee2e6;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: Arial, sans-serif;
  font-size: 16px;
}

nav a {
  margin-right: 15px;
  text-decoration: none;
  color: #42b983;
}
nav a:hover {
  text-decoration: underline;
}


nav a.router-link-exact-active {
  font-weight: bold;
}
</style>