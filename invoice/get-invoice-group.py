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
group_id = '51eae3dc-eec8-4ffa-b7d1-65b7b797538e'

invoice_group = invoiceApi.get_invoices_group(group_id, account_id)

print(invoice_group)