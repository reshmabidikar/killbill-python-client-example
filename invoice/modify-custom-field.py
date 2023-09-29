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
custom_field_id = 'da4c9071-e3da-418c-aa28-2b7cbf9ec3c8'
body = CustomField(custom_field_id=custom_field_id, value='New Value')

invoiceApi.modify_invoice_custom_fields(invoice_id,
                                        [body],
                                        created_by='demo',
                                        reason='reason',
                                        comment='comment')
