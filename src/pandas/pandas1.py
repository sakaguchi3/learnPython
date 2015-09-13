import pandas as pd
from numpy import ndarray
from pandas.core.series import Series

cnt: Series = pd.Series([10, 20, 30, 50, 80, 130])

v2: ndarray = cnt.values

pass
