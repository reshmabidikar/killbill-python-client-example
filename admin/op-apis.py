import killbill
from killbill import AdminPayment, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

print("invalidate cache")

adminApi = killbill.api.AdminApi()

adminApi.invalidates_cache()

print("invalidate account cache")
adminApi = killbill.api.AdminApi()
account_id = '0e7700ad-7608-44bf-ac32-7691b6100f5a'

adminApi.invalidates_cache_by_account(account_id)

print("invalidate tenant cache")
adminApi = killbill.api.AdminApi()

adminApi.invalidates_cache_by_tenant()

print("put host in rotation")
adminApi = killbill.api.AdminApi()

adminApi.put_in_rotation()
adminApi = killbill.api.AdminApi()

adminApi.put_out_of_rotation()

print("get queue entries")
adminApi = killbill.api.AdminApi()

adminApi.get_queue_entries()



print("put host out of rotation")

