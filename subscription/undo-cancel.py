import killbill
from killbill import Subscription, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

subscriptionApi = killbill.api.SubscriptionApi()
subscription_id = '6e5e4336-0acd-4b8f-9738-c17a975e043e'

subscriptionApi.uncancel_subscription_plan(subscription_id,
                                           created_by='demo',
                                           reason='reason',
                                           comment='comment')
