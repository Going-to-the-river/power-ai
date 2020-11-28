import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import locations_json from "./locations_json";
import utils from "./utils";


var backend_url
if (window.location.hostname === '194.67.111.199'){
  backend_url = 'http://194.67.111.199/backend/'
}else{
  backend_url = 'http://localhost:54321/backend/'
}

var SCREEN_TYPES = {
  BIG:0,
  MEDIUM:1,
  SMALL:2,
}

var GRAPH_RESOLUTIONS = {
  DAY:{
    title:'День',
      name:'day'
  },
  MONTH:{
    title:'Месяц',
      name:'month'
  },
  YEAR:{
    title:'Год',
      name:'year'
  },
}

export default new Vuex.Store({
  state:{
    backend_url: backend_url,

    locations:[],
    current_location:null,
    location_position_by_id:locations_json.position_by_id,

    GRAPH_RESOLUTIONS:GRAPH_RESOLUTIONS,
    current_graph_resolution:GRAPH_RESOLUTIONS.DAY,
    current_graph_date: Date.now(),

    features:[],

    baseline_graph_data:[],
    prediction_graph_data:[{x:'2020.10.11', y:0},{x:'2020.10.12', y:1}],

    SCREEN_TYPES:SCREEN_TYPES,
    screen_type:SCREEN_TYPES.BIG,
  },
  actions:{

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    async get_locations(context) {
      var root_state = context.state

      var data_json = {}
      var data_string = JSON.stringify(data_json);
      var url = root_state.backend_url + 'get_locations/'

      await $.post(url, data_string)
        .done(async function(r_json, success){
          //~~~~~~~~~~~START CHECK ERROR~~~~~~~~~~~~~~~
          if (await utils.is_error(r_json, root_state, context)){
            return
          }
          //~~~~~~~~~~~END CHECK ERROR~~~~~~~~~~~~~~~
          //catalogue.catalogue_hierarchy.children = r_json.categories

          if (r_json.hasOwnProperty('locations')){
            var list_to = root_state.locations
            var list_from = r_json.locations

            list_to.length = 1
            list_to.pop()

            for(var i = 0; i < list_from.length; i++){
              var item = list_from[i]
              list_to.push(item)
            }
          }

        })
      // .fail(function(xhr, status, error) {
      //   alert('No connection with server!')
      // });
    },

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    async get_features(context) {
      var root_state = context.state

      var data_json = {}
      var data_string = JSON.stringify(data_json);
      var url = root_state.backend_url + 'get_features/'

      await $.post(url, data_string)
        .done(async function(r_json, success){
          //~~~~~~~~~~~START CHECK ERROR~~~~~~~~~~~~~~~
          if (await utils.is_error(r_json, root_state, context)){
            return
          }
          //~~~~~~~~~~~END CHECK ERROR~~~~~~~~~~~~~~~

          if (r_json.hasOwnProperty('features')){
            var list_to = root_state.features
            var list_from = r_json.features

            list_to.length = 1
            list_to.pop()

            for(var i = 0; i < list_from.length; i++){
              var item = list_from[i]
              list_to.push(item)
            }
          }

        })
      // .fail(function(xhr, status, error) {
      //   alert('No connection with server!')
      // });
    },

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    async get_graph_by_id(context, data){
      var root_state = context.state

      var resolution = root_state.current_graph_resolution.name

      var start = new Date(root_state.current_graph_date)
      var end = new Date(root_state.current_graph_date)
      if (resolution === 'day'){
        start.setDate(start.getDate() - 15);
        end.setDate(end.getDate() + 15);
      }else if(resolution === 'month'){
        start.setDate(start.getDate() - 180);
        end.setDate(end.getDate() + 180);
      }else{
        start.setDate(start.getDate() - 365*5);
        end.setDate(end.getDate() + 365*5);
      }

      var data_json = {
        id:data.id,
        resolution:resolution,
        start:start,
        end:end,
      }
      var data_string = JSON.stringify(data_json);
      var url = root_state.backend_url + 'get_graph_by_id/'

      await $.post(url, data_string)
        .done(async function(r_json, success){
          //~~~~~~~~~~~START CHECK ERROR~~~~~~~~~~~~~~~
          if (await utils.is_error(r_json, root_state, context)){
            return
          }
          //~~~~~~~~~~~END CHECK ERROR~~~~~~~~~~~~~~~
          //catalogue.catalogue_hierarchy.children = r_json.categories

          if (r_json.hasOwnProperty('data')){
            //~~~~~~~~~~~~~~~~~~~~~start replace data~~~~~~~~~~~~~~~~~~~~
            var list_from =r_json.data
            var list_to = data.chart.data.datasets[0].data

            list_to.length = 1;
            list_to.pop();

            var value_min = Infinity
            var value_max = 0
            for(var i = 0; i < list_from.length; i++){
              var item = list_from[i]

              var y = item.y
              if(y < value_min){
                value_min = y
              }
              if(y > value_max){
                value_max = y
              }

              list_to.push(item)
            }
            //~~~~~~~~~~~~~~~~~~~~~end replace data~~~~~~~~~~~~~~~~~~~~

            //~~~~~~~~~~~~~~~~~~~~~start replace data 2~~~~~~~~~~~~~~~~~~~~
            var datasets = data.chart.data.datasets

            var today = new Date()
            today.setHours(0,0,0,0)

            if(today.getTime() < end.getTime() + 3600){
              datasets[1] = {
                label:'today',
                borderColor:'red',
                pointBackgroundColor:'red',
                data:[
                  {
                    x:today,
                    y:value_min
                  },
                  {
                    x:today,
                    y:value_max
                  }
                ]
              }

            }else{
              datasets.length = 1
            }

            //~~~~~~~~~~~~~~~~~~~~~end replace data 2~~~~~~~~~~~~~~~~~~~~

            data.chart.update();
          }
          if (r_json.hasOwnProperty('color')){
            data.color_backref = r_json.color
          }
          if (r_json.hasOwnProperty('ylab')){
            var ds = data.chart.data.datasets[0]
            if (ds.label === 'empty'){
              ds.label = r_json.ylab
            }
          }

        })
      // .fail(function(xhr, status, error) {
      //   alert('No connection with server!')
      // });
    },

    //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    async get_prediction(context, data){
      var root_state = context.state

      var data_json = {
        features:data.features
      }
      var data_string = JSON.stringify(data_json);
      var url = root_state.backend_url + 'get_prediction/'

      await $.post(url, data_string)
        .done(async function(r_json, success){
          //~~~~~~~~~~~START CHECK ERROR~~~~~~~~~~~~~~~
          if (await utils.is_error(r_json, root_state, context)){
            return
          }
          //~~~~~~~~~~~END CHECK ERROR~~~~~~~~~~~~~~~
          //catalogue.catalogue_hierarchy.children = r_json.categories

          if (r_json.hasOwnProperty('baseline')){
            //~~~~~~~~~~~~~~~~~~~~~start replace data~~~~~~~~~~~~~~~~~~~~
            var list_from = r_json.baseline
            var list_to = root_state.baseline_graph_data

            list_to.length = 1;
            list_to.pop();

            for(var i = 0; i < list_from.length; i++){
              var item = list_from[i]

              list_to.push(item)
            }
            //~~~~~~~~~~~~~~~~~~~~~end replace data~~~~~~~~~~~~~~~~~~~~
          }

          if (r_json.hasOwnProperty('prediction')){
            //~~~~~~~~~~~~~~~~~~~~~start replace data 2~~~~~~~~~~~~~~~~~~~~
            var list_from = r_json.prediction
            var list_to = root_state.prediction_graph_data

            list_to.length = 1;
            list_to.pop();

            for(var i = 0; i < list_from.length; i++){
              var item = list_from[i]

              list_to.push(item)
            }
            //~~~~~~~~~~~~~~~~~~~~~end replace data 2~~~~~~~~~~~~~~~~~~~~
          }

        })
      // .fail(function(xhr, status, error) {
      //   alert('No connection with server!')
      // });
    },

  }
})
