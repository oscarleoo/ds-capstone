import seaborn as sns
import matplotlib.pyplot as plt

def plot_lines(df, building_ids, meter=0):
    """
    Function for plotting sequences 3 columns
    
    Input:
        df - the data to plot
        building_ids - the building_ids that we want to show
        meter - the meter that we want to show
    """
    row, col = 0, 0
    nrows = int(len(building_ids) / 3)
    fig, axes = plt.subplots(ncols=3, nrows=nrows, figsize=(18, 2.5*nrows))
    for building_id in building_ids:
        values = df[(df.building_id == building_id) & (df.meter == meter)].meter_reading.values
        sns.lineplot(y=values, x=[i for i in range(len(values))], ax=axes[row][col])
        axes[row][col].set_xticks([])
        axes[row][col].set_yticks([])
        title = 'building_id: {}  meter: {}'.format(building_id, meter)
        axes[row][col].set_title(title, fontsize=16, pad=15)
        if col == 2:
            col = 0
            row += 1
        else:
            col += 1
    
    plt.tight_layout()
    plt.show()