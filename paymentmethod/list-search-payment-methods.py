import killbill
from killbill import PaymentMethod, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

print("list payment methods")
paymentMethodApi = killbill.api.PaymentMethodApi()

payment_methods = paymentMethodApi.get_payment_methods()
print(payment_methods)



print("search payment methods")

paymentMethodApi = killbill.api.PaymentMethodApi()
search_key = '__EXTERNAL_PAYMENT__'

payment_methods = paymentMethodApi.search_payment_methods(search_key)
print(payment_methods)