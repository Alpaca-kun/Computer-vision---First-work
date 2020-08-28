# %% [markdown] 
# ## A sample code to test 
# Sample obtained from https://matplotlib.org/3.2.1/gallery/lines_bars_and_markers/simple_plot.html

# %%
import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# %%
gray_img = cv2.imread('../Images/Alpaca.jpg',cv2.IMREAD_GRAYSCALE)
save_gray_img = cv2.imwrite('../Outputs/Gray_Alpaca.jpg', gray_img)

# %%
# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("../Outputs/test.png")
plt.show()
# %%
