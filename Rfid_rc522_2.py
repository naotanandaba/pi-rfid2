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
            #1
            Gtk.Window.__init__(self, title="Lets's reard your card")
            self.connect("destroy", Gtk.main_quit)
            self.set_border_width(10)
            #2
            self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
            self.add(self.box)
            self.evbox=Gtk.EventBox()
            self.evbox.override_background_color(0, Gdk.RGBA(0,0,8,1))
            #3
            self.label=Gtk.Label('')
            self.label.set_use_markup(True)
            self.label.set_name("Bluelabel")
            self.label.set_size_request(500,100)
            #4
            self.evbox.add(self.label)
            self.button=Gtk.Button(label="Clear")
            self.button.connect("clicked", self.clicked)
            self.box.pack_start(self.evbox, True, True, 0)
            self.box.pack_start(self.button, True, True, 0)
            #Thread start
            thread = threading.Thread(target=self.scan_uid)
            thread.setDaemon(True)
            thread.start()
            self.show_all
            Gtk.main()
            
        #5
        def clicked(self, widget):
            self.label.set_label('')
            self.evbox.override_background_color(0, Gdk.RGBA(0,0,8,1))
            #Thread start
            thread = threading.Thread(target=self.scan_uid)
            thread.start()
            
        #6
        def scan_uid(self):
            reader = SimpleMFRC522()
            uid = reader.read_id()
            uid_hex = hex(uid).upper()
            self.label.set_label('UID:'+uid+'')
            self.evbox.override_background_color(0, Gdk.RGBA(8,0,0,1))
win = Finestra()