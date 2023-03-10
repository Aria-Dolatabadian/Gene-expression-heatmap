import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load gene expression data into a pandas dataframe
df = pd.read_csv('Spellman.csv', index_col=0)

# Create heatmap using seaborn
sns.heatmap(df, cmap='coolwarm', center=0, vmin=-2, vmax=2, linewidths=0.5, linecolor='gray')

plt.show()
