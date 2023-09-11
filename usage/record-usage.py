import killbill
from killbill import UsageRecord,UnitUsageRecord, SubscriptionUsageRecord,Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

usageApi = killbill.api.UsageApi()

usageRecord = UsageRecord(record_date='2023-09-05', amount=1)
unitUsageRecord = UnitUsageRecord(unit_type='hours',usage_records=[usageRecord])

subscriptionUsageRecord = SubscriptionUsageRecord(subscription_id='dc89f346-bc55-46ee-8963-1b666d8fea50', tracking_id="t4", unit_usage_records=[unitUsageRecord])

usageApi.record_usage(subscriptionUsageRecord,
                      created_by='demo',
                      reason='reason',
                      comment='comment')