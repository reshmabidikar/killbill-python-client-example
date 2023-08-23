import killbill
from killbill import Subscription, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

subscriptionApi = killbill.api.SubscriptionApi()
subscription_id = '74acaa2b-62b7-4d99-b26c-85c25020b287'
body = Subscription(plan_name='pistol-thirty-days')

subscriptionApi.change_subscription_plan(subscription_id,
                                         body,
                                         created_by='demo',
                                         reason='reason',
                                         comment='comment')
