import smtplib

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()

sender_email = "abdullahranapakistan@gmail.com"
sender_pass = "wkeg ohdp ljjl lyck"
reciver_email = "muhammadabdullahkhan@gmail.com"


print("Email sent")
