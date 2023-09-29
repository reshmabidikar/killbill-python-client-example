import killbill
from killbill import InvoiceDryRun, Configuration
import datetime

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

invoiceApi = killbill.api.InvoiceApi()
account_id = '8452df66-ded8-4fba-b7dc-50302d19bc5b'
target_date = datetime.date(2023, 11, 22)

invoiceApi.create_future_invoice_group(account_id,
                                       target_date=target_date,
                                       created_by='demo',
                                       reason='reason',
                                       comment='comment')