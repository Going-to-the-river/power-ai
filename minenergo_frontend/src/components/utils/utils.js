import Vue from 'vue'

export default {
  set_all_graphs_selected(locations, is_selected){
    //~~~~~~~~~~~~~~~~start locations~~~~~~~~~~~~~~~~~~~~
    for(var i = 0; i < locations.length; i++){
      var location = locations[i]

      //~~~~~~~~~~~~~~~~start graphs~~~~~~~~~~~~~~~~~~~~
      var graphs = location.graphs
      for(var j = 0; j < graphs.length; j++){
        var graph = graphs[j]

        if(!graph.is_group){
          Vue.set(graph, 'is_selected', is_selected)
        }else{
          //~~~~~~~~~~~~~~~~start graphs lvl 2~~~~~~~~~~~~~~~~~~~~
          var graphs_v2 = graph.children
          for(var k = 0; k < graphs_v2.length; k++){
            var graph_v2 = graphs_v2[k]

            if(!graph_v2.is_group){
              Vue.set(graph_v2, 'is_selected', is_selected)
            }
          }
          //~~~~~~~~~~~~~~~~end graphs lvl 2~~~~~~~~~~~~~~~~~~~~
        }
      }
      //~~~~~~~~~~~~~~~~end graphs~~~~~~~~~~~~~~~~~~~~
    }
    //~~~~~~~~~~~~~~~~end locations~~~~~~~~~~~~~~~~~~~~
  },


  set_all_graphs_expanded(locations, is_expanded){
    //~~~~~~~~~~~~~~~~start locations~~~~~~~~~~~~~~~~~~~~
    for(var i = 0; i < locations.length; i++){
      var location = locations[i]

      Vue.set(location, 'is_expanded', is_expanded)
    }
    //~~~~~~~~~~~~~~~~end locations~~~~~~~~~~~~~~~~~~~~
  },


  set_location_graphs_selected(locations, id, is_selected){
    //~~~~~~~~~~~~~~~~start locations~~~~~~~~~~~~~~~~~~~~
    for(var i = 0; i < locations.length; i++){
      var location = locations[i]

      if(location.id === id){
        //~~~~~~~~~~~~~~~~start graphs~~~~~~~~~~~~~~~~~~~~
        var graphs = location.graphs
        for(var j = 0; j < graphs.length; j++){
          var graph = graphs[j]

          if(!graph.is_group){
            Vue.set(graph, 'is_selected', is_selected)
          }else{
            //~~~~~~~~~~~~~~~~start graphs lvl 2~~~~~~~~~~~~~~~~~~~~
            var graphs_v2 = graph.children
            for(var k = 0; k < graphs_v2.length; k++){
              var graph_v2 = graphs_v2[k]

              if(!graph_v2.is_group){
                Vue.set(graph_v2, 'is_selected', is_selected)
              }
            }
            //~~~~~~~~~~~~~~~~end graphs lvl 2~~~~~~~~~~~~~~~~~~~~
          }
        }
        //~~~~~~~~~~~~~~~~end graphs~~~~~~~~~~~~~~~~~~~~
      }
    }
    //~~~~~~~~~~~~~~~~end locations~~~~~~~~~~~~~~~~~~~~
  },

}
