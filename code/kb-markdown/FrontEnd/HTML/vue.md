# vue 3

## router

```vue
import {createRouter, createWebHistory} from 'vue-router';

const routes = [
    {
        path: '/',
        component: () => import("../components/HomeComp.vue"),
        children: [
            {
            component: () => import("../components/form/DmComp.vue"),
            path: '/dm'
        },
        {
            component: () => import("../components/form/XMLChunk.vue"),
            path: '/xml-chunk'
        },

        ]
    },
    {
        path: '/ab',
        component: () => import("../components/AboutComp.vue")
    },
    {
        path: '/co',
        component: () => import("../components/ContactComp.vue")
    }
]


const router = createRouter({
    history: createWebHistory(),
    routes,
    linkActiveClass: "active"
})

export default router
```

## about vue

```vue
<template>

  <div class="container-fluid mt-5">
    <div class="row">
      <div class="col-sm-6 col-sm-offset-3">
        <h2>About</h2>
        <p>Lorem ipsum dolor sit</p>
      </div>

    </div>

  </div>

</template>

<script>
export default {}
</script>

<style scoped>

</style>
```

## xml chunk ui

```vue
<template>
  <div class="row">
    <div class="col-sm-6">
      <h3>XML chunk</h3>
      <form @submit.prevent="onSubmit">
        <table>
          <tr>
            <td>loc</td>
            <!--        <td><input type="text" v-model="res.loc"/></td>-->
            <td><textarea v-model="res.loc" rows="3" cols="20"></textarea></td>
          </tr>
          <tr>
            <td>content type</td>
            <td><input type="text" v-model="res.ct"/></td>
          </tr>
          <tr>
            <td>tag selected</td>
            <td><input type="text" v-model="res.ts" required/>
              <div class="max-width">
              <small>Multiple values should be comma seperated</small>
              </div>
            </td>
          </tr>
          <tr>
            <td>att selected</td>
            <td><input type="text" v-model="res.att"/>
              <div class="max-width">

              <small>Multiple values should be comma seperated</small>
              </div>

            </td>
          </tr>

          <tr>
            <td>Choose product</td>
            <td>
              <input type="checkbox" id="c1" v-model="selectAll">
              <label for="c1"> all products</label><br>
              OR
              <button @click="get_dir" type="button">Choose from prod</button>

              <div v-for="item in res.prods" :key="item">
                <input type="checkbox" :id="item" v-model="res.selected" :value="item">
                <label :for="item"> {{ item }}</label>
              </div>
              <div>
                <small>{{ msg }}</small>
              </div>
            </td>
          </tr>

          <tr>
            <td colspan="2">
              <button type="submit">Submit</button>
            </td>
          </tr>
        </table>

      </form>
      <h3>Sample directory structure</h3>
      <pre>
xml
├─ xml_deskbook_chunk
├─ xml_deskbook_orig
│  ├─ ppct55
│  │  └─ ppct55.xml
│  └─ ppct65
│     └─ ppct65.xml
└─ xml_deskbook_zip
</pre>

    </div>
    <div class="col-sm-6">
      <h3>Logs</h3>
      <ol v-html="out">
      </ol>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import sourceData from '../../store.json'

export default {
  methods: {
    async onSubmit() {
      if (this.res.selected.length < 1 && this.selectAll === false) {
        this.msg = 'Please select prod'
        return
      } else {
        this.msg = ''
      }
      this.out = ''
      this.out += `<li>processing...</li>`
      console.log(this.res);
      try {
        fetch("http://localhost:5000/xml-chunk", {
          method: "post",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({
            loc: this.res.loc,
            ct: this.res.ct,
            tag_selected: this.res.ts,
            att_sel: this.res.att,
            all: this.selectAll,
            prod: this.res.selected
          })
        }).then(async (response) => {
          const reader = response.body.getReader();
          while (true) {
            const {value, done} = await reader.read();
            if (done) break;
            let string = new TextDecoder().decode(value);
            this.out += `<li>${string}</li>`
          }
          this.out += `<li>processed</li>`
        });
      } catch (error) {
        console.error(error);
        this.out = error
      }
    }
    ,
    async get_dir() {
      console.log(this.res);
      try {
        let result = await axios.post("http://localhost:5000/dir", {
          loc: this.res.loc,
          ct: this.res.ct
        });
        console.log(result);
        if (result.data['status'] === 'success') {
          this.res.prods = result.data['ls']
        }
      } catch (error) {
        console.error(error);
        this.out = error
      }
    }
  }
  ,
  data() {
    return {
      msg: '',
      out: "",
      disabled: true,
      res: {
        loc: sourceData.loc,
        ct: sourceData.ct,
        ts: '',
        att: '',
        // all: true,
        prods: [],
        selected: []
      },
    };
  }
  ,

  computed: {
    selectAll: {
      get: function () {
        if (this.res.prods) {
          return this.res.selected.length === this.res.prods.length;
        } else {
          return false;
        }
      },
      set: function (value) {
        let selected = [];
        if (value) {
          this.res.prods.forEach(function (item) {
            selected.push(item);
          });
        }
        this.res.selected = selected;
      }
    }
  }
}
</script>
```

## header comp

```vue
<template>
  <nav class="topnav">
      <router-link to="/">Home</router-link>
      <router-link to="/ab">About</router-link>
      <router-link to="/co">Contact</router-link>
    </nav>
</template>
```

## app vue

```vue
<template>
  <HeaderComp/>
  <router-view></router-view>
</template>
<script>
import HeaderComp from './components/HeaderComp.vue'
import HomeComp from './components/HomeComp.vue'

export default {
  components:{
    HeaderComp,
    HomeComp
  }
}

</script>



```

## main.js

```vue
import { createApp } from 'vue'
import './style.css'
import './grid.css'
import App from './App.vue'
import router from "./router/index_router.js";


createApp(App).use(router).mount('#app')

```

## expose network

```vue
export default defineConfig({
  plugins: [vue()],
  server: {
    host: true
  }
})
```

## run vite app

```vue
npm run dev
```
