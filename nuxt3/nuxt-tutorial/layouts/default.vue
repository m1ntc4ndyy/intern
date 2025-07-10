<template>
    <nav class="bg-gray-800 p-4 text-white flex justify-center space-x-4">
          <NuxtLink to="/">Home</NuxtLink>
          <NuxtLink to="/about">About</NuxtLink>
          <NuxtLink to="/post">Posts</NuxtLink>
    </nav>
    <slot />
</template>