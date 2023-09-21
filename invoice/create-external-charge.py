import killbill
from killbill import InvoiceItem, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

invoiceApi = killbill.api.InvoiceApi()

account_id = 'bdbed417-a84b-4303-958c-b88a36807416'
body = InvoiceItem(account_id=account_id,
                   amount=50.0,
                   currency='USD',
                   description='External charge')

invoiceApi.create_external_charges(account_id,
                                   [body],
                                   auto_commit=True,
                                   created_by='demo',
                                   reason='reason',
                                   comment='comment')

