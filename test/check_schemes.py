from matplotlib import pyplot as plt

from plotsauce import schemes

fig, ax = plt.subplots()
cs = schemes.cycle_scheme(schemes.BrightScheme)
for i, c in enumerate(schemes.BrightScheme):
    ax.hlines(i, xmin=0, xmax=1, color=c.value)
plt.show()