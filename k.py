from twilio.rest import Client
import environ

env = environ.Env()
environ.Env.read_env()

account_sid = env('SID')
auth_token = env('auth_token')
client = Client(account_sid, auth_token)

message = client.messages.create(
 
    from_='whatsapp:+14155238886',
    body='hello abel',
    to='whatsapp:+251973507781'
)


print(message.body)




