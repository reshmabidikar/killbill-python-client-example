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
body = 'sports-monthly = Voiture Sport'

invoiceApi.upload_catalog_translation(locale,
                                      body,
                                      created_by='demo',
                                      reason='reason',
                                      comment='comment')
