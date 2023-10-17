import killbill
from killbill import CustomField, Configuration
import datetime

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

invoiceItemApi = killbill.api.InvoiceItemApi()

invoice_item_id = 'e212f5bf-6960-4b95-ac4e-c60439447ee5'

custom_fields = invoiceItemApi.get_invoice_item_custom_fields(invoice_item_id)

print(custom_fields)