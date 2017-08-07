import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
from flask import Flask
from flask import Markup
from flask import Flask, make_response
from flask import render_template
import numpy as np
import random
import threading
import sched, time


app = Flask(__name__)


style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1,)

s = sched.scheduler(time.time, time.sleep)
def animate():
    #threading.Timer(5.0, animate).start()
    pull_data = open("twitter_out.txt", "r").read()
    lines = pull_data.split('\n')
    xar = []
    yar = []

    x = 0
    y = 0

    for l in lines:
        x += 1
        if "pos" in l:
            y += 1
        elif "neg" in l:
            y -= 1

        #xar.append(x)
        #yar.append(y)
        xar = random.randrange(100, 105)
        yar = random.randrange(1, 99)
        s.enter(1, 1, animate, ())
    return xar, yar
#    ax1.clear()
#    ax1.plot(xar,yar)
#animate()
fig = plt.figure()
ani = animation.FuncAnimation(fig,animate,interval=2000)
s.enter(1, 1, animate, ())
#figure.savefig('C:/Users/danial/PycharmProjects/SentAnalysis/static/img/sine_wave_plot.svg')
#plt.show()


def printit():
  threading.Timer(1.0, printit).start()
  yar = random.random() * 100
  xar = random.random() * 10
  return xar, yar


@app.route('/')
def chart():
    threading.Timer(1.0, chart).start()
    logo = 4+2 #Testing purposes
    xar, yar = printit()

    #threading.Timer(1.0, chart).start()

    return render_template("graphing2.html", xar=xar, yar=yar, logo=logo)
    #return render_template("graphing2.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
