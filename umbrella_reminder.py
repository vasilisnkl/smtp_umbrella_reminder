import schedule 
import smtplib 
from requests_html import HTMLSession

def app():
    session = HTMLSession()
    url = f"https://www.google.com/search?q=weather+athens"

    root = session.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})
    temperature = root.html.find('span#wob_tm', first=True).text
    weather = root.html.find('span#wob_dc', first=True).text

    server = smtplib.SMTP('smtp.gmail.com', 587)
    print(server.ehlo())
    print(server.starttls())

    server.login('gmail', 'app password')

    if weather == 'Βροχερός' or weather == 'Νεφελώδης':

        subject = "Υπευνθύμιση Ομπρέλας"
        body = f"Πάρε ομπρέλα μαζί σου.\nΚαιρός για σήμερα στην Αθήνα: {weather}, {temperature} βαθμοί."

        msg = f"Subject:{subject}\n\n{body}\n\nΜε εκτίμηση,\nΟ μελλοντικός σου εαυτός".encode('utf-8')
        print(msg)

        server.sendmail("b.nikolaou20@gmail.com", 'b.nikolaou20@gmail.com', msg)

        print("Email Sent!")

        server.quit()

schedule.every().day.at("10:00").do(app)

while True:
    schedule.run_pending()