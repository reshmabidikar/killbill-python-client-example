import killbill
from killbill import PaymentTransaction, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

paymentTransactionApi = killbill.PaymentTransactionApi()
payment_transaction_id = 'edb52a56-f5d2-4285-9a23-ccafb6f1ae1f'

payment = paymentTransactionApi.get_payment_by_transaction_id(payment_transaction_id)
print(payment)

print("by key")

paymentTransactionApi = killbill.PaymentTransactionApi()
payment_transaction_key = 'edb52a56-f5d2-4285-9a23-ccafb6f1ae1f'

payment = paymentTransactionApi.get_payment_by_transaction_external_key(payment_transaction_key)
print(payment)
