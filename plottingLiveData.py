import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
from flask import Flask
from flask import Markup
from flask import Flask, make_response
from flask import render_template
import numpy as np


app = Flask(__name__)


style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1,)


def animate(i):
    pull_data = open("twitter_results_to_plot.txt", "r").read()   # This file contains positive and negatives
    pull_data_calais = open("output_Calais.txt", "r").read()      # Calais only outputs the raw texts with a a -ve/+ve value telling if the raw text is negative or positive respectivelt
    lines_calais = pull_data.split('\n')
    lines = pull_data.split('\n')
    xar = []
    yar = []

    xxar = []
    yyar = []

    x = 0
    y = 0
    x1 = 0
    y1 = 0
    for l in lines[500:]: # Logic behind plotting the graph. Plot only the first 500 pooints to conserve data bundle :)
        x += 1
        if "pos" in l:   #Any positive review, increment by one on y-axis
            y += 1
        elif "neg" in l:
            y -= 1

    for l in lines_calais[500:]:      #  Plot calais results
        if "pos" in l:   #Any positive review, increment by one on y-axis
            y1 += 1
        elif "neg" in l:
            y1 -= 1       #Any nnegative review, derement by one on y-axis

        xar.append(x)   # Fill the above in the xar/yar arrays for plotting
        yar.append(y)

        xxar.append(x1)   # Fill the above in the xar/yar arrays for plotting
        yyar.append(y1)

    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig,animate,interval=1000)  #Refresh this update periodically every second
fig = plt.figure()
#figure.savefig('C:/Users/danial/PycharmProjects/safaricom_social_tracker_application/static/img/sine_wave_plot.svg')
plt.show()    #Render using ggplot



#@app.route('/')
#def chart():
#    return render_template("index.html")

#if __name__ == "__main__":
#    app.run(host='127.0.0.1', port=5000)
