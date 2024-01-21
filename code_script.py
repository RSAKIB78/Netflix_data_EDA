# %%
# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import seaborn as sns

# Reading csv
netflix_data = pd.read_csv("netflix_data.csv")
display(netflix_data)



# %%
# Checking the structure of the table
print(netflix_data.info()) #structure info

print(netflix_data.describe()) #summary stats

# Checking nulls
missing_values = netflix_data.isnull().sum()
print("Missing values:", missing_values)

# %%
# Groupings and aggregations
grouped_data = netflix_data.groupby("type")["duration"].mean()
print("Grouped data:", grouped_data)

# %%
# Exploring the column values
table = PrettyTable(["Column", "Unique Values"])

for column in netflix_data.columns:
    unique_values = netflix_data[column].unique()
    table.add_row([column, unique_values])

print(table)

# %%
# Filtering all TV Shows
netflix_subset = netflix_data[netflix_data["type"] != "TV Show"]

# Subsetting the dataset

netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]

# %%
# Finding movies shorter than 60 minutes
short_movies = netflix_movies[netflix_movies["duration"] < 60]
display(short_movies)

# %%
# Plotting histograms
fig, axes = plt.subplots(3, 1, figsize=(12, 15))

# Histogram for 'genre'
axes[0].hist(short_movies['genre'], bins=30, color='skyblue', edgecolor='black')
axes[0].set_title('Histogram of Genre')
axes[0].set_xlabel('Genre')
axes[0].set_ylabel('Count')
axes[0].tick_params(axis='x', rotation=45)

# Histogram for 'country'
axes[1].hist(short_movies['country'].astype(str).sort_values(), bins=30, color='lightcoral', edgecolor='black', orientation='horizontal')
axes[1].set_title('Histogram of Country')
axes[1].set_xlabel('Count')
axes[1].set_ylabel('Country')

# Histogram for 'release_year'
axes[2].hist(short_movies['release_year'].astype(str).sort_values(), bins=30, color='lightgreen', edgecolor='black')
axes[2].set_title('Histogram of Release Year')
axes[2].set_xlabel('Release Year')
axes[2].set_ylabel('Count')
axes[2].tick_params(axis='x', rotation=45)

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()


# %%
# Iterate over the genres to assign colors
colors = []

for index, rows in netflix_movies.iterrows():
    genre = rows["genre"]
    if genre == "Children":
       color = "Red"
    elif genre == "Documentaries":
        color = "Black"
    elif genre == "Stand-up":
        color = "Blue"
    else:
        color = "Purple"

    colors.append(color) 

#Plot by colors
release_year = netflix_movies['release_year']
duration = netflix_movies['duration']

# Plot by colors with enhanced settings
plt.figure(figsize=(10, 6))
scatter = plt.scatter(release_year, duration, c=colors, alpha=0.6, edgecolors='k', linewidths=0.5)

# Add labels and title
plt.xlabel('Release Year')
plt.ylabel('Duration (min)')
plt.title('Movie Duration by Year of Release')

# Add legend
legend_labels = {'Red': 'Children', 'Black': 'Documentaries', 'Blue': 'Stand-up', 'White': 'Other'}
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label) for color, label in legend_labels.items()]
plt.legend(handles=legend_elements, title='Genre', loc='upper right')

# Customize the colorbar
cbar = plt.colorbar(scatter)
cbar.set_ticks([])
cbar.set_ticklabels([])

# Add a general trendline for the entire plot
sns.regplot(x=release_year, y=duration, scatter=False, color='gray', line_kws={'label': 'Trendline'})

# Show the plot
plt.show()



# %%
