# import csv
# import random
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# # Read CSV file with contacts (make sure file is in the same directory or provide full path)
# contacts_list = []
# with open('demo.csv', newline='', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         contacts_list.append(row)

# # Define a base message template. Customize as needed.
# base_message = "Hello {name}, how are you hoping you're doing great.. your CNIC is {cnic} is  regisered in Pser..know you are eligible for applying any govt scheme. join this group https://chat.whatsapp.com/IlVQ0NUGjR1HVVWbtn7SdU."

# # Initialize the Selenium WebDriver (ensure chromedriver is in the same folder or set PATH accordingly)
# driver = webdriver.Chrome()
# driver.get("https://web.whatsapp.com/")

# input("Scan the QR code in WhatsApp Web and press Enter...")

# for contact in contacts_list:
#     phone = contact['phone']
#     name = contact['name']
#     cnic = contact['cnic']
    
#     # Customize the message for each contact
#     message = base_message.format(name=name, cnic=cnic)
    
#     # Open WhatsApp chat with the pre-filled message
#     driver.get(f"https://web.whatsapp.com/send?phone={phone}&text={message}")
#     time.sleep(8)  # Wait for the chat to load
    
#     try:
#         # Look for the send button and click it
#         send_button = driver.find_element(By.XPATH, '//div[@class="x123j3cw xs9asl8 x9f619 x78zum5 x6s0dn4 xl56j7k x1ofbdpd x100vrsf x1fns5xo"]')
#         send_button.click()
#         print(f"Message sent to {phone}")
#     except Exception as e:
#         print(f"Failed to send message to {phone}: {e}")
    
#     # Wait a random period between messages to reduce detection risk
#     time.sleep(random.randint(5, 10))

# driver.quit()






import csv
import random
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# File to track sent messages
sent_numbers_file = "sent_numbers.txt"

# Load sent numbers into a set
if os.path.exists(sent_numbers_file):
    with open(sent_numbers_file, "r") as f:
        sent_numbers = set(f.read().splitlines())
else:
    sent_numbers = set()

# Read CSV file with contacts
contacts_list = []
with open("monsaf.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        contacts_list.append(row)

# Message template
base_message = '''Aslam_O_Alikum Mrs/Mr {name} hoping you're doing great.. your CNIC # {cnic} is registered in PSER.. know you are eligible for applying in any govt scheme. Join this group for more update:  https://chat.whatsapp.com/IlVQ0NUGjR1HVVWbtn7SdU. /n
 عید کے بعد نئے سروئے میں اندراج کےلئے یا کسی بھی سکیم میں اپلائی کے لئے یا اپنے سروئے کا موجودہ سٹیٹس جاننے کےلئے اگلے مرحلے کو کرنے کےلئے اپنے سیکٹری یونین کونسل اختر ورک اور کمیوٹر آپریٹر منصف علی سے رابطہ میں رہیے۔ 
http://wa.me//923116940272
'''

# Initialize the Selenium WebDriver
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
input("Scan the QR code in WhatsApp Web and press Enter...")

for contact in contacts_list:
    phone = contact["phone"]
    
    # Skip if message was already sent
    if phone in sent_numbers:
        print(f"Skipping {phone}, already processed.")
        continue  

    name = contact["name"]
    cnic = contact["cnic"]

    message = base_message.format(name=name, cnic=cnic)
    
    # Open WhatsApp chat
    driver.get(f"https://web.whatsapp.com/send?phone={phone}&text={message}")
    time.sleep(8)  # Wait for chat to load

    try:
        send_button = driver.find_element(By.XPATH, '//div[@class="x123j3cw xs9asl8 x9f619 x78zum5 x6s0dn4 xl56j7k x1ofbdpd x100vrsf x1fns5xo"]')
        send_button.click()
        print(f"Message sent to {phone}")

        # Add number to sent_numbers file
        with open(sent_numbers_file, "a") as f:
            f.write(phone + "\n")
            
    except Exception as e:
        print(f"Failed to send message to {phone}: {e}")
    
    time.sleep(random.randint(10, 15))  # Wait before sending the next message

driver.quit()
