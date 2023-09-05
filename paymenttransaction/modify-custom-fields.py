import killbill
from killbill import PaymentTransaction, CustomField, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

paymentTransactionApi = killbill.api.PaymentTransactionApi()
payment_transaction_id = '02acb6b2-8139-40d3-816c-8b7ec858d350'
custom_field_id = 'eddc016c-0336-44d3-9383-a29962e276b7'
body = CustomField(custom_field_id=custom_field_id, value='new value')

paymentTransactionApi.modify_transaction_custom_fields(payment_transaction_id,
                                                       [body],
                                                       created_by='demo',
                                                       reason='reason',
                                                       comment='comment')
