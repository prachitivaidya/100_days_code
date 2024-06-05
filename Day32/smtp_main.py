import smtplib

my_email = "Septdac@gmail.com"
password = "pswd modify security"

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()  # to make connection secure
    connection.login(user = my_email, password = password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="septdac@gmail.com",
        msg="Subject:Hello\n\nthis is Body of email"
    )
