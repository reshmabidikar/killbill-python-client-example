import killbill
from killbill import InvoiceItem, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

invoiceApi = killbill.api.InvoiceApi()
invoice_id = '18d23ef1-ea82-442d-8602-43305232f3e5'

invoiceApi.void_invoice(invoice_id,
                        created_by='demo',
                        reason='reason',
                        comment='comment')
