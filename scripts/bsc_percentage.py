import matplotlib.pyplot as plt
from matplotlib.mlab import csv2rec
from matplotlib.cbook import get_sample_data

fname = get_sample_data('percent_bachelors_degrees_women_usa.csv')
gender_degree_data = csv2rec(fname)

color_sequence = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c',
                  '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5',
                  '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f',
                  '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']

ax = plt.subplot(1,1,1)

ax.set_xlim(1970, 2011)
ax.set_ylim(-0.25, 90)

plt.xticks(range(1970, 2011, 10))
plt.yticks(range(0, 91, 10))

major_codes = {
    'Health Professions':'health_professions',
    'Public Administration':'public_administration',
    'Education':'education',
    'Psychology':'psychology',
    'Foreign Languages':'foreign_languages',
    'English':'english',
    'Comm. and Journalism':'communications_and_journalism',
    'Art and Performance':'art_and_performance',
    'Biology':'biology',
    'Agriculture':'agriculture',
    'Soc. Sciences and History':'social_sciences_and_history',
    'Business':'business',
    'Math and Statistics':'math_and_statistics',
    'Architecture':'architecture',
    'Physical Sciences':'physical_sciences',
    'Computer Science':'computer_science',
    'Engineering':'engineering',
    }

y_offsets = {
    'Foreign Languages': 1,
    'English': -1,
    'Comm. and Journalism': 0.8,
    'Art and Performance': -1.2,
    'Agriculture': 2.2,
    'Soc. Sciences and History': 0.,
    'Business': -1.8,
    'Math and Statistics': 0.1,
    'Architecture': -2.2,
    'Computer Science': 0.8,
    'Engineering': -1.4,
    'Physical Sciences': -2.5,
    'Biology': -1.7,
    'Health Professions': 0.4,
    'Public Administration': 0,
    'Education': -0.6,
    'Psychology':-1,
    }

for rank, major in enumerate(major_codes):
    line = plt.plot(gender_degree_data.year,
                    gender_degree_data[major_codes[major]],
                    color=color_sequence[rank])

    y_pos = gender_degree_data[major_codes[major]][-1] - 0.5

    if major in y_offsets:
        y_pos += y_offsets[major]

    plt.text(2011.5, y_pos, major, color=color_sequence[rank])

