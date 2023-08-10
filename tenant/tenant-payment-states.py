import killbill
from killbill import Tenant, Configuration

config = Configuration()
apiKey = 'bob'
apiSecret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = apiKey
config.api_key['X-Killbill-ApiSecret'] =  apiSecret

print("add payment state")

tenantApi = killbill.api.TenantApi()

plugin_name = 'demo_plugin'
body = '<xml>..</xml>'

tenantApi.upload_plugin_payment_state_machine_config(plugin_name, body, created_by='demo')

print("retrieve payment state")

tenantApi = killbill.api.TenantApi()

plugin_name = 'demo_plugin'

tenantKeyValue = tenantApi.get_plugin_payment_state_machine_config(plugin_name)
print(tenantKeyValue)

print("delete payment state")
tenantApi = killbill.api.TenantApi()

plugin_name = 'demo_plugin'

tenantApi.delete_plugin_payment_state_machine_config(plugin_name, created_by='demo')


