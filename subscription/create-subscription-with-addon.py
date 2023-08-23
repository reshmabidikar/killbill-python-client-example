import killbill
from killbill import Subscription, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

subscriptionApi = killbill.api.SubscriptionApi()
account_id = '32660591-b8a0-4a0e-b6a8-9b52611217c2'
subscription_a = Subscription(account_id=account_id,
                              plan_name='pistol-monthly')

subscription_b = Subscription(account_id=account_id,
                              plan_name='cleaning-monthly')

body = [subscription_a, subscription_b]

subscriptionApi.create_subscription_with_add_ons(body, created_by='demo',reason='reason', comment='comment')
