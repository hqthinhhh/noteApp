<template>
  <v-card>
    <v-layout>
      <v-navigation-drawer
        expand-on-hover
        rail
      >
        <v-list>
          <v-list-item
            prepend-avatar="https://scontent.fhan2-5.fna.fbcdn.net/v/t39.30808-6/310761643_3377412469153813_5266504739968298039_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=iuGPogw0_58AX_xJfJg&_nc_ht=scontent.fhan2-5.fna&oh=00_AfB_0cIiHFZAYov907ftCX2nKbKvw29QvmiewjPK_z_V9A&oe=6418239E"
            title="Hoang Quoc Thinh"
            subtitle="thinhhq@gmail.com"
          ></v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list density="compact" nav>
          <!-- <router-link to="/"><v-list-item prepend-icon="mdi-view-list" title="My Lists" value="myfiles"></v-list-item></router-link> 
          <router-link :to="{name:'newnote'}"><v-list-item prepend-icon="mdi-view-list" title="New Note" value="myfiles"></v-list-item></router-link>  -->

        </v-list>
      </v-navigation-drawer>

      <v-main style="height: 60px"> </v-main>
    </v-layout>
  </v-card>
</template>

<script>
  export default {
    //
  }
</script>
<style scoped>
a{
    text-decoration: none;
}
</style>