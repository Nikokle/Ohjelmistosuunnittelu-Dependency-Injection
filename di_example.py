
# Esimerkki 1: Ilman Depency Injectionia

class EmailSender:
    # Tämä luokka on riippuvuus
    # Sen vastuulla on viestin lähettäminen
    def send(self, message):
        print(f"Email sent: {message}")


class BadNotificationService:
    def __init__(self):
        # TIGHT COUPLING:
        # Tämä luokka luo oman riippuvuutensa
        # Palvelu on suoraan sidottu EmailSender-luokkaan.
        self.sender = EmailSender()

    def notify(self, message):
        # Palvelu käyttää riippuvuutta.
        self.sender.send(message)


#Esimerkki 2: Dependency Injectionin kanssa


class GoodNotificationService:
    def __init__(self, sender):
        # DEPENDENCY INJECTION tapahtuu tässä
        # Riippuvuus (sender) annetaan ulkopuolelta
        # sen sijaan että se luotaisiin luokan sisällä
        self.sender = sender

    def notify(self, message):
        # Palvelu käyttää injektoitua riippuvuutta
        self.sender.send(message)


# Riippuvuus luodaan palvelun ulkopuolella
email_sender = EmailSender()

# Riippuvuus injektoidaan palveluun
good_service = GoodNotificationService(email_sender)

good_service.notify("Hello from good example")


#Esimerkki 3: Riippuvuutta on helppo vaihtaa


class SmsSender:
    def send(self, message):
        print(f"SMS sent: {message}")


# Luodaan toinen riippuvuus
sms_sender = SmsSender()

# Injektoidaan toinen riippuvuus
sms_service = GoodNotificationService(sms_sender)

# Sama palvelu toimii molemmilla tavoilla
sms_service.notify("Hello from SMS example")


#Esimerkki 4: Depency Injection ja testaus


#Käytettään Mock-oliota riippuvuutta luodessa
class MockSender:
    def send(self, message):
        print(f"[TEST] Message captured: {message}")


#Injektoidaan riippuvuus Mock-oliolla
mock_sender = MockSender()
service = GoodNotificationService(mock_sender)

service.notify("Test message")