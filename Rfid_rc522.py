#!/usr/bin/env python

import RPi.GPIO as GPIO
import os
from mfrc522 import *
class Rfid_rc522:
    def scan_uid(self):
            reader = SimpleMFRC522()
            uid = reader.read_id()
            uid_hex = hex(uid).upper()
            return uid_hex
if __name__ == "__main__":
    opc=""
    while(opc!="n"):
        os.system("clear")
        print("Scan your card","\t")
        try:
            rf = Rfid_rc522()
            uid = rf.scan_uid()
            print("Your card number is: ","\t")
            print(uid.strip("0X"),"\t")
        finally:
            opc="n"
            opc = input("Scan again (y/n):")
            GPIO.cleanup()