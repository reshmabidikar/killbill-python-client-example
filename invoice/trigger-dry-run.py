import killbill
from killbill import InvoiceDryRun, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret
#
# This case is when you create a dry-run invoice with UPCOMING_INVOICE,
# to see what is the next invoice that the system will generate for this account
#
invoiceApi = killbill.api.InvoiceApi()
body = InvoiceDryRun(dry_run_type='UPCOMING_INVOICE')
account_id = '8452df66-ded8-4fba-b7dc-50302d19bc5b'

invoice = invoiceApi.generate_dry_run_invoice(body,
                                    account_id,
                                    created_by='demo',
                                    reason='reason',
                                    comment='comment')
print(invoice)