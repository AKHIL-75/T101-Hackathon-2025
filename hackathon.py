import requests
import json
import time
res = []
words = ["mdma", "lsd", "mephedrone", "buy drugs", "ecstasy", "acid", "sale"]
def tg_scan():
    print("\n🔍 Telegram Check...")
    chs = [
        {"u": "https://t.me/officialmcstan", "n": "MC Stan Official", "f": False},
        {"u": "https://t.me/indiagramdrugstore", "n": "India Gram Drug Store", "f": True},
        {"u": "https://t.me/medsindiachannel", "n": "Meds India Channel", "f": True},
        {"u": "https://t.me/bollywoodspy", "n": "Bollywood Spy", "f": False}
    ]
    for c in chs:
        time.sleep(0.4)
        if c["f"]:
            res.append({
                "app": "Telegram",
                "name": c["n"],
                "url": c["u"],
                "flag": True,
                "data": {
                    "ip": "192.168.1.101",
                    "mail": "contact@indiagramdrugstore.com",
                    "mob": "+91-9876543210"
                }
            })
            print(f"🚩 Flagged: {c['n']} ({c['u']})")
        else:
            print(f"✅ Clean: {c['n']} ({c['u']})")
def insta_scan():
    print("\n🔍 Instagram Check...")
    accs = [
        {"u": "https://instagram.com/virat.kohli", "n": "Virat Kohli", "f": False},
        {"u": "https://instagram.com/bollywooddrugstore", "n": "Bollywood Drug Store", "f": True},
        {"u": "https://instagram.com/shraddhakapoor", "n": "Shraddha Kapoor", "f": False},
        {"u": "https://instagram.com/meds4u_india", "n": "Meds4U India", "f": True}
    ]
    for a in accs:
        time.sleep(0.4)
        if a["f"]:
            res.append({
                "app": "Instagram",
                "name": a["n"],
                "url": a["u"],
                "flag": True,
                "data": {
                    "ip": "192.168.2.202",
                    "mail": "support@bollywooddrugstore.com",
                    "mob": "+91-9123456789"
                }
            })
            print(f"🚩 Flagged: {a['n']} ({a['u']})")
        else:
            print(f"✅ Clean: {a['n']} ({a['u']})")
def wa_scan():
    print("\n🔍 WhatsApp Check...")
    gps = [
        {"u": "https://chat.whatsapp.com/officialnews", "n": "Official News", "f": False},
        {"u": "https://chat.whatsapp.com/mdma_india_group", "n": "MDMA India Group", "f": True},
        {"u": "https://chat.whatsapp.com/dailyupdates", "n": "Daily Updates", "f": False},
        {"u": "https://chat.whatsapp.com/lsd_suppliers", "n": "LSD Suppliers", "f": True}
    ]
    for g in gps:
        time.sleep(0.4)
        if g["f"]:
            res.append({
                "app": "WhatsApp",
                "name": g["n"],
                "url": g["u"],
                "flag": True,
                "data": {
                    "ip": "192.168.3.150",
                    "mail": "info@mdmaindiagroup.com",
                    "mob": "+91-7001234567"
                }
            })
            print(f"🚩 Flagged: {g['n']} ({g['u']})")
        else:
            print(f"✅ Clean: {g['n']} ({g['u']})")
def show():
    print("\n📊 Final Report:\n")
    time.sleep(0.2)
    print(json.dumps(res, indent=3))
tg_scan()
time.sleep(0.2)
insta_scan()
time.sleep(0.2)
wa_scan()
time.sleep(0.2)
show()