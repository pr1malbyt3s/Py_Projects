import plotly.graph_objects as go

fig = go.Figure(data=
	go.Parcoords(
		dimensions = list([
			dict(range = [1,5],
				tickvals = [2,4],
				label = 'x1', values = [2,4,2,2,4],
				ticktext = ['A', 'B']),			
			dict(range = [1,5],
				label = 'x2', values = [1,3,5,2,5]),
			dict(range = [21,30],
				label = 'x3', values = [25,27,29,21,30]),
			dict(range = [3,9],
				label = 'x4', values = [7,3,5,9,7]),
			dict(range = [1,5],
				tickvals = [2,4],
				label = 'x5', values = [2,2,2,4,4],
				ticktext = ['T', 'F']),
			dict(range = [1,3],
				label = 'x6', values = [1,2,1,3,1]),
			dict(range = [2,9],
				label = 'x7', values = [5,9,7,2,7])
		])
	)
)
fig.show()
