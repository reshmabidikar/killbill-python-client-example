import killbill
from killbill import PaymentTransaction, CustomField, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

paymentTransactionApi = killbill.api.PaymentTransactionApi()
payment_transaction_id = '02acb6b2-8139-40d3-816c-8b7ec858d350'
custom_fields = ['494c8e9b-0840-4955-9e23-e84d4c353c25']

paymentTransactionApi.delete_transaction_custom_fields(payment_transaction_id,
                                                       custom_field=custom_fields,
                                                       created_by='demo',
                                                       reason='reason',
                                                       comment='comment')
