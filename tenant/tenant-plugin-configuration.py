import killbill
from killbill import Tenant, Configuration

config = Configuration()
apiKey = 'bob'
apiSecret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = apiKey
config.api_key['X-Killbill-ApiSecret'] =  apiSecret

print("add plugin configuration")

tenantApi = killbill.api.TenantApi()

plugin_name = 'demo_plugin'
body = 'tenant_config'

tenantApi.upload_plugin_configuration(plugin_name, body, created_by='demo')

print("Retrieve plugin configuration")

tenantApi = killbill.api.TenantApi()

plugin_name = 'demo_plugin'

tenantKeyValue = tenantApi.get_plugin_configuration(plugin_name)
print(tenantKeyValue)

print("Delete plugin configuration")

tenantApi = killbill.api.TenantApi()

plugin_name = 'demo_plugin'

tenantApi.delete_plugin_configuration(plugin_name, created_by='demo')



