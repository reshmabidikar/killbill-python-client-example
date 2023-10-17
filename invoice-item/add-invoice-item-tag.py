import killbill
from killbill import CustomField, Configuration
import datetime

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

invoiceItemApi = killbill.api.InvoiceItemApi()
invoice_item_id = 'e212f5bf-6960-4b95-ac4e-c60439447ee5'
tagDefIds = ["2c1f8309-24d7-437c-971b-7e68ff2d393a"]

invoiceItemApi.create_invoice_item_tags(invoice_item_id,
                               tagDefIds,
                               created_by='demo',
                               reason='reason',
                               comment='comment')
