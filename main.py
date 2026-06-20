"""
DataInsight Main Script
ETL Pipeline and Analysis
"""

from src.data_loader import DataLoader
from src.analyzer import DataAnalyzer
from src.visualizations import Visualizer
import pandas as pd

def main():
    print("DataInsight - Data Analytics Pipeline")
    print("=" * 50)
    
    # Initialize data loader
    loader = DataLoader('data/raw/')
    
    # Load sample data (you would replace this with your actual data)
    print("\n1. Loading data...")
    # df = loader.load_csv('sample_data.csv')
    
    # For demo, create sample data
    df = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=100),
        'sales': [100 + i*2 for i in range(100)],
        'revenue': [1000 + i*20 for i in range(100)]
    })
    
    print(f"Data shape: {df.shape}")
    
    # Analyze data
    print("\n2. Analyzing data...")
    analyzer = DataAnalyzer(df)
    summary = analyzer.get_summary_statistics()
    print(f"Columns: {summary['columns']}")
    
    # Create visualizations
    print("\n3. Creating visualizations...")
    visualizer = Visualizer(df)
    visualizer.plot_distribution('sales', 'sales_distribution.png')
    visualizer.plot_boxplot(['sales', 'revenue'], 'boxplot.png')
    
    # Save processed data
    print("\n4. Saving processed data...")
    loader.save_data(df, 'processed_data.csv')
    
    print("\n✅ Analysis complete!")
    print(f"Results saved to: results/visualizations/")

if __name__ == '__main__':
    main()
