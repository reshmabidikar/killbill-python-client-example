import killbill
from killbill import Configuration
import datetime

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

invoiceApi = killbill.api.InvoiceApi()

account_id = 'bdbed417-a84b-4303-958c-b88a36807416'
target_date = datetime.date(2023, 11, 20)

invoiceApi.create_future_invoice(account_id,
                                 target_date=target_date,
                                 created_by='demo',
                                 reason='reason',
                                 comment='comment')
