import killbill
from killbill import CustomField, Configuration
import datetime

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

invoiceApi = killbill.api.InvoiceApi()
locale = 'fr_FR'
body = "invoiceDate = date de facture"
delete_if_exists = True

invoiceApi.upload_invoice_translation(locale,
                                      body,
                                      delete_if_exists=delete_if_exists,
                                      created_by='demo',
                                      reason='reason',
                                      comment='comment')
