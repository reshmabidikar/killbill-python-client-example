import killbill
from killbill import Tenant, Configuration

config = Configuration()
apiKey = 'bob'
apiSecret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = apiKey
config.api_key['X-Killbill-ApiSecret'] =  apiSecret

print("register push notification")

tenantApi = killbill.api.TenantApi()

tenantApi.register_push_notification_callback(created_by='demo', cb='http://demo/callmeback')

print("retrieve push notification")
tenantApi = killbill.api.TenantApi()

tenantKeyValue = tenantApi.get_push_notification_callbacks()
print(tenantKeyValue)

print("delete payment state")
tenantApi = killbill.api.TenantApi()

tenantApi.delete_push_notification_callbacks(created_by='demo')


