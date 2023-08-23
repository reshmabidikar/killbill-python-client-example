import killbill
from killbill import Subscription, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

print("sub by id")
subscriptionApi = killbill.api.SubscriptionApi()
subscription_id = '7b3f0181-d9e8-4886-a90a-af35e671f5f0'

subscription = subscriptionApi.get_subscription(subscription_id)
print(subscription)

print("sub by key")
subscriptionApi = killbill.api.SubscriptionApi()
external_key = '7b3f0181-d9e8-4886-a90a-af35e671f5f0'
subscription = subscriptionApi.get_subscription_by_key(external_key)

print(subscription)
