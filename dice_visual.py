from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

def roll_dice(die_first, die_second):
    result = die_first.roll() * die_second.roll() 
    return result

def get_max(die_first, die_second):
    max_result = die_first.num_sides * die_second.num_sides
    return max_result

die_1 = Die()
die_2 = Die()


# Make some rolls, and store results in a list. 
results = [roll_dice(die_1, die_2) for x in range(1000)] 
frequencies = {frequency: results.count(frequency) for frequency in range(2, get_max(die_1, die_2)+1)}


# Visualize the results
x_values = list(range(2, get_max(die_1, die_2)+1))
data = [Bar(x=x_values, y=list(frequencies.values()))]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Multiplying Results of rolling two D6s 1000 times', 
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
