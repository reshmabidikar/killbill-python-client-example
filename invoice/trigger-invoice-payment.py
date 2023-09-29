import killbill
from killbill import InvoicePayment, Configuration
import datetime

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

invoiceApi = killbill.api.InvoiceApi()

account_id = '04779ade-11f9-48d1-88a1-a63be84d1cb7'
invoice_id = '46ab72dc-8abf-4984-818b-cf1558c7ef4b'

body = InvoicePayment(account_id=account_id,
                      purchased_amount=50.0,
                      target_invoice_id=invoice_id)

invoiceApi.create_instant_payment(invoice_id,
                                  body,
                                  external_payment=True,
                                  created_by='demo',
                                  reason='reason',
                                  comment='comment')
