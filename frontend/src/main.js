import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
// import axios from 'axios'

const vuetify = createVuetify({
  components,
  directives,
});

import './assets/main.css'

const app = createApp(App)
// axios.defaults.baseURL = '/api'

app.use(router)
app.use(vuetify)

app.mount('#app')
