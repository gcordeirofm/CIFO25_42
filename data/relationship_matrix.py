import pandas as pd
import numpy as np
from pathlib import Path

here = Path(__file__).parent
df = pd.read_csv(here / "seating_data.csv", index_col=0)
relationship_matrix = df.to_numpy()