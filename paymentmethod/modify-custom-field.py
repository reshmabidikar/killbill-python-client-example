import killbill
from killbill import PaymentMethod, CustomField, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

paymentMethodApi = killbill.api.PaymentMethodApi()
payment_method_id = '34150e56-c1fe-4560-a177-2e1376662e20'
custom_field_id = '75d6449f-d012-42d8-a9bc-56261a63281f'
body = CustomField(custom_field_id=custom_field_id,
                   name='Test Custom Field',
                   value='new value')

paymentMethodApi.modify_payment_method_custom_fields(payment_method_id,
                                                     [body],
                                                     created_by='demo',
                                                     reason='reason',
                                                     comment='comment')
