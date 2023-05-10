from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore



@csrf_exempt
def survey(request):
    if request.method == 'POST':
        incoming_msg = request.POST.get('Body', '').strip().lower()
        session = request.session
        session['incoming_msg'] = incoming_msg

        resp = MessagingResponse()
        incoming_msg = session.get('incoming_msg')

        if incoming_msg == 'hi' or incoming_msg == 'hello':
            session['state'] = 'get_name'
            msg = resp.message("hiiiii ... tell me your name please...")
        elif session.get('state') == 'get_name':
            session['name'] = incoming_msg.title()
            session['state'] = 'get_father_name'
            msg = resp.message(f"Hello {session['name']}, please tell me your father's name...")
        elif session.get('state') == 'get_father_name':
            msg = resp.message(f"Hello {session['name']} {incoming_msg.title()} , nice to meet you!")
            session.flush()
        else:
            msg = resp.message(f"Hello there . Please enter 'hi' or 'hello' to start your session.")

        return HttpResponse(str(resp), content_type='text/xml')
    else:
        return HttpResponse("Invalid request", status=400)
    


