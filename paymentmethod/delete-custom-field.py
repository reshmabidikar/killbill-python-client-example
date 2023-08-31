import killbill
from killbill import PaymentMethod, CustomField, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

paymentMethodApi = killbill.api.PaymentMethodApi()
payment_method_id = '34150e56-c1fe-4560-a177-2e1376662e20'

custom_fields = ['0ef3863d-1d3f-4b18-a795-9bb6b68cef83']

paymentMethodApi.delete_payment_method_custom_fields(payment_method_id,
                                                     custom_field=custom_fields,
                                                     created_by='demo',
                                                     reason='reason',
                                                     comment='comment')
