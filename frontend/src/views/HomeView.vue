<template>
  <v-container v-if="notes.length" class="pa-2 bg-surface-variant">
    
    <v-row  no-gutters>
      <v-col
        v-for="note in notes"
        :key="note.id"
        cols="6"
        sm="4" 
      >
        <v-sheet class="ma-2 pa-2" >
          <router-link :class="note.progress" :to="{name:'detail',params:{id:note.id}}"> 
            <p v-if="note.title == ''" style="text-align: center; font-size: large;" > Title </p>
            <p v-else style="text-align: center; font-size: large;" > {{ note.title }} </p>
          </router-link>
          <label>Progress:  </label>
          <select @change.prevent="updateNote(note.id, note)" v-model="note.progress">
            <option v-for="option in options" :value="option.value">
              {{ option.text }}
            </option>
          </select> 
          <v-btn color="red-lighten-1" type="submit" @click="deleteNote(note.id, note)" block class="mt-2">Delete</v-btn>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
  <p style="font-size: 20px;" v-else>Your list is empty. Please give him new notes &#128525;</p>
  

</template>

<script setup>
import {  computed, ref } from 'vue';

const notes = ref([])
const noteId = ref('')
const props = defineProps(['time'])

const options = ref([
  { text: 'To-Do', value: 'To-do' },
  { text: 'Doing', value: 'Doing' },
  { text: 'Done', value: 'Done' }
])

const api = axios.get('http://127.0.0.1:8000/notes')
            .then(response => response)
            .then(response => {
              notes.value = response.data
            }) 

const updateNote = (id, note)=>{
      // noteUp.value = notes.value.find(note => note.id == id)
      console.log(id, note)

      axios.patch(`http://127.0.0.1:8000/notes/${id}`, note)
            .then(function (response) {
              console.log(response);
            })
}

 const deleteNote = (id)=>{
      axios.delete(`http://127.0.0.1:8000/notes/${id}`)
            .then(function (response) {
              console.log(response);
            })
        notes.value = notes.value.filter(note => note.id != id)
    }
// onMounted(() => {
//   const 
// })

// Components
</script>
<style scoped>
a{
  text-decoration: none;
  color: black;

}
.Done {
  text-decoration: line-through;
  color: #ec120b;
}

.Doing{
  color: green;
}

.select{
  width: 100px;
}
</style>
