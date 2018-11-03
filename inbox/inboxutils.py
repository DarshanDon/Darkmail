from googleapiclient import errors

from apiauth.authenticate import Authenticator


class Inbox:
    SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

    def __init__(self):
        authenticator = Authenticator(self.SCOPES)
        self.__service = authenticator.get_service()

    def get_messages(self):
        response = self.__service.users().messages().list(userId='me', q='raw').execute()
        messages_list = []
        if 'messages' in response:
            messages_list.extend(response['messages'])

        '''
        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = self.service.users().messages().list(
                userId='me', q='', pageToken=page_token).execute()
            messages.extend(response['messages'])
        '''

        messages = []
        for message in messages_list:
            try:
                messages.append(self.__service.users().messages().get(
                    userId='me', id=message['id']).execute())

            except errors.HttpError as error:
                print('An error occurred: %s', error)

        return messages