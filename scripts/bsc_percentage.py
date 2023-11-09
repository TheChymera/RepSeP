import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cbook import get_sample_data


gender_degree_data = np.genfromtxt('data/percent-bachelors-degrees-women-usa.csv', delimiter=',', names=True)

# You typically want your plot to be ~1.33x wider than tall. This plot
# is a rare exception because of the number of lines being plotted on it.
# Common sizes: (10, 7.5) and (12, 9)
fig, ax = plt.subplots(1, 1)

# These are the colors that will be used in the plot
ax.set_prop_cycle(color=[
	'#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', '#98df8a',
	'#d62728', '#ff9896', '#9467bd', '#c5b0d5', '#8c564b', '#c49c94',
	'#e377c2', '#f7b6d2', '#7f7f7f', '#c7c7c7', '#bcbd22', '#dbdb8d',
	'#17becf', '#9edae5'])

# Remove the plot frame lines. They are unnecessary here.
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Ensure that the axis ticks only show up on the bottom and left of the plot.
# Ticks on the right and top of the plot are generally unnecessary.
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

fig.subplots_adjust(left=.06, right=.75, bottom=.02, top=.94)
# Limit the range of the plot to only where the data is.
# Avoid unnecessary whitespace.
ax.set_xlim(1969.5, 2011.1)
ax.set_ylim(-0.25, 90)

# Set a fixed location and format for ticks.
ax.set_xticks(range(1970, 2011, 10))
ax.set_yticks(range(0, 91, 10))
ax.xaxis.set_major_formatter(plt.FuncFormatter('{:.0f}'.format))
ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0f}%'.format))

# Remove the tick marks; they are unnecessary with the tick lines we just
# plotted. Make sure your axis ticks are large enough to be easily read.
# You don't want your viewers squinting to read your plot.
ax.tick_params(
	axis='both',
	which='both',
	bottom=False,
	top=False,
	labelbottom=True,
	left=False,
	right=False,
	labelleft=True,
	)

# Now that the plot is prepared, it's time to actually plot the data!
# Note that I plotted the majors in order of the highest % in the final year.
majors = ['Health Professions', 'Public Administration', 'Education',
	'Psychology', 'Foreign Languages', 'English',
	'Communications\nand Journalism', 'Art and Performance', 'Biology',
	'Agriculture', 'Social Sciences and History', 'Business',
	'Math and Statistics', 'Architecture', 'Physical Sciences',
	'Computer Science', 'Engineering']

y_offsets = {
	'Foreign Languages': 2.25,
	'English': 0.5,
	'Communications\nand Journalism': 0.0,
	'Art and Performance': -1.75,
	'Biology': -2.0,
	'Agriculture': 2.0,
	'Social Sciences and History': 0.15,
	'Business': -1.5,
	'Math and Statistics': 0.5,
	'Architecture': -1.75,
	'Physical Sciences': -1.75,
	'Computer Science': 0.75,
	'Engineering': -1.0,
	}

for column in majors:
	# Plot each line separately with its own color.
	column_rec_name = column.replace('\n', '_').replace(' ', '_')

	line, = ax.plot('Year', column_rec_name, data=gender_degree_data,
			)
		   #lw=2.5)

	# Add a text label to the right end of every line. Most of the code below
	# is adding specific offsets y position because some labels overlapped.
	y_pos = gender_degree_data[column_rec_name][-1] - 0.5

	if column in y_offsets:
		y_pos += y_offsets[column]

	# Again, make sure that all labels are large enough to be easily read
	# by the viewer.
	ax.text(2011.5, y_pos, column, color=line.get_color())
