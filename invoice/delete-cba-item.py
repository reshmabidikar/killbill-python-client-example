import killbill
from killbill import InvoiceItem, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

invoiceApi = killbill.api.InvoiceApi()
invoice_id='a493320b-29ab-4228-ad84-58d53e88b73b'
invoice_item_id='b3aeb9d7-4501-4285-8071-f5c02f45a659'
account_id = 'bdbed417-a84b-4303-958c-b88a36807416'

invoiceApi.delete_cba(invoice_id,
                      invoice_item_id,
                      account_id,
                      created_by='demo',
                      reason='reason',
                      comment='comment')
