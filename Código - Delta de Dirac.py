import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import quad

plt.style.use("dark_background")

#Animación de la aceleración dada con gráfica

def f(x, e):
    
    return 1/(2*e) if -e <= x <= e else 0

e = np.linspace(0.5, 0.0001, 120)
t = np.linspace(-1, 1, 1000)
y = [f(i, e[0]) for i in t]

fig = plt.figure(figsize=(16, 9))
ax = plt.axes()

ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(("axes", 0))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylim([-0.1, 6])

ax.plot(t, y)
ax.text(-1, 6, "$\\varepsilon = $" + str(e[0]))

#fig.savefig("Fuerza.png", dpi=200)

def update(g):
    
    ax.cla()
    ax.spines['left'].set_position(("data", 0))
    y = [f(i, g) for i in t]
    ax.plot(t, y)
    ax.text(-1, 6, "$\\varepsilon = $" + str(round(g, 3)))
    ax.set_ylim([-0.1, 6])
    
anim = FuncAnimation(fig, update, frames=e, interval=13)
#anim.save("Fuerza.gif", dpi=200)

#Función velocidad estática

def v(t):
    
    return 1 if t >= 0 else 0

t1, t2 = np.linspace(-1, -0.001, 100), np.linspace(0.001, 1, 100)
y1, y2 = [v(i) for i in t1], [v(i) for i in t2]

fig1 = plt.figure(figsize=(16, 9))
ax1 = plt.axes()

ax1.plot(t1, y1, c="cyan")
ax1.plot(t2, y2, c="yellow")
ax1.scatter(0, 1, c="yellow")
ax1.scatter(0, 0, c="cyan")

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

#fig1.savefig("Velocidad Estática.png", dpi=200)

#Velocidad con animación

def ve(t, e):
    
    if t < -e: return 0
    if t > e: return 1
    
    return t/(2*e) + 1/2

y = [ve(i, e[0]) for i in t]

fig2 = plt.figure(figsize=(16, 9))
ax2 = plt.axes()

ax2.spines['left'].set_position(('data', 0))
ax2.spines['bottom'].set_position(("axes", 0))
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.set_ylim([-0.1, 1.2])

ax2.plot(t, y)
ax2.plot([-e[0]]*2, [-0.1, 1.2], "--", c="white")
ax2.plot([e[0]]*2, [-0.1, 1.2], "--", c="white")
ax2.text(-1, 1.2, "$\\varepsilon = $" + str(e[0]))
ax2.text(-e[0]-0.05, 1.2, "$-\\varepsilon$")
ax2.text(e[0]+0.01, 1.2, "$+\\varepsilon$")

#fig2.savefig("Velocidad Variante.png", dpi=200)

def update1(g):
    
    ax2.cla()
    ax2.spines['left'].set_position(("data", 0))
    y = [ve(i, g) for i in t]
    ax2.plot(t, y)
    ax2.plot([-g]*2, [-0.1, 1.2], "--", c="white")
    ax2.plot([g]*2, [-0.1, 1.2], "--", c="white")
    ax2.text(-1, 1.2, "$\\varepsilon = $" + str(round(g, 3)))
    ax2.text(-g-0.05, 1.2, "$-\\varepsilon$")
    ax2.text(g+0.01, 1.2, "$+\\varepsilon$")
    ax2.set_ylim([-0.1, 1.2])
    
anim1 = FuncAnimation(fig2, update1, frames=e, interval=13)
#anim1.save("Velocidad Variante.gif", dpi=200)

#Distribución gaussiana

def fg(x, n):
    
    return n*np.exp(-(n**2)*(x**2))/np.sqrt(np.pi)

n = np.linspace(1, 20, 120)
tg = np.linspace(-2, 2, 1000)
yg = [fg(i, n[0]) for i in tg]

figG = plt.figure(figsize=(16, 9))
axG = plt.axes()

axG.spines['left'].set_position(('data', 0))
axG.spines['bottom'].set_position(("axes", 0))
axG.spines['top'].set_visible(False)
axG.spines['right'].set_visible(False)
axG.set_ylim([-0.1, 6])

axG.plot(tg, yg)
axG.text(-2, 6, "$n = $" + str(int(n[0])))

#figG.savefig("Gaussiana.png", dpi=200)

def updateG(frame):
    
    axG.cla()
    axG.spines['left'].set_position(('data', 0))
    axG.spines['bottom'].set_position(("axes", 0))
    yg = [fg(i, frame) for i in tg]
    axG.set_ylim([-0.1, 6])

    axG.plot(tg, yg)
    axG.text(-2, 6, "$n = $" + str(int(frame)))
    
aniG = FuncAnimation(figG, updateG, frames=n, interval=13)
#aniG.save("Gaussiana.gif", dpi=200)

