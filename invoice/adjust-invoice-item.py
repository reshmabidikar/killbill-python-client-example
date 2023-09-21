import killbill
from killbill import InvoiceItem, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

invoiceApi = killbill.api.InvoiceApi()
invoice_id = '4b16ad29-2f32-4e7e-85f9-99beda4ae7dd'
body = InvoiceItem(account_id='bdbed417-a84b-4303-958c-b88a36807416',
                   invoice_id='4b16ad29-2f32-4e7e-85f9-99beda4ae7dd',
                   invoice_item_id='5cc1dce5-7f95-4d8e-987b-27ddd9e5b171',
                   amount=10,
                   currency='USD',
                   description='Free adjustment: good customer')

invoiceApi.adjust_invoice_item(invoice_id,
                               body,
                               created_by='demo',
                               reason='reason',
                               comment='comment')
