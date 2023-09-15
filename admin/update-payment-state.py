import killbill
from killbill import AdminPayment, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

adminApi = killbill.api.AdminApi()

payment_id = '770d7802-9e03-45dc-a16a-dc58ddcb44d1'
payment_transaction_id = 'f20e1bca-8c3e-4a8f-b411-27f4362f858b'
body = AdminPayment(transaction_status='PAYMENT_FAILURE')

adminApi.update_payment_transaction_state(payment_id,
                                          payment_transaction_id,
                                          body,
                                          created_by='demo',
                                          reason='reason',
                                          comment='comment')
