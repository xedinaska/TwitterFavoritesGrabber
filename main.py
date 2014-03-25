#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Alex P'
__email__ = 'Xedinaska@gmail.com'
__version__ = '0.0.1'
__date__ = '2014-03-25'

from Tkinter import *
from TwiOAuthHandler import TwiOAuthHandler
from TwiFavoritesGrabber import TwiFavoritesGrabber


def get_favorites(auth):
    favorites_grabber = TwiFavoritesGrabber(auth)
    favorites_grabber.grab()


def authenticate_user(ev):
    access_token = access_token_entry.get()
    access_token_secret = access_token_secret_entry.get()

    consumer_key = consumer_key_entry.get()
    consumer_key_secret = consumer_secret_entry.get()

    oauthConnector = TwiOAuthHandler(consumer_key, consumer_key_secret, access_token, access_token_secret)
    auth = oauthConnector.request_auth_object()

    get_favorites(auth)

#start draw window
root = Tk(screenName="Favorites Grabber", className="Favorites Grabber")

panelFrame = Frame(root, height=80, bg='white')
textFrame = Frame(root, height=320, width=400)

panelFrame.pack(side='bottom', fill='x')
textFrame.pack(side='top', fill='both', expand=1)

access_token_entry = Entry(textFrame)
access_token_secret_entry = Entry(textFrame)
access_token_label = Label(textFrame, text="Enter Access Token", font="Arial 16")
access_token_secret_label = Label(textFrame, text="Enter Access Token Secret", font="Arial 16")

consumer_key_entry = Entry(textFrame)
consumer_secret_entry = Entry(textFrame)
consumer_key_label = Label(textFrame, text="Enter Consumer Key", font="Arial 16")
consumer_secret_label = Label(textFrame, text="Enter Consumer Key Secret", font="Arial 16")


access_token_label.place(x=90, y=15, width=220, height=20)
access_token_entry.place(x=90, y=40, width=220, height=40)

access_token_secret_label.place(x=90, y=95, width=220, height=20)
access_token_secret_entry.place(x=90, y=120, width=220, height=40)

consumer_key_label.place(x=90, y=175, width=220, height=20)
consumer_key_entry.place(x=90, y=200, width=220, height=40)

consumer_secret_label.place(x=90, y=255, width=220, height=20)
consumer_secret_entry.place(x=90, y=280, width=220, height=40)

loadBtn = Button(panelFrame, text='Get Favorites')
loadBtn.place(x=90, y=10, width=220, height=80)

loadBtn.bind("<Button-1>", authenticate_user)

if __name__ == "__main__":
    root.mainloop()

