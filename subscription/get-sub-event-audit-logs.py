import killbill
from killbill import Subscription, CustomField, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

subscriptionApi = killbill.api.SubscriptionApi()
event_id = 'dc283026-5be0-4e47-8190-b62fb0c9e357'

auditlogs = subscriptionApi.get_subscription_event_audit_logs_with_history(event_id)
print(auditlogs)

