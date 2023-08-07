import killbill
from killbill import Tenant, Configuration

config = Configuration()
apiKey = 'bob'
apiSecret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = apiKey
config.api_key['X-Killbill-ApiSecret'] =  apiSecret

# create tenant
# tenantApi = killbill.api.TenantApi()
# body = Tenant(api_key='python_key', api_secret='python_secret')
# tenantApi.create_tenant(body, created_by='demo')

# retrieve tenant by id
tenantApi = killbill.api.TenantApi()
tenant = tenantApi.get_tenant(tenant_id='639feed0-6d1f-436a-8d04-0fcc9520e5bd')
print(tenant)

# retrieve tenant by api key
tenantApi = killbill.api.TenantApi()
tenant = tenantApi.get_tenant_by_api_key(api_key='python_key')
print("Tenant by key")
print(tenant)

