#  π±π»κ΄ν΅ νλ‘μ νΈ 10- μμκ΅

## β¨ Vueλ₯Ό νμ©ν  SPA κ΅¬μ±

### π μ΄ν

#### 	π±βπ€ μ νΈμ 

> μ€λμ λ§μ§λ§ κ΄ν΅ νλ‘μ νΈλ€. λ€μμ£Ό μ΅μ’ νλ‘μ νΈλ λ¨μμμΌλ λ±ν λ§μ§λ§μ΄λΌλ κΈ°λΆμ μλ λ€. μ€λ μ‘°μ΄λ¦μ μ§μλλ° μνν+ μμκ΅(λκ°μ€λ§μ§) μ΄ ν©μ³μ Έ  μμνμ§λ§ κ΅μ₯ν΄ λΌλ λ»μΌλ‘ 'μμκ΅'μ΄λ€.π μ΄λ¦μ μ΄λ κ² μ§μΌλ λ μ΄μ¬ν ν΄μΌν  κ² κ°μ κΈ°λΆμ΄ λ€μλ€. μ€λμ Vue κ³Όλͺ©μμ λ°°μ΄ κ±Έ λ€ μ¨λ¨Ήμ κ² κ°λ€. routerλ vuexλ vuex-persistedstate κΉμ§!! μ€μ΅μμ κ½€ νλ€κ³  μ€λμ ν¬κ² μ΄λ €μ΄ μ μ μμλ€. λ¨μ§ μμ΄λ²λ¦° CSSλ₯Ό μ°ΎμΌλ¬ λ€λλκ²,,,νλ€μλ€. κ·Έλ¦¬κ³  RANDOMμ κ΅¬μνλ λ° λ‘μ§μ΄ λμ λ°λ‘ λ€μ΄μ€μ§ μμμ μ‘°κΈ μκ°μ΄ κ±Έλ Έλ€. κ·Έλλ λͺμ¬λκ³Ό ν¨κ» νλ λΆμ‘±ν  κ±Έ μ±μΈ μ μμλ€. μ΅μ’μ μν΄ CSS κ³΅λΆλ μμ νμ΄μ§μ’ μ°Ύμλ΄μΌκ² λ€! μ°λ¦¬μ μ»¨μμ..?

#### 	π±βπ€ μ΅λͺμ¬

>λ§μ§λ§ κ΄ν΅ νλ‘μ νΈλ₯Ό λ§μ³€λ€. μ΅μ’ νλ‘μ νΈλ₯Ό μλκ³  λ§μ§λ§μΌλ‘ μ°μ΅μ ν΄λ³Ό μ μλ νλ‘μ νΈλΌμ μμ½κΈ°λ νλ€. μ΄λ² νλ‘μ νΈλ Vueλ₯Ό μ λΆ νμ©ν  μ μλ νλ‘μ νΈμλ€. router, Vuex, lodash, axios λ± λ€μν κΈ°λ₯μ νμ©ν΄μ μν κ²μνμ λ§λ€μλ€. λ€νν λ¬Έμ μμ μκ΅¬νλ κΈ°λ₯μ λ€ κ΅¬ννκ³  λμ μκ°μ΄ μ’ λ¨μμ CSSλ₯Ό νμ©ν΄μ νμ΄μ§λ₯Ό κΎΈλ©°λ³΄μλ€. νμ§λ§ λΆνΈμ€νΈλ©κ³Ό CSSλ₯Ό ν μ§ μ’ μ§λμ κ·Έλ°μ§ κΉλ¨Ήμλ€λ... γγγ μΆκ° κΈ°λ₯μ λ§λ€λ €κ³  νλλ° μμ±μ λͺ»νκ³  κ΅¬ννλ€λ κ²λ§μΌλ‘ ννμ ν΄μΌ νλ€ γ γ  κ·Έλμ μ΅μ’ νλ‘μ νΈλ₯Ό λλΉν΄μ κ³΅λΆν΄μΌκ² λ€λ μκ°μ νλ€. μμ§ μ»¨μμ μ νμ§ λͺ»νμ§λ§ μμκ΅ νμ΄ν~~!π

### π λͺ©ν

- μν μ λ³΄λ₯Ό μ κ³΅νλ SPA μ μ

-  AJAXν΅μ κ³Ό JSON κ΅¬μ‘°μ λν μ΄ν΄
-  Single File Component κ΅¬μ‘°μ λν μ΄ν΄
-  vue-cli, vuex, vue-routerλ± νλ¬κ·ΈμΈ νμ©



### π¨κ²°κ³Ό μ¬μ§

------

#### 1. HOME

![home1](README.assets/home1.png)

![home2](README.assets/home2.png)

