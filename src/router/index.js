import Vue from 'vue'
import Router from 'vue-router'
import Computers from '@/components/Computers'
import Motherboards from '@/components/Computers'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Computers',
      component: Computers
    },
    {
      path: '/motherboards',
      name: 'Motherboards',
      component: Motherboards
    }
  ]
})
