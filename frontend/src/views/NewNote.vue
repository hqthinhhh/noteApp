<template>
  <v-sheet width="500" class="mx-auto">
    <v-form fast-fail @submit.prevent>
      <v-text-field
        v-model="notes.title"
        label="Title"
      ></v-text-field>

      <v-textarea
        
        label="Description"
        v-model="notes.description"
      ></v-textarea>

       <label>Progress: </label>
      <select v-model="notes.progress">
        <option v-for="option in options" :value="option.value">
          {{ option.text }}
        </option>
      </select>
     
      <label style="margin-left: 50px;"> Deadline:</label>
      <input type="date"
      v-model="notes.deadline" 
       >

      <v-btn  @click="test" type="submit" block class="mt-2">New Note </v-btn>
      <router-link v-if="noteId != ''" :to="`/detail/${noteId}`"> <v-btn block class="mt-2">Edit Note </v-btn> </router-link>
    </v-form>
  </v-sheet>
</template>

<script>
import {  ref, computed } from 'vue';

  export default {
    setup(){
      const notes = ref({title: '', description: '', deadline: '', progress: ''})
      const noteId = ref('')
      const options = ref([
        { text: 'To-Do', value: 'To-do' },
        { text: 'Doing', value: 'Doing' },
        { text: 'Done', value: 'Done' }
      ])

      const test = async ()=>{
        await axios.post(`https://be.thinh.com/notes`, notes.value )
              .then(function (response) {
                noteId.value = response.data.id;
                console.log(noteId.value)
              })
      }
      
      return {notes,options, noteId, test,}
    }
  }
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
