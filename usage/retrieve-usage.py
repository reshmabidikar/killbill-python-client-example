import killbill
from killbill import UsageRecord,UnitUsageRecord, SubscriptionUsageRecord,Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

usageApi = killbill.api.UsageApi()

subscription_id = 'dc89f346-bc55-46ee-8963-1b666d8fea50'
unit_type='hours'
start_date='2023-09-01'
end_date='2023-09-30'
usages = usageApi.get_usage(subscription_id, unit_type, start_date, end_date)
print(usages)