from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pickle

with open("pred_nn", "rb") as fp:   # Unpickling
    y_pred_list = pickle.load(fp)

p1_lat, p1_lon = 39.835694, -105.359097
fig = plt.figure() 
m = Basemap(projection='merc', lat_0 = p1_lat, lon_0 = p1_lon,
    resolution = 'h', area_thresh = 0.1,
    llcrnrlon=-110, llcrnrlat=36,
    urcrnrlon=-101, urcrnrlat=42)

m.bluemarble()
m.drawstates()
m.drawcounties()

x,y = m(p1_lon, p1_lat)

import matplotlib.animation as animation 
from matplotlib.animation import PillowWriter

point = m.plot(x, y, 'ro', markersize=5)[0]

def init(): 
    point.set_markersize(0)
    return point,

# animation function.  This is called sequentially
def animate(i):
    s = 0.05 * i
    # point.set_linewidth(s)
    # m = Basemap(projection='merc', lat_0 = p1_lat, lon_0 = p1_lon, resolution = 'h', area_thresh = 0.1, llcrnrlon=-110, llcrnrlat=36, urcrnrlon=-101, urcrnrlat=42)
    point.set_markersize(s)
    return point, 
    # m.bluemarble()
    # m.drawstates()
    # m.drawcounties()
    
    # x,y = m(p1_lon, p1_lat)
    # m.plot(x, y, 'yo', markersize=s)

anim = animation.FuncAnimation(plt.gcf(), animate, init_func = init, frames = y_pred_list, interval = 200, blit = True)
# writer = PillowWriter(fps=30)
# anim.save("myMap.gif", writer=writer)

# plt.tight_layout()
plt.show()
# anim.save('animatedMap.mp4', writer = 'sa', fps = 30)
