
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import mannwhitneyu
import sys
import os
import re
from itertools import combinations

plot_border_color = '#ffffff'
plot_tick_color = '#bbbbbb'
compare_column = "Source"
plot_colors = sns.set_palette( sns.color_palette( [ "#F7001D", "#116552", "#FFA504","#FF68ED" ] ) )


# Ensure a file path and column header are provided as command-line arguments
if len(sys.argv) < 3:
    print("Usage: python script_name.py path_to_tsv_file \"column header\" \"Y-axis title\"")
    sys.exit()

# Read the data from the provided TSV file path
tsv_file_path = sys.argv[1]
data = pd.read_csv(tsv_file_path, sep='\t')

# Read desired data to print
print_column = sys.argv[2]
if len(sys.argv) < 4:
    print_column_title = sys.argv[2]
else:
    print_column_title = sys.argv[3]
print_column_title_filename = re.sub(r'\W', '', print_column_title)

# Identify unique conditions in the compare_column
# conditions = data[compare_column].unique()
conditions = list(data[compare_column].unique())

# Perform pairwise t-tests between all unique condition pairs
p_values = {}
for cond1, cond2 in combinations(conditions, 2):
    # t_stat, p_value = ttest_ind(data[data[compare_column] == cond1][print_column], data[data[compare_column] == cond2][print_column], nan_policy='omit')
    u_stat, p_value = mannwhitneyu(data[data[compare_column] == cond1][print_column], data[data[compare_column] == cond2][print_column], alternative='two-sided') 
    p_values[(cond1, cond2)] = p_value

# Determine an appropriate y-axis range for the print_column measurement
data_max = data[print_column].max()
data_min = data[print_column].min()
y_min = data_min - abs( data_max - data_min ) * .25
y_max = data_max - abs( data_max - data_min ) * .25
# y_min = data[print_column].min() - abs( data[print_column].min() * .5 )
# y_max = data[print_column].max() + abs( data[print_column].max() * .25 ) #leaves room for p-value

# Plot setup
plt.rcParams["font.family"] = "Arial"
#plt.rcParams["font.size"] = "9.5"
plt.figure(figsize=(len(conditions) * 0.75, 6))
#plt.figure(figsize=(len(conditions) * 0.8, 3.5))

#print( data[compare_column] )

# Plotting
sns.violinplot(x=compare_column, y=print_column, hue=compare_column, data=data, palette=plot_colors, order=conditions, inner='quart', density_norm='width', log_scale=False)
sns.stripplot(x=compare_column, y=print_column, hue=compare_column, data=data, palette='dark:black', jitter=0.4, size=1, marker="o", alpha=0.7, order=conditions, dodge=False)

plt.ylim(y_min, y_max)
#plt.yscale('symlog')
plt.xlabel("")

# Remove the legend since it's redundant
plt.legend().set_visible(False)

# Adjust spine colors and labels
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_edgecolor(plot_border_color)
ax.tick_params(axis='both', which='both', color=plot_tick_color, labelcolor='black')
ax.set_ylabel(print_column_title)
ax.set_xticklabels(conditions)

# Print p-values (for now, just print to console if cannot annotate on plot)
for pair, p_value in p_values.items():
    print(f"{pair}: p = {p_value:.4f}")
    
    # Assuming 'ax' is the Axes object for your plot
y_max = ax.get_ylim()[1]  + abs( data_max - data_min ) * 0.33 # Get the current maximum y-value to start annotations
increment = abs( data_max - data_min ) * 0.1   # Increment to separate annotations

for (cond1, cond2), p_val in p_values.items():
    x1 = conditions.index(cond1)
    x2 = conditions.index(cond2)
    y = y_max + increment
    bracket_height = increment / 4

    # Explicitly adjust the line specifications for visibility
    ax.plot([x1, x2], [y+ bracket_height, y+ bracket_height], color="black", linewidth=1)  # Connecting line
    
    ax.plot([x1, x1], [y, y + bracket_height], color="black", linewidth=1)  # Left bracket end
    ax.plot([x2, x2], [y, y + bracket_height], color="black", linewidth=1)  # Right bracket end

    # Place p-value text above the bracket
    ax.text((x1 + x2) / 2, y + bracket_height * 1.25, f'p={p_val:.3f}', ha='center', va='bottom')

    # Adjust y_max for the next annotation
    y_max += increment

# After plotting all annotations, adjust y-limits to include them
current_ylim = ax.get_ylim()
ax.set_ylim(current_ylim[0], y_max + increment)  # Adjust the top y-limit to include the last annotation

plt.tight_layout()

# Save the figure as a .png file
base_filename = os.path.basename(tsv_file_path).split('.')[0]
output_filename = f"{base_filename}_{print_column_title_filename}.png"
plt.savefig(output_filename, dpi=300)
print(f"Figure saved as {output_filename}")
