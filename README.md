# job-application-bot

A Python automation script designed to streamline the job application process. This tool allows you to send personalized cold emails with your resume attached to a list of recruiters or hiring managers, while using intelligent delays to avoid spam filters.

🚀 Features
Personalization: Automatically extracts the recipient's first name and company name to customize the email body.

Resume Attachment: Automatically attaches your resume.pdf to every email.

Anti-Spam Logic: Implements randomized delays (45–90 seconds) between emails and "coffee breaks" every 10 emails to mimic human behavior.

Batch Processing: Allows you to choose a specific range of contacts to process (e.g., rows 1–20) to manage daily sending limits.

Error Handling: Skips invalid contacts and logs successful/failed attempts in the console.

🛠️ Prerequisites
Python 3.x installed.

A Gmail account.

Google App Password (Required because standard login passwords won't work with scripts).

⚙️ Setup & Configuration
1. File Structure
Ensure your folder looks like this:

Plaintext
/project-folder
    ├── main.py                # The script file
    ├── resume.pdf             # Your resume (MUST be named exactly this)
    └── hr_contacts_clean.csv  # Your contact list
2. CSV Formatting
Your hr_contacts_clean.csv must follow this specific column order (without headers, or skip the first row in the script):

Format: Name, Email, Company Name

Example:

Code snippet
Amit Sharma, amit.sharma@techcorp.com, Tech Corp
Sarah Jenkins, sarah.j@startuplab.io, Startup Lab
3. Google App Password
Go to your Google Account Security Settings.

Enable 2-Step Verification.

Search for App Passwords.

Create a new app password (name it "Python Script").

Copy the 16-character code generated.
4. Configure the Script
Open main.py and update the configuration section:

Python
# ================= CONFIGURATION =================
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "xxxx xxxx xxxx xxxx"  # Paste your 16-char App Password here
# =================================================
🏃‍♂️ How to Run
Open your terminal or command prompt.

Navigate to the project folder.

Run the script:

Bash
python main.py
Follow the on-screen prompts to select which rows to process:

Plaintext
Start at row number (1 - 100): 1
How many emails to send now? (Rec: 20-50): 20
⚠️ Important Safety Notes
Daily Limits: Gmail typically limits sending to ~500 emails/day, but for cold outreach, it is recommended to stay under 50 emails per day to avoid having your account flagged as spam.

Credentials: Never upload your main.py with your real password to GitHub. Use environment variables or a separate config file if sharing the code.
