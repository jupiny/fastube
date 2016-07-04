from .base import SendNotificationBaseTask

from notifications.models import SMSNotification


class SendSMSTask(SendNotificationBaseTask):

    def get_object(self, object_id):
        sms = SMSNotification.objects.get(pk=object_id)
        return sms

    def get_api_base_url(self):
        base_url = "http://api.openapi.io/ppurio/1/message/sms/dobestan"
        return base_url

    def get_headers(self):
        headers = {
            'x-waple-authorization': 'MTkyMC0xNDEzODU0NTAwMzU3LTllM2VkOTM3LTYwMTEtNGU2Zi1iZWQ5LTM3NjAxMTNlNmYyMg==',
        }
        return headers

    def get_data(self, object):
        data = {
            "send_phone": object.sender,
            "dest_phone": object.receiver,
            "msg_body": object.content,
        }
        return data
