import killbill
from killbill import PaymentMethod, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

paymentMethodApi = killbill.api.PaymentMethodApi()
payment_method_id = '2aabb688-a92d-4e02-8571-854c76c9269e'

paymentMethodApi.delete_payment_method(payment_method_id,
                                       created_by='demo',
                                       reason='reason',
                                       comment='comment')
