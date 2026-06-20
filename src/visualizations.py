import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

class Visualizer:
    """Create and save visualizations"""
    
    def __init__(self, df):
        self.df = df
        self.output_path = Path('results/visualizations')
        self.output_path.mkdir(parents=True, exist_ok=True)
    
    def plot_distribution(self, column, filename='distribution.png'):
        """Plot distribution of a column"""
        plt.figure(figsize=(10, 6))
        sns.histplot(data=self.df, x=column, kde=True)
        plt.title(f'Distribution of {column}')
        plt.savefig(self.output_path / filename)
        plt.close()
    
    def plot_correlation(self, filename='correlation.png'):
        """Plot correlation heatmap"""
        numeric_df = self.df.select_dtypes(include=['number'])
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix')
        plt.savefig(self.output_path / filename)
        plt.close()
    
    def plot_boxplot(self, columns, filename='boxplot.png'):
        """Plot boxplot for multiple columns"""
        plt.figure(figsize=(12, 6))
        self.df[columns].boxplot()
        plt.title('Box Plot')
        plt.savefig(self.output_path / filename)
        plt.close()
