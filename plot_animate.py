from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
from matplotlib.animation import PillowWriter
import pickle

locs = 6
p1_lat, p1_lon = 39.835694, -105.359097         #Golden
p2_lat, p2_lon = 38.821557, -104.660183         #Colorado Spring
p3_lat, p3_lon = 39.656653, -106.343787         #Vale
p4_lat, p4_lon = 40.569931, -105.182480         #Fort Collins
p5_lat, p5_lon = 39.044038, -108.594066         #Grand junction
p6_lat, p6_lon = 36.995228, -102.044999         #3points
P_lats = [p1_lat, p2_lat, p3_lat, p4_lat, p5_lat, p6_lat]
P_lons = [p1_lon, p2_lon, p3_lon, p4_lon, p5_lon, p6_lon]
text = ['Location1(Golden,CO)', 'Location2(Colorado Spring,CO)',
        'Location3(Vale,CO)', 'Location4(Fort Collins,CO)',
        'Location5(Grand Junction,CO)', 'Location6(3Points,CO)']

y_pred_list = []
y_true_list = []
for i in range(locs):
    with open("pred_nn{}".format(i+1), "rb") as fp:   # Unpickling
        y_pred_list.append(pickle.load(fp))
    
    with open("true_y{}".format(i+1), "rb") as fp:   # Unpickling
        y_true_list.append(pickle.load(fp))


fig, axes = plt.subplots(2, 1, figsize=(15, 15))

axes[0].set_title("Forecasted DNI using ANN model")
mp = Basemap(projection='merc', lat_0 = p1_lat, lon_0 = p1_lon,resolution = 'h', area_thresh = 0.1,
            llcrnrlon=-110, llcrnrlat=36, urcrnrlon=-101, urcrnrlat=42, ax=axes[0])
mp.bluemarble()
mp.drawstates()
mp.drawcounties()

axes[1].set_title("True DNI")
mt = Basemap(projection='merc', lat_0 = p1_lat, lon_0 = p1_lon,resolution = 'h', area_thresh = 0.1,
            llcrnrlon=-110, llcrnrlat=36, urcrnrlon=-101, urcrnrlat=42, ax=axes[1])
mt.bluemarble()
mt.drawstates()
mt.drawcounties()

# xp_lst = []
# yp_lst = []
# xt_lst = []
# yt_lst = []
points_p = []
points_t = []
for i in range(locs):
    xp,yp = mp(P_lons[i], P_lats[i])
    xt,yt = mt(P_lons[i], P_lats[i])
    # xp_lst.append(xp)
    # yp_lst.append(yp)
    # xt_lst.append(xt)
    # yt_lst.append(yt)

    points_p.append(mp.plot(xp, yp, 'ro', markersize=5)[0])
    points_t.append(mt.plot(xt, yt, 'bo', markersize=5)[0])


# points = [point1, point2]

def init(): 
    for i in range(locs):
        points_p[i].set_markersize(0)
        points_t[i].set_markersize(0)
    
    return points_p + points_t

def data_gen():
    t = 0
    while t < len(y_pred_list):
        for i in range(locs):
            p_p = y_pred_list[i][t]
            p_t = y_true_list[i][t]
        t += 1
        
        yield p_p + p_t

# animation function.  This is called sequentially
def animate(t):
    for i in range(locs): 
        sp = 0.02 * y_pred_list[i][t]
        st = 0.02 * y_true_list[i][t]
        points_p[i].set_markersize(sp)
        points_t[i].set_markersize(st)

    points = points_p + points_t
    return points
    
# anim = animation.FuncAnimation(fig, animate, init_func = init, frames = data_gen, interval = 200, blit = True)
anim = animation.FuncAnimation(fig, animate, init_func = init, frames = len(y_pred_list[0]), interval = 500, blit = True)
# writer = PillowWriter(fps=30)
# anim.save("myMap.gif", writer=writer)

# plt.tight_layout()
plt.show()
# anim.save('animatedMap.mp4', writer = 'sa', fps = 30)
