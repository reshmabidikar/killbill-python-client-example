import killbill
from killbill import Tenant, Configuration

config = Configuration()
apiKey = 'bob'
apiSecret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = apiKey
config.api_key['X-Killbill-ApiSecret'] =  apiSecret

tenantApi = killbill.api.TenantApi()

print("create")
key_name = 'demo_key_python'
body = 'demo_value'
tenantApi.insert_user_key_value(key_name, body, created_by='demo')
tenantApi = killbill.api.TenantApi()

print("retrieve")
key_name = 'demo_key_python'
tenantKeyValue = tenantApi.get_user_key_value(key_name)
print(tenantKeyValue)
#
# print("delete")
# tenantApi = killbill.api.TenantApi()
# key_name = 'demo_key_python'
# tenantApi.delete_user_key_value(key_name, created_by='demo')

print("Retrieve based on key prefix")
tenantApi = killbill.api.TenantApi()

tenantKeyValues = tenantApi.get_all_plugin_configuration(key_prefix='demo_key')
print(tenantKeyValues)

