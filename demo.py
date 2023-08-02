import killbill
from killbill.configuration import Configuration
from killbill.models.account import Account
from killbill.models.tenant import Tenant
from killbill.models.payment_method import PaymentMethod
from killbill.models.subscription import Subscription
from killbill.models.invoice_dry_run import InvoiceDryRun
from killbill.models.invoice_item import InvoiceItem
from killbill.models.payment_transaction import PaymentTransaction
from random import choice
from string import ascii_lowercase
import time
import datetime
from killbill.rest import ApiException

config = Configuration()
apiKey = 'bob'
apiSecret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = apiKey
config.api_key['X-Killbill-ApiSecret'] =  apiSecret

api_tenant = killbill.TenantApi()
api_account = killbill.AccountApi()

tenant = api_tenant.get_tenant_by_api_key(api_key=apiKey)

print(tenant)

body = Account(name='John', external_key='key1', currency='USD', state='CA', country='USA',bill_cycle_day_local=25)

print (api_account.create_account(body, 'test'))

accountID = api_account.get_account_by_key('key1').account_id

print(accountID)
