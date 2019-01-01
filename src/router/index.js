import Vue from 'vue'
import Router from 'vue-router'
import Computers from '@/components/Computers'
import Motherboards from '@/components/Motherboards'
import Processors from '@/components/Processors'
import Rams from '@/components/Rams'
import Trunks from '@/components/Trunks'
import Warranties from '@/components/Warranties'
import Manufacturers from '@/components/Manufacturers'
import CustomSqlPage from '@/components/CustomSqlPage'

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
    },
    {
      path: '/processors',
      name: 'Processors',
      component: Processors
    },
    {
      path: '/rams',
      name: 'Rams',
      component: Rams
    },
    {
      path: '/trunks',
      name: 'Trunks',
      component: Trunks
    },
    {
      path: '/warranties',
      name: 'Warranties',
      component: Warranties
    },
    {
      path: '/manufacturers',
      name: 'Manufacturers',
      component: Manufacturers
    },
    {
      path: '/customsql',
      name: 'CustomSql',
      component: CustomSqlPage
    }
  ]
})
