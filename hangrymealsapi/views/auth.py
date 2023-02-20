from hangrymealsapi.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):

    uid = request.data['uid']
    try:

        user = User.objects.get(uid=uid)
        data = {
            'id': user.id,
            'uid': user.uid,
            'username': user.username,
        }
        return Response(data)
    except:
        data = {'valid': False}
        return Response(data)


@api_view(['POST'])
def register_user(request):
    user = User.objects.create(
        uid=request.data['uid'],
        username=request.data['username'],
    )

    data = {
        'id': user.id,
        'uid': user.uid,
        'username': user.username,
    }
    return Response(data)
