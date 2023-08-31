import killbill
from killbill import PaymentMethod, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

paymentMethodApi = killbill.PaymentMethodApi()
payment_method_id = '83fc2425-ede3-4fbd-b117-2eff4c660cfe'

payment_method = paymentMethodApi.get_payment_method(payment_method_id)
print(payment_method)

print("payment method by key")
paymentMethodApi = killbill.api.PaymentMethodApi()
external_key = '83fc2425-ede3-4fbd-b117-2eff4c660cfe'

payment_method = paymentMethodApi.get_payment_method_by_key(external_key)
print(payment_method)
