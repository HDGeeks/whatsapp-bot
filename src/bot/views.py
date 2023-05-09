from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse


@csrf_exempt
def survey(request):
    if request.method == 'POST':
        incoming_msg = request.POST.get('Body', '').strip().lower()
        resp = MessagingResponse()

        if incoming_msg == 'hello':
            msg = resp.message("Please provide your name:")
        else:
            name = incoming_msg
            msg = resp.message(f"Hello {name}, thank you for participating in our survey!")

        return HttpResponse(str(resp), content_type='text/xml')
    else:
        return HttpResponse("Invalid request", status=400)