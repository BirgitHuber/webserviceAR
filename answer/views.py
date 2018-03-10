
import base64
import datetime

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from answer.recognise_object import decode_image
from .models import Code


# post method: receive code and return info text
@csrf_exempt
def code_return(request):
    # receive the data from client
    post_data = request.POST
    req_code = post_data.get('code')
    # get information from database
    obj = Code.objects.get(code=req_code)
    ret_string = obj.code + " + "+obj.object_type +" + "+obj.info_text
    # return the retrieved information to client
    return HttpResponse(ret_string)


# post method: receives an image
@csrf_exempt
def image_post(request):
    # receive the image data from client and convert it to jpeg
    post_data = request.POST
    image_string = post_data.get('image')
    image_data = base64.b64decode(image_string)

    # set the image
    timestamp = str(datetime.datetime.now().microsecond)
    filename = "image"+timestamp+".jpeg"
    with open(filename, 'wb') as f:
        f.write(image_data)
    # use nn for object reconition
    response = decode_image(filename)
    # send result back to client
    return HttpResponse(response)
