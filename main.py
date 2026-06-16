import smtplib
import csv
import time
import random
import sys
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# ================= CONFIGURATION =================
# 1. Your Gmail Address
MY_EMAIL = "yourgmail@gmail.com"

# 2. Your Google App Password (NOT your login password)
# Generate here: https://myaccount.google.com/apppasswords
MY_PASSWORD = "xxxx xxxx xxxx xxxx" 

# 3. Files
CSV_FILE = "hr_contacts_clean.csv"
RESUME_FILE = "resume.pdf"
# =================================================

def send_application(hr_name, hr_email, company_name):
    msg = MIMEMultipart()
    msg['From'] = MY_EMAIL
    msg['To'] = hr_email
    msg['Subject'] = f"Application for Developer Role - {hr_name}"

    # --- PERSONALIZATION LOGIC ---
    # 1. Get First Name (e.g., "Amit" from "Amit Sharma")
    first_name = hr_name.split()[0] if hr_name else "Hiring Team"
    
    # 2. Clean Company Name (Optional: falls back to "your company" if missing)
    if not company_name or company_name.lower() == "unknown":
        company_text = "your company"
    else:
        company_text = company_name

    # --- EMAIL BODY ---
    body = f"""
    Hi {first_name},

    I hope this email finds you well.

    I am writing to express my interest in technical roles at {company_text}. 
    I have strong knowledge in Python, Automation, and Much more.

    I have attached my resume for your review. I would love to connect and discuss how I can contribute to your engineering team.

   
    msg.attach(MIMEText(body, 'plain'))

    # --- ATTACH RESUME ---
    try:
        with open(RESUME_FILE, "rb") as attachment:
            p = MIMEBase('application', 'octet-stream')
            p.set_payload(attachment.read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', f"attachment; filename= {RESUME_FILE}")
            msg.attach(p)
    except FileNotFoundError:
        print(f"\n❌ CRITICAL ERROR: Could not find '{RESUME_FILE}' in this folder.")
        print("Please rename your resume file to 'resume.pdf' and try again.")
        sys.exit()

    # --- SENDING ---
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(MY_EMAIL, MY_PASSWORD)
        text = msg.as_string()
        server.sendmail(MY_EMAIL, hr_email, text)
        server.quit()
        print(f"✅ Sent to: {first_name} at {company_text} ({hr_email})")
        return True
    except Exception as e:
        print(f"❌ FAILED to send to {hr_email}: {e}")
        return False

def main():
    # 1. Check if CSV exists
    if not os.path.exists(CSV_FILE):
        print(f"❌ Error: '{CSV_FILE}' not found. Please run the extraction script first.")
        return

    # 2. Load Contacts
    contacts = []
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader) # Skip header row
        for row in reader:
            # Row format: [Name, Email, Company]
            if len(row) >= 3:
                contacts.append(row)

    total = len(contacts)
    print(f"\nLoaded {total} contacts ready to process.")
    print("--------------------------------------------------")
    print("⚠️  SAFETY TIP: Send max 50 emails per day to avoid spam filters.")
    print("--------------------------------------------------")

    # 3. User Input for Batching
    try:
        start_num = int(input(f"Start at row number (1 - {total}): "))
        count_num = int(input("How many emails to send now? (Rec: 20-50): "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    start_index = start_num - 1
    end_index = start_index + count_num

    print(f"\n🚀 Starting batch: Row {start_num} to {min(end_index, total)}...")
    
    sent_counter = 0

    # 4. Processing Loop
    for i in range(start_index, min(end_index, total)):
        name = contacts[i][0]
        email = contacts[i][1]
        company = contacts[i][2]

        success = send_application(name, email, company)
        
        if success:
            sent_counter += 1
            
            # --- HUMAN TIMING DELAY ---
            # Wait 45 to 90 seconds between emails
            wait_time = random.randint(45, 90)
            print(f"⏳ Waiting {wait_time}s...")
            time.sleep(wait_time)

            # Extra break every 10 emails
            if sent_counter % 10 == 0:
                print("☕ Taking a 3-minute coffee break (Safety Pause)...")
                time.sleep(180)

    print(f"\n🎉 Batch Complete! Sent {sent_counter} emails.")

if __name__ == "__main__":

    main()
