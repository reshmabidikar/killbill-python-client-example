import killbill
from killbill import CustomField, Configuration
import datetime

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

invoiceApi = killbill.api.InvoiceApi()
body = 'Some_HTML_String'

invoiceApi.upload_invoice_mp_template(body,
                                      created_by='demo',
                                      reason='reason',
                                      comment='comment')
