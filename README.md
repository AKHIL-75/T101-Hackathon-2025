🚨 Social Platform Drug Activity Scanner
This Python script simulates a scanner tool that flags Telegram, Instagram, and WhatsApp groups or accounts suspected of promoting or selling illicit drugs such as MDMA, LSD, ecstasy, etc. 
It's intended for educational or research purposes only, such as learning how data could be organized and flagged in content moderation systems.

📌 Features

Scans predefined links from Telegram, Instagram, and WhatsApp.
Flags suspicious channels or groups based on hardcoded flags.
Simulates detection of drug-related activity.
Shows a final report with flagged entries including mock IP, email, and phone.

🧪 Sample Output

🔍 Telegram Check...
✅ Clean: MC Stan Official (https://t.me/officialmcstan)
🚩 Flagged: India Gram Drug Store (https://t.me/indiagramdrugstore)
🚩 Flagged: Meds India Channel (https://t.me/medsindiachannel)
✅ Clean: Bollywood Spy (https://t.me/bollywoodspy)

🔍 Instagram Check...
✅ Clean: Virat Kohli (https://instagram.com/virat.kohli)
🚩 Flagged: Bollywood Drug Store (https://instagram.com/bollywooddrugstore)
✅ Clean: Shraddha Kapoor (https://instagram.com/shraddhakapoor)
🚩 Flagged: Meds4U India (https://instagram.com/meds4u_india)

🔍 WhatsApp Check...
✅ Clean: Official News (https://chat.whatsapp.com/officialnews)
🚩 Flagged: MDMA India Group (https://chat.whatsapp.com/mdma_india_group)
✅ Clean: Daily Updates (https://chat.whatsapp.com/dailyupdates)
🚩 Flagged: LSD Suppliers (https://chat.whatsapp.com/lsd_suppliers)

📊 Final Report:

[
   {
      "app": "Telegram",
      "name": "India Gram Drug Store",
      "url": "https://t.me/indiagramdrugstore",
      "flag": true,
      "data": {
         "ip": "192.168.1.101",
         "mail": "contact@indiagramdrugstore.com",
         "mob": "+91-9876543210"
      }
   },
   {
      "app": "Telegram",
      "name": "Meds India Channel",
      "url": "https://t.me/medsindiachannel",
      "flag": true,
      "data": {
         "ip": "192.168.1.101",
         "mail": "contact@indiagramdrugstore.com",
         "mob": "+91-9876543210"
      }
   },
   {
      "app": "Instagram",
      "name": "Bollywood Drug Store",
      "url": "https://instagram.com/bollywooddrugstore",
      "flag": true,
      "data": {
         "ip": "192.168.2.202",
         "mail": "support@bollywooddrugstore.com",
         "mob": "+91-9123456789"
      }
   },
   {
      "app": "Instagram",
      "name": "Meds4U India",
      "url": "https://instagram.com/meds4u_india",
      "flag": true,
      "data": {
         "ip": "192.168.2.202",
         "mail": "support@bollywooddrugstore.com",
         "mob": "+91-9123456789"
      }
   },
   {
      "app": "WhatsApp",
      "name": "MDMA India Group",
      "url": "https://chat.whatsapp.com/mdma_india_group",
      "flag": true,
      "data": {
         "ip": "192.168.3.150",
         "mail": "info@mdmaindiagroup.com",
         "mob": "+91-7001234567"
      }
   },
   {
      "app": "WhatsApp",
      "name": "LSD Suppliers",
      "url": "https://chat.whatsapp.com/lsd_suppliers",
      "flag": true,
      "data": {
         "ip": "192.168.3.150",
         "mail": "info@mdmaindiagroup.com",
         "mob": "+91-7001234567"
      }
   }
]
