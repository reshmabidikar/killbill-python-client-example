import killbill
from killbill import Subscription, CustomField, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

subscriptionApi = killbill.api.SubscriptionApi()
subscription_id = '33aa2952-cea2-4cad-900a-9731c1042e54'

fields = subscriptionApi.get_subscription_custom_fields(subscription_id)
print(fields)
