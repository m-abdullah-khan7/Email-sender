import smtplib

errors = []
filename = input("Enter the file name or file path: ")
line_number = 1
with open(filename , 'r') as file:
    lines = file.readlines()
    for line in lines:

        if line.find('error') != -1 or line.find('issue') != -1:
            errors.append(f"Line number {line_number} has the following error: {line}") 
            errorfound = True
        line_number += 1    
body = "".join(errors)



if errorfound == True:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()

    sender_email = "abdullahranapakistan@gmail.com"
    sender_pass = "gsby rsdo zkmb wzrs" 
    reciver_email = "muhammadabdullahkhanjt@gmail.com"

    connection.login(sender_email, sender_pass)

    subject = "There is a error in the log file"
    body = "".join(errors)
    message = f"Subject: {subject}\n\n{body}"

    connection.sendmail(
        from_addr=sender_email,
        to_addrs=reciver_email,
        msg=message
    )
    print("Email was sent")
    connection.quit