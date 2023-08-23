import killbill
from killbill import Subscription, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

subscriptionApi = killbill.api.SubscriptionApi()
subscription_id = '7b3f0181-d9e8-4886-a90a-af35e671f5f0'
body = Subscription(subscription_id=subscription_id,
                    bill_cycle_day_local=26)

subscriptionApi.update_subscription_bcd(subscription_id, body, created_by='demo',reason='reason', comment='comment')
