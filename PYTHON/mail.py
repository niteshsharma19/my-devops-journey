
import smtplib

# Create an SMTP session
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

# Start TLS for security
smtp_server.starttls()

# Login to the email account
smtp_server.login('abhimanyuartss@gmail.com','ojky opcd gepj wkut')

# Construct the email message
message = """From: From Person <your_email@gmail.com>
To: To Person <recipient_email@gmail.com>
Subject: SMTP Email Test

This is a test email sent using Python's smtplib.
"""

# Send the email
smtp_server.sendmail('abhimanyuartss@gmail.com','nitesh19b@gmail.com', message)

# Close the connection
smtp_server.quit()