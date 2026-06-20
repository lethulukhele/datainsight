import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalyzer:
    """Analyze data and generate insights"""
    
    def __init__(self, df):
        self.df = df
    
    def get_summary_statistics(self):
        """Generate summary statistics"""
        return {
            'shape': self.df.shape,
            'columns': list(self.df.columns),
            'dtypes': self.df.dtypes.to_dict(),
            'missing_values': self.df.isnull().sum().to_dict(),
            'describe': self.df.describe().to_dict()
        }
    
    def analyze_trends(self):
        """Analyze trends in the data"""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        return {
            'correlation': self.df[numeric_cols].corr().to_dict(),
            'variance': self.df[numeric_cols].var().to_dict(),
            'mean': self.df[numeric_cols].mean().to_dict()
        }
    
    def detect_outliers(self, column, method='iqr'):
        """Detect outliers in a column"""
        if method == 'iqr':
            Q1 = self.df[column].quantile(0.25)
            Q3 = self.df[column].quantile(0.75)
            IQR = Q3 - Q1
            return self.df[(self.df[column] < Q1 - 1.5 * IQR) | (self.df[column] > Q3 + 1.5 * IQR)]
