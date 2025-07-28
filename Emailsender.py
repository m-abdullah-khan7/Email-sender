import smtplib

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()

sender_email = "abdullahranapakistan@gmail.com"
sender_pass = "wkeg ohdp ljjl lyck" #you need to add a new one this one will no longer work i removed it
reciver_email = "muhammadabdullahkhanjt@gmail.com"

connection.login(sender_email, sender_pass)

subject = "Sending my first mail through python"
body = "This is the body of the text and has the message of the text and does not really have anything import and husnain is pretty dumb"
message = f"Subject: {subject}\n\n{body}"

connection.sendmail(
    from_addr=sender_email,
    to_addrs=reciver_email,
    msg=message
)
print("Email was sent")
connection.quit