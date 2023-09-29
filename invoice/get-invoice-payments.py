import killbill
from killbill import InvoicePayment, Configuration
import datetime

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

invoiceApi = killbill.api.InvoiceApi()
invoice_id = '46ab72dc-8abf-4984-818b-cf1558c7ef4b'

invoice_payments = invoiceApi.get_payments_for_invoice(invoice_id)

print(invoice_payments)
