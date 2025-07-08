<script setup>
import { reactive, ref, watch, computed } from 'vue'
const list = reactive(['item1', 'item2', 'item3'])
const search = ref('')
const selected = ref('')
const name = ref('')

watch(selected, (item) => {
    name.value = item
})

const filteredList = computed(() => {
    console.log('Filtering list with search:', search)
    if (!search.value.trim()) {
        return list
    }
    return list.filter(item => item.toLowerCase().includes(search.value.toLowerCase()))
})

const create = () => {
    if (name.value.trim() === '') {
        alert('Name cannot be empty')
        return
    }
    list.push(name.value.trim())
    name.value = ''
}

const update = () => {
    if (selected.value === '' || name.value.trim() === '') {
        alert('Please select an item and enter a new name to update')
        return
    }
    const index = list.indexOf(selected.value)
    if (index !== -1){
        list[index] = name.value.trim()
        name.value = ''
    }
}

const del = () => {
    if (selected.value === '' ){
        alert('Please select an item to delete')
        return
    }
    const index = list.indexOf(selected.value)
    if (index !== -1) {
        list.splice(index, 1)
        selected.value = ''
    }
}

</script>

<template>
    <div class="container">
        <div>
            <input type="text" v-model="search" placeholder="Search items" />
            <button style="margin-left: 5px;" @click="search = ''">reset</button>
        </div>
        <select size="5" v-model="selected">
            <option v-for="item in filteredList" :key="item">
                {{ item }}
            </option>
        </select>
        <label>Item:
            <input type="text" v-model="name"/>
        </label>

        <div class="buttons">
            <button @click="create">Create</button>
            <button @click="update">Update</button>
            <button @click="del">Delete</button>
        </div>
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
select {
    width: 100%;
    height: 100px;
    margin-bottom: 10px;
}

option {
    padding: 3px;
    font-weight: bold;
}

.buttons {
    clear: both;
    margin-top: 10px;
}
button {
    margin-right: 10px;
    padding: 5px 10px;
    background-color: #42b983;
    color: white;
    border: none;
    border-radius: 3px;
    cursor: pointer;
}
</style>