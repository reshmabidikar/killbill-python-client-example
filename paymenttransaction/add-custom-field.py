import killbill
from killbill import PaymentTransaction, CustomField, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

paymentTransactionApi = killbill.api.PaymentTransactionApi()
payment_transaction_id = '02acb6b2-8139-40d3-816c-8b7ec858d350'
body = CustomField(name='Test Custom Field2', value='test_value2')

paymentTransactionApi.create_transaction_custom_fields(payment_transaction_id,
                                                       [body],
                                                       created_by='demo',
                                                       reason='reason',
                                                       comment='comment')
