import numpy as np
import pandas as pd
import string

# 5.1
random_array_1d = np.random.randint(10, size=100)

# 5.2
random_array_2d = np.reshape(random_array_1d, (10, 10))

# 5.3
random_data_frame = pd.DataFrame(data=random_array_2d, index=list(map(chr, range(97,107))), columns=range(1, 11))

# 5.4
new_df_index = random_data_frame.iloc[::2, 5:]
