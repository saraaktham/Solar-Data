from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
from matplotlib.animation import PillowWriter
import pickle


with open("pred_nn", "rb") as fp:   # Unpickling
    y_pred_list = pickle.load(fp)

with open("true_y", "rb") as fp:   # Unpickling
    y_true_list = pickle.load(fp)

p1_lat, p1_lon = 39.835694, -105.359097
fig, axes = plt.subplots(2, 1, figsize=(15, 15))

axes[0].set_title("Forecasted DNI using ANN model")
m1 = Basemap(projection='merc', lat_0 = p1_lat, lon_0 = p1_lon,resolution = 'h', area_thresh = 0.1,
            llcrnrlon=-110, llcrnrlat=36, urcrnrlon=-101, urcrnrlat=42, ax=axes[0])
m1.bluemarble()
m1.drawstates()
m1.drawcounties()

axes[1].set_title("True DNI")
m2 = Basemap(projection='merc', lat_0 = p1_lat, lon_0 = p1_lon,resolution = 'h', area_thresh = 0.1,
            llcrnrlon=-110, llcrnrlat=36, urcrnrlon=-101, urcrnrlat=42, ax=axes[1])
m2.bluemarble()
m2.drawstates()
m2.drawcounties()


x1,y1 = m1(p1_lon, p1_lat)
x2,y2 = m2(p1_lon, p1_lat)


point1 = m1.plot(x1, y1, 'ro', markersize=5)[0]
point2 = m2.plot(x2, y2, 'bo', markersize=5)[0]
points = [point1, point2]

def init(): 
    points[0].set_markersize(0)
    points[1].set_markersize(0)
    return points

def data_gen():
    t = 0
    while t < len(y_pred_list):
        y1 = y_pred_list[t]
        y2 = y_true_list[t]
        t += 1
        yield y1, y2

# animation function.  This is called sequentially
def animate(i):
    s1, s2 = y_pred_list[i], y_true_list[i]
    s1 = 0.02 * s1
    s2 = 0.02 * s2
    points[0].set_markersize(s1)
    points[1].set_markersize(s2)
    # point = (point1, point2)
    return points
    
# anim = animation.FuncAnimation(fig, animate, init_func = init, frames = data_gen, interval = 200, blit = True)
anim = animation.FuncAnimation(fig, animate, init_func = init, frames = len(y_pred_list), interval = 500, blit = True)
# writer = PillowWriter(fps=30)
# anim.save("myMap.gif", writer=writer)

# plt.tight_layout()
plt.show()
# anim.save('animatedMap.mp4', writer = 'sa', fps = 30)
