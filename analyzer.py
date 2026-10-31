import numpy as np
import pandas as pd

df = pd.read_csv("test_log.csv")          # fps, momentum, body count over time
data = np.load("test_log.npz")

x0 = data["x_pos_0"]                       # positions at the start
y0 = data["y_pos_0"]
r = np.sqrt((x0 - 640)**2 + (y0 - 360)**2) # distance from the screen centre (1280/2, 720/2)
# for a uniform disk, the histogram of r should rise linearly (r is uniform, not r²)