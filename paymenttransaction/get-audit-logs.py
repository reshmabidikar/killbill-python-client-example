import killbill
from killbill import PaymentTransaction, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

paymentTransactionApi = killbill.PaymentTransactionApi()
payment_transaction_id = '02acb6b2-8139-40d3-816c-8b7ec858d350'
audit_logs = paymentTransactionApi.get_transaction_audit_logs_with_history(payment_transaction_id)
print(audit_logs)