#### 2. RANDOM

![random2](README.assets/random2.PNG)

#### 3. MyMovieList

![list](README.assets/list.PNG)



###   β λ¨κ³λ³ κ΅¬ν κ³Όμ 

#### 1. router

- index.js

  ```js
  import Vue from 'vue'
  import VueRouter from 'vue-router'
  import Home from '../views/Home.vue'
  import Random from '../views/Random.vue'
  import MyMovieList from '../views/MyMovieList.vue'
  
  
  Vue.use(VueRouter)
  
  const routes = [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path:'/random',
      name:'Random',
      component:Random
  
    },
    {
      path:'/my-movie-list',
      name:'MyMovieList',
      component:MyMovieList
    }
  ]
  
  const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
  })
  
  export default router
  ```
  
  

------

#### 2. store

- index.js

  ```js
  import Vue from 'vue'
  import Vuex from 'vuex'
  import axios from 'axios'
  
  import createPersistedState from 'vuex-persistedstate'
  
  Vue.use(Vuex)
  
  export default new Vuex.Store({
    plugins:[
      createPersistedState()
    ],
    state: {
      movieCards:[],
      myMovies:[],
    },
    mutations: {
      LOAD_MOVIE_CARDS:function(state,results){
        state.movieCards=results
      },
      CREATE_LIST:function(state,movie){
        state.myMovies.push(movie)
      },
      DELETE_MOVIE:function(state,movie){
        const index=state.myMovies.indexOf(movie)
        state.myMovies.splice(index,1)
      },
      UPDATE_MOVIE:function(state,movie){
        state.myMovies=state.myMovies.map(myMovie=>{
          if(myMovie==movie){
            return{
              ...myMovie,
              isWatched:!movie.isWatched
            }
          }else{
            return myMovie
          }
        })
      }
    },
    actions: {
      LoadMovieCards:function({commit}){
        axios({
          methods:'get',
          url:'https://api.themoviedb.org/3/movie/popular',
          params:{
            api_key:'cf85387cb23102d7dcdbb033efadd2e5',
            language:'ko-kr',
          }
        })
          .then((res)=>{
            console.log(res)
            commit('LOAD_MOVIE_CARDS',res.data.results)
          })
      },
      createList:function({commit},movie){
        commit('CREATE_LIST',movie)
      },
      deleteMovie:function({commit},movie){
        commit('DELETE_MOVIE',movie)
      },
      updateMovie:function({commit},movie){
        console.log(movie)
        commit('UPDATE_MOVIE',movie)
      }
    },
    modules: {
    }
  })
  ```
  

------

#### 3. views

- Home.vue

  ```vue
  <template>
    <div class="home">
      <h1>Popular Movies</h1>
      <div>
        <b-card-group class="center-block">
          <movie-card
            v-for="movieCard in movieCards" 
            :key="movieCard.id" 
            :movieCard="movieCard">
          </movie-card>
        </b-card-group>
      </div> 
    </div>
  </template>
  
  <script>
  // @ is an alias to /src
  import MovieCard from '@/components/MovieCard.vue'
  import {mapState} from 'vuex'
  
  export default {
    name: 'Home',
    components: {
      MovieCard,
    },
    created:function(){
      this.$store.dispatch('LoadMovieCards')
    },
    computed:{
      ...mapState(['movieCards'])
    }
  }
  </script>
  ```
  
- MyMovieList

  ```vue
  <template>
    <div class="container">
      <header class="bg-sky">
        <br>
        <h1 class="text-color">My Movie List</h1>
        <my-list-form></my-list-form>
        <br>
      </header>
        <my-list></my-list>
    </div>
  </template>
  
  <script>
  import MyListForm from '@/components/MyListForm.vue'
  import MyList from '@/components/MyList.vue'
  
  export default {
    name:'MyMovieList',
    components:{
      MyListForm,
      MyList,
    }
  }
  </script>
  
  <style>
  .bg-sky{
    background-color:#2c3e50;
  }
  .text-color{
    color:honeydew;
  }
  
  </style>
  ```

