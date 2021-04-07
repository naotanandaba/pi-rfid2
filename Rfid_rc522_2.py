import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gdk
import RPi.GPIO as GPIO
import os
from mfrc522 import *
import Rfid_rc522
import threading

class Finestra(Gtk.Window):
        def __init__(self):
            window = Gtk.Window(title="Read your card")
            box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
            window.add(box)
            evbox = Gtk.EventBox()
            self.label=Gtk.Label('Please, login with your university card')
            evbox.add(self.label)
            button = Gtk.Button(label="Clear")
            button.connect("clicked", self.clicked)
            box.pack_start(evbox, True, True, 0)
            box.pack_start(button, True, True, 0)
            window.connect("destroy", Gtk.main_quit)
            thread = threading.Thread(target=self.scan_uid)
            thread.setDaemon(True)
            thread.start()
            window.show_all()
            Gtk.main()
            
        def clicked(self, widget):
            thread = threading.Thread(target = self.scan_uid)
            thread.start
            
        def scan_uid(self):
            reader = SimpleMFRC522()
            uid = reader.read_id()
            uid_hex = hex(uid).upper()
            self.label.set_text('UID: '+uid_hex.strip("0X")+'')

win = Finestra()
