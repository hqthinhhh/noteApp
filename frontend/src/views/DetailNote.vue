<template>
  <v-sheet v-cloak v-if="state == true" width="500" class="mx-auto">
    <v-form v-for="note in notes" fast-fail @submit.prevent="updateNote">
      <v-text-field
        v-model="note.title"
        label="Title"
        @change.prevent="updateNote"
      ></v-text-field>

      <v-textarea
        
        label="Description"
        v-model="note.description"
        @change.prevent="updateNote"
      ></v-textarea>

      <label>Progress: </label>
      <select @change.prevent="updateNote" v-model="note.progress">
        <option v-for="option in options" :value="option.value">
          {{ option.text }}
        </option>
      </select>
     
      <label style="margin-left: 50px;"> Deadline:</label>
      <input type="date"
      v-model="note.deadline" 
      @change.prevent="updateNote" >
      
      <!-- <v-btn type="submit" @submit.prevent="updateNote" block class="mt-2">Save </v-btn> -->
      <v-btn color="red-lighten-1" type="submit" @click="deleteNote" block class="mt-2">Delete</v-btn>
    </v-form>
  </v-sheet>
  <p v-else> Note is deleted. Please add New Note or back to Home page</p>
</template>

<script>
import {  ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';

export default {

  setup(){
    const notes = ref([])
    const router = useRouter()
    const route = useRoute()
    const noteId = route.params.id
    const state = ref(true)
    
  
  const options = ref([
  { text: 'To-Do', value: 'To-do' },
  { text: 'Doing', value: 'Doing' },
  { text: 'Done', value: 'Done' }
])

    const updateNote = ()=>{
      console.log(noteUpdate.value)
      axios.patch(`https://be.thinh/notes/${noteId}`, noteUpdate.value)
            .then(function (response) {
              console.log(response);
            })
    }

    const deleteNote = ()=>{
      axios.delete(`https://be.thinh.com/notes/${noteId}`)
            .then(function (response) {
              console.log(response);
            })
            state.value = false
    }
    axios.get(`https://be.thinh.com/notes/${noteId}`)
          .then(response => response)
          .then(response => {
            notes.value = response.data
          }) 

    const noteUpdate = computed(()=>{
      return [...notes.value].shift()
    })
    const select = ref({ state: 'To-do', abbr: noteUpdate.progress })
    
    return {notes,state,select,options, deleteNote, updateNote, noteUpdate}
    
  }
  
  // created() {
  // axios.get('http://127.0.0.1:8000/notes')
  //             .then(response => response)
  //             .then(response => {
  //               this.notes = response.data
  //             }) 
  // },
}
</script>

<style scoped>
@media (min-width: 1024px) {

}
  [v-cloak]{
    display: none;
  }
</style>
