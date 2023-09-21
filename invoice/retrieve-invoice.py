import killbill
from killbill import InvoiceItem, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret


print("invoice by id")
invoiceApi = killbill.api.InvoiceApi()
invoice_id = '4b16ad29-2f32-4e7e-85f9-99beda4ae7dd'

invoice = invoiceApi.get_invoice(invoice_id)
print(invoice)

print("invoice by number")
invoiceApi = killbill.api.InvoiceApi()
invoice_number = '7452'

invoice = invoiceApi.get_invoice_by_number(invoice_number)
print(invoice)

print("invoice by item id")
invoiceApi = killbill.api.InvoiceApi()
invoice_item_id = '5cc1dce5-7f95-4d8e-987b-27ddd9e5b171'

invoice = invoiceApi.get_invoice_by_item_id(invoice_item_id,
                                            with_children_items=True)

print(invoice)

print("invoice HTML")
invoiceApi = killbill.api.InvoiceApi()
invoice_id = '4b16ad29-2f32-4e7e-85f9-99beda4ae7dd'

invoiceHTML = invoiceApi.get_invoice_as_html(invoice_id)
print(invoiceHTML)