- Random.vue

  ```vue
  <template>
    <div id="app">
      <h1>Pick a Movie</h1>
      <br>
      <b-button @click="showMovie">Pick!</b-button>
        <br>
        <br>
        <div >
          <b-card v-if="pickedMovie"
          :img-src="getMovieImg"
          img-alt="Movie Poster"
          imt-top
          style="max-width: 20rem;"
          class="mb-2 ms-auto me-auto"
          border-variant="dark"
          >
            <b-card-text>
              <p>{{ pickedMovie.title}}</p>
              <p>{{ pickedMovie.overview}}</p>
            </b-card-text>
          </b-card>
          <p v-else> Pick a Movie!!</p>`
        </div>
    </div>
  </template>
  
  <script>
  import {mapState} from 'vuex'
  import _ from 'lodash'
  
  export default {
    name:'Random',
    data: function () {
      return {
        pickedMovie: null,
      }
    },
    computed: {
      ...mapState([
        'movieCards'
      ]),
      getMovieImg: function () {
        const movieImg = this.pickedMovie.poster_path
        return `https://image.tmdb.org/t/p/w500/${movieImg}`
      }
    },
    methods: {
      showMovie: function () {
        this.pickedMovie = _.sample(this.movieCards)
        console.log(this.pickedMovie)
      },
    }
  }
  </script>
  ```

------

#### 4. App

- App.vue

  ```vue
  <template>
    <div id="app">
      <div class="ml-auto" >
        <b-navbar type="dark" variant="dark">
          <b-navbar-nav class="justify-content-end">
            <b-nav-item>
              <router-link to="/">Home</router-link>
            </b-nav-item>
            <b-nav-item>
              <router-link to="/random">Random</router-link> 
            </b-nav-item>
            <b-nav-item>  
              <router-link to="/my-movie-list">MyMovieList</router-link>
            </b-nav-item>
          </b-navbar-nav>
        </b-navbar>
      </div>
      <br>
      <router-view/>
    </div>
  </template>
  
  <style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    background-color:rgb(186, 213, 248)
  }
  
  #nav {
    padding: 30px;
  }
  
  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }
  
  #nav a.router-link-exact-active {
    color: #42b983;
  }
  html {
    background-color:rgb(186, 213, 248);
  }
  </style>
  
  ```

------

#### 5. components


- MovieCard.vue

  ```vue
  <template>
    <div>
      <br>
      <div class="container">
        <b-card
          :img-src="getMovieImg"
          img-alt="Movie Poster"
          imt-top
          style="max-width: 20rem;"
          class="mb-2"
          border-variant="dark"
        >
          <b-card-text>
            <p><strong>{{ movieCard.title}}</strong></p>
            <b-button v-b-toggle.overview variant="primary">μ€κ±°λ¦¬ λ³΄κΈ°</b-button>
            <b-collapse id="overview" class="collapse">
              <br>
              <p>{{ movieCard.overview }}</p>
            </b-collapse>
          </b-card-text>
        </b-card>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name:'MovieCard',
    props:{
      movieCard:Object,
    },
    computed: {
      getMovieImg: function () {
        const movieImg = this.movieCard.poster_path
        return `https://image.tmdb.org/t/p/w500/${movieImg}`
      }
    }
  }
  </script>
  ```

- MyList.vue

  ```vue
  <template>
    <div>
      <my-list-item
      v-for="myMovie in myMovies" :key="myMovie.date"
      :myMovie="myMovie"
      >
      </my-list-item>
    </div>
  </template>
  
  <script>
  import MyListItem from '@/components/MyListItem.vue'
  import {mapState} from 'vuex'
  
  export default {
    name:'MyList',
    components:{
      MyListItem
    },
    computed:{
      ...mapState(['myMovies'])
    }
  }
  </script>
  ```

- MyListForm.vue

  ```vue
  <template>
    <div>
      <input 
      type="text"
      @keyup.enter="createList"
      v-model.trim="movieTitle">
      <span>' '</span>
      <b-button @click="createList">Add</b-button>
    </div>
  </template>
  
  <script>
  export default {
    name:'MyListForm',
    data:function(){
      return{
        movieTitle:null,
      }
    },
    methods:{
      createList:function(){
        const myMovie={
          title:this.movieTitle,
          isWatched:false,
          date:new Date().getTime()
        }
        if (myMovie.title){
          this.$store.dispatch('createList',myMovie)
        }
        this.movieTitle=null
      }
  
    }
  }
  </script>
  ```

- MyListItem.vue

  ```vue
  <template>
    <div>
      <p></p>
      <div class="list-color">
        <span  @click="updateMovie" :class="{'is-watched':myMovie.isWatched}">{{myMovie.title+' '}}</span>
        <b-button size='sm' @click="deleteMovie">Delete</b-button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name:'MyListItem',
    props:{
      myMovie:Object,
    },
    methods:{
      deleteMovie:function(){
        this.$store.dispatch('deleteMovie',this.myMovie)
      },
      updateMovie:function(){
        this.$store.dispatch('updateMovie',this.myMovie)
      }
    }
  }
  </script>
  
  <style>
  .is-watched{
    color: grey;
    text-decoration: line-through;
  }
  .list-color{
    background-color:rgb(243, 234, 234);
  }
  
  </style>
  ```

  
