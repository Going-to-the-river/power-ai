<template>
  <div class="chart-container">
    <canvas :id="'chart_' + graph_id"></canvas>
  </div>
</template>

<script>
  import Chart from 'chart.js';

  export default {
    props:{
      graph_id:{
        type:Number,
        required:true
      },
      title:{
        type:String,
        required:true,
      },
      ylab:{
        type:String,
      },
      //~~~~~~~~~~
      is_immutable:{
        type:Boolean,
        default: false
      },
      immutable_datasets:{
        type:Array,
        default:() => {return []},
      },
      color:{
        type:String,
        default:'teal'
      },
    },
    data(){
      return{
        chart:null,
      }
    },
    computed:{
      current_graph_resolution(){
        return this.$store.state.current_graph_resolution
      },
      current_graph_date(){
        return this.$store.state.current_graph_date
      }
    },
    watch:{
      current_graph_resolution (new_value, old_value) {
        this.update_data()
      },
      current_graph_date (new_value, old_value) {
        this.update_data()
      }
    },
    methods:{
      update_color(color){
        var options = this.chart.options
        options.elements.line.borderColor = color
        options.elements.point.borderColor = color
        options.elements.point.backgroundColor = color

        this.chart.update()
      },
      update_time_unit(){
        var options = this.chart.options
        options.scales.xAxes = [{
          type: 'time',
          time: {
            unit: this.$store.state.current_graph_resolution.name,
            displayFormats: {
              day: 'D MMM YYYY'
            }
          },
        }]

        this.chart.update()
      },
      async update_data(){
        if(this.is_immutable){
          return
        }

        var request_data = {
          id:this.graph_id,
          chart:this.chart,
          color_backref:null,
        }
        await this.$store.dispatch('get_graph_by_id', request_data)

        if (request_data.color_backref !== null){
          this.update_color(request_data.color_backref)
        }
        this.update_time_unit()
      }
    },
    async mounted(){
      var ctx = document.getElementById('chart_' + this.graph_id);
      var chart = new Chart(ctx, {
        type: 'line',
        data: {
          datasets: this.is_immutable ? this.immutable_datasets : [
            {
              label:(this.ylab !== undefined) ? this.ylab : 'empty',
              data:[],
            },
          ]
        },
        options: {
          title: {
            display: true,
            text: this.title,
            fontSize: 20,
            fontFamily: "'Roboto', 'sans-serif'",
            fontColor: '#000',
            fontStyle: 'normal',
            padding: 5,
          },
          scales: {
            xAxes: [{
              type: 'time',
              time: {
                unit: 'day'
              },
            }]
          },
          legend: {
            labels: {
              filter: function(item, chart) {
                // Logic to remove a particular legend item goes here
                if (item.text.includes('empty')){
                  return false
                }
                if (item.text.includes('today')){
                  return false
                }
                return true
              }
            }
          },
          responsive:true,
          maintainAspectRatio: false,
        }
      });
      this.chart = chart

      this.update_color(this.color)
      this.update_time_unit()
      this.update_data()
    }

  }
</script>

<style scoped>
  .chart-container{
    position: relative;
    width: 100%;
    height: 100%;

    background-color: #f0f0f0;
    border-radius: 5px;
  }

</style>
