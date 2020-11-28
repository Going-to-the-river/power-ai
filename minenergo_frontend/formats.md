# minenergo_frontend

> A Vue.js project

## Locations list

``` python
get_locations()

[
 #location[
],
 #location,
 #location,
]

#location
{
    title, id, graphs:[
        #graphs_group
    ]
}

#graphs_group
{ title, is_group=true, children=[#graph] }

#graph
{ title, id, ylab, is_group=false}

graph should have unique id!
```

Get graph by id

``` python
get_graph_by_id()

json:
- id
- resolution (day/week/month/year)
- start
- end

response:
{x:[], y:[]}
or
{x0:0, y:[]}
```

