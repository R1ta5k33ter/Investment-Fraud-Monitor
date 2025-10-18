import pandas as pd
import json
import os

def json_to_dataframe(file_path, lines=False):
    """
    Convert a JSON file into a pandas DataFrame.

    Parameters:
    -----------
    file_path : str
        The path to the JSON file.
    lines : bool, optional (default=False)
        Set to True if the JSON file uses JSON Lines format 
        (each line is a JSON object).

    Returns:
    --------
    pd.DataFrame
        DataFrame containing the JSON content.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at path '{file_path}' was not found.")

    try:
        # Use pandas built-in JSON reader
        df = pd.read_json(file_path, lines=lines)
        return df
    except ValueError:
        # Fallback for more complex JSON structures
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        df = pd.json_normalize(data)
        return df


# Test it:
# activate venv on Windows: & '.venv\Scripts\Activate.ps1'
# activate venv on Linux/Mac: source .venv/bin/activate

# Get the absolute path to the JSON file
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', 'sample_data', '2025_10_18_investor-alert-list_from_moneysmart.gov.au.json')

# Convert JSON to DataFrame
df = json_to_dataframe(file_path, lines=False)
print(df.head(20))

df.to_csv("sample_output.csv", index=False, encoding='utf-8')
