import pandas as pd
import numpy as np
from pathlib import Path

class DataLoader:
    """Load and manage data from various sources"""
    
    def __init__(self, data_path='data/raw/'):
        self.data_path = Path(data_path)
        self.data_path.mkdir(parents=True, exist_ok=True)
    
    def load_csv(self, filename):
        """Load CSV file"""
        file_path = self.data_path / filename
        return pd.read_csv(file_path)
    
    def load_json(self, filename):
        """Load JSON file"""
        file_path = self.data_path / filename
        return pd.read_json(file_path)
    
    def save_data(self, df, filename, format='csv'):
        """Save dataframe to file"""
        output_path = Path('data/processed') / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        if format == 'csv':
            df.to_csv(output_path, index=False)
        elif format == 'json':
            df.to_json(output_path)
        
        return output_path
