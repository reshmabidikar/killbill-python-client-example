import killbill
from killbill import PaymentTransaction, CustomField, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

paymentTransactionApi = killbill.api.PaymentTransactionApi()
payment_transaction_id = '02acb6b2-8139-40d3-816c-8b7ec858d350'
tagDefIds = ["3d70a355-8342-4042-8694-a2447f0f2b1e"]

paymentTransactionApi.delete_transaction_tags(payment_transaction_id,
                                              tag_def=tagDefIds,
                                              created_by='demo',
                                              reason='reason',
                                              comment='comment')
