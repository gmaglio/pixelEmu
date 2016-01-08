#!/usr/bin/python2.7
from celery import Celery
from pixelEmu import renderScreen

app = Celery('tasks', broker='amqp://guest@localhost//', backend='redis://localhost')

@app.task
def render():
    renderScreen() 
