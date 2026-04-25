import json
import pandas as pd
import os

class FileHandler:
    @staticmethod
    def save_to_json(data, filename):
        """Saves a list of dictionaries to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving JSON: {e}")

    @staticmethod
    def load_from_csv(filename):
        """Loads data using Pandas with basic error handling."""
        if not os.path.exists(filename):
            print(f"Warning: {filename} not found. Returning empty list.")
            return []
        try:
            df = pd.read_csv(filename)
            return df.to_dict(orient='records')
        except Exception as e:
            print(f"Error reading CSV: {e}")
            return []

    @staticmethod
    def save_to_csv(data_list, filename):
        """Saves list of dicts to CSV using Pandas."""
        df = pd.DataFrame(data_list)
        df.to_csv(filename, index=False)