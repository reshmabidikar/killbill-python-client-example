import killbill
from killbill import Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

adminApi = killbill.api.AdminApi()

adminApi.trigger_invoice_generation_for_parked_accounts(created_by='demo',
                                                        reason='reason',
                                                        comment='comment')


