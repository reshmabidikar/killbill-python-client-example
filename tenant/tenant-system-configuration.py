import killbill
from killbill import Tenant, Configuration

config = Configuration()
apiKey = 'bob'
apiSecret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = apiKey
config.api_key['X-Killbill-ApiSecret'] =  apiSecret

print("add system configuration")
tenantApi = killbill.api.TenantApi()
body = '{"org.killbill.invoice.sanitySafetyBoundEnabled":"false"}'
tenantApi.upload_per_tenant_configuration(body, created_by='demo')

print("retrieve system configuration")
tenantApi = killbill.api.TenantApi()
tenantKeyValue = tenantApi.get_per_tenant_configuration()
print(tenantKeyValue)

print("delete system configuration")
tenantApi = killbill.api.TenantApi()
tenantApi.delete_per_tenant_configuration(created_by='demo')
