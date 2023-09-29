import killbill
from killbill import CustomField, Configuration
import datetime

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

invoiceApi = killbill.api.InvoiceApi()
invoice_id = 'b64bd7d2-167b-4e89-bb76-15ee955801f1'
tagDefIds = ["00000000-0000-0000-0000-000000000004"]

invoiceApi.create_invoice_tags(invoice_id,
                               tagDefIds,
                               created_by='demo',
                               reason='reason',
                               comment='comment')