#Parecida a arcotangente

def ftg(x, n):
    
    return n/(((n**2)*(x**2)+1)*np.pi)

nTg = np.linspace(1, 30, 120)
yTg = [ftg(i, nTg[0]) for i in tg]

figTg = plt.figure(figsize=(16, 9))
axTg = plt.axes()

axTg.spines['left'].set_position(('data', 0))
axTg.spines['bottom'].set_position(("axes", 0))
axTg.spines['top'].set_visible(False)
axTg.spines['right'].set_visible(False)
axTg.set_ylim([-0.1, 6])

axTg.plot(tg, yTg)
axTg.text(-2, 6, "$n = $" + str(int(nTg[0])))

#figTg.savefig("Arco.png", dpi=200)

def updateTg(frame):
    
    axTg.cla()
    axTg.spines['left'].set_position(('data', 0))
    axTg.spines['bottom'].set_position(("axes", 0))
    yTg = [ftg(i, frame) for i in tg]
    axTg.set_ylim([-0.1, 6])

    axTg.plot(tg, yTg)
    axTg.text(-2, 6, "$n = $" + str(int(frame)))
    
aniTg = FuncAnimation(figTg, updateTg, frames=nTg, interval=16)
#aniTg.save("Arco.gif", dpi=200)

#Seno

def fsen(x, n):
    
    return np.sin(n*x)/(np.pi*x)

ySen = [fsen(i, nTg[0]) for i in tg]

figSen = plt.figure(figsize=(16, 9))
axSen = plt.axes()

axSen.spines['left'].set_position(('data', 0))
axSen.spines['bottom'].set_position(("data", 0))
axSen.spines['top'].set_visible(False)
axSen.spines['right'].set_visible(False)
axSen.set_ylim([-3, 6])

axSen.plot(tg, ySen)
axSen.text(-2, 3, "$n = $" + str(int(nTg[0])))

#figSen.savefig("Seno.png", dpi=200)

def updateSen(frame):
    
    axSen.cla()
    axSen.spines['left'].set_position(('data', 0))
    axSen.spines['bottom'].set_position(("data", 0))
    ySen = [fsen(i, frame) for i in tg]
    axSen.set_ylim([-3, 6])

    axSen.plot(tg, ySen)
    axSen.text(-2, 6, "$n = $" + str(int(frame)))
    
aniSen = FuncAnimation(figSen, updateSen, frames=n, interval=16)
#aniSen.save("Seno.gif", dpi=200)

def updateIntegral(frame, ax, f, ymin, ymax):
    
    ax.cla()
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(("data", 0))
    ax.set_ylim([ymin, ymax])
    
    y = [f(i, frame) for i in t]
    a = quad(f, -np.inf, np.inf, args=(frame,))[0]
    
    ax.plot(t, y)
    ax.fill_between(t, y, alpha=0.5)
    ax.text(min(t), ymax, "$n = $" + str(int(frame)) + "\n$Área = $" + str(round(a, 12)))

def animateIntegral(f, t, name, nmax=20, res=200, interval=10, ymin = -0.1, ymax=6):
    
    n = np.linspace(1, nmax, res)
    y = [f(i, n[0]) for i in t]
    a = quad(f, -np.inf, np.inf, args=(n[0]))[0]
    
    #Dibujamos el frame 0
    
    fig = plt.figure(figsize=(16, 9))
    ax = plt.axes()
    
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(("data", 0))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylim([ymin, ymax])
    
    ax.plot(t, y)
    ax.fill_between(t, y, alpha=0.5)
    ax.text(min(t), ymax, "$n = $" + str(int(n[0])) + "$\\$" + "\n$Área = $" + str(round(a, 12)))
    
    fig.savefig(name + ".png", dpi=200)
    
    ani = FuncAnimation(fig, updateIntegral, frames=n, interval=interval, fargs=(ax, f, ymin, ymax))
    ani.save(name + ".gif", dpi=200)

#animateIntegral(fg, t, "Gaussiana Integral")
#animateIntegral(ftg, tg, "Arcotangente Integral", nmax=30)
#animateIntegral(fsen, tg, "Seno integral", nmax=200, ymin=-3, res=1000)

def vn(x, n):
    
    return n/2 if -1/n <= x <= 1/n else 0

#animateIntegral(vn, t, "Velocidad Integral")

def vnf(x, n, f):
    
    return f(x)*n/2 if -1/n <= x <= 1/n else 0

animateIntegral(lambda x, n: vnf(x, n, lambda x: x**2 + 1), t, "Delta con Función")
animateIntegral(lambda x, n: fg(x, n)*(x**2 + 1), t, "Delta con Función - 2")

plt.show()