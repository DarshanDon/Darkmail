from __future__ import print_function

from django.shortcuts import render

from inbox.inbox_utils import InboxUtils


def inbox(request):
    inbox_utils = InboxUtils(request.session.get('access_token'),
                             request.META['HTTP_USER_AGENT'])
    messages = inbox_utils.get_messages()
    context = {'messages': messages}
    return render(request, 'inbox/inbox.html', context)


def details(request, message_id):
    inbox_utils = InboxUtils(request.session.get('access_token'),
                             request.META['HTTP_USER_AGENT'])
    detailed_message = inbox_utils.get_detailed_message(message_id)
    context = {'message_body': detailed_message}
    return render(request, 'inbox/details.html', context)
