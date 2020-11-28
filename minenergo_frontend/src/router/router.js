import Vue from 'vue'
import Router from 'vue-router'

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//import page_frame from '@/components/page_frame'
const page_frame = () => import('@/components/page_frame/page_frame')

const view_simple = () => import('@/components/page_frame/view_simple')
const view_advanced = () => import('@/components/page_frame/view_advanced')
const view_prediction = () => import('@/components/page_frame/view_prediction')

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Vue.use(Router)

export default new Router({
  // mode: 'history',
  scrollBehavior(to, from, savedPosition){
    return {
      x:0,
      y:0
    }
  },
  routes: [
    {
      name:'page_frame',
      path:'/',
      redirect:'simple',
      component: page_frame,
      children:[
        {
          name:'view_simple',
          path:'simple',
          component: view_simple,
        },
        {
          name:'view_advanced',
          path:'advanced',
          component: view_advanced,
        },
        {
          name:'view_prediction',
          path:'prediction',
          component: view_prediction,
        },
      ]
    },
  ]
})
