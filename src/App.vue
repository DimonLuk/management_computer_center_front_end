<template>
  <div id="app">
    <v-app id='management'>
      <v-toolbar app>
        <v-toolbar-title>Управление ВЦ ВУЗа</v-toolbar-title>
      </v-toolbar>
      <v-navigation-drawer app>
        <v-toolbar flat>
          <v-list>
            <v-list-tile>
              <v-list-tile-title class="title">
                Меню
              </v-list-tile-title>
            </v-list-tile>
          </v-list>
        </v-toolbar>
        <v-divider></v-divider>
        <v-list dense class="pt-0">
          <v-list-tile
            v-for="item in items"
            :key="item.title"
            @click="changeRoute(item)"
          >
            <v-list-tile-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>
  
            <v-list-tile-content>
              <v-list-tile-title :class='item.isHighlighted'>
              {{ item.title }}
              </v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-navigation-drawer>
      <v-content>
        <router-view></router-view>
      </v-content>
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      items: [
        { title: 'Компьютеры', icon: 'computer', isHighlighted: 'blue--text', route: '/' },
        { title: 'Материнские платы', icon: 'developer_board', isHighlighted: '', route: '/motherboards'  },
        { title: 'Процессоры', icon: 'memory', isHighlighted: '', route: '/processors'  },
        { title: 'Оперативная память', icon: 'storage', isHighlighted: '', route: '/rams'  },
        { title: 'Корпуса', icon: 'kitchen', isHighlighted: '', route: '/trunks'  },
        { title: 'Гарантии', icon: 'class', isHighlighted: '', route: '/warranties'  },
        { title: 'Производители', icon: 'domain', isHighlighted: '', route: '/manufacturers'  },
      ]
    }
  },
  methods: {
    changeRoute(item) {
      for(let i of this.items) {
        i.isHighlighted = '';
      }
      item.isHighlighted = 'blue--text';
      this.$router.push(item.route)
    }
  }
}
</script>

<style>
body {
  margin: 0;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

main {
  text-align: center;
  margin-top: 40px;
}

header {
  margin: 0;
  height: 56px;
  padding: 0 16px 0 24px;
  background-color: #35495E;
  color: #ffffff;
}

header span {
  display: block;
  position: relative;
  font-size: 20px;
  line-height: 1;
  letter-spacing: .02em;
  font-weight: 400;
  box-sizing: border-box;
  padding-top: 16px;
}
</style>
