import killbill
from killbill import Subscription, CustomField, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

subscriptionApi = killbill.api.SubscriptionApi()
subscription_id = '9eb5e295-70a1-4c0c-9b3c-951c934f410b'
tagDefIds = ['30363fe5-310d-4446-b000-d7bb6e6662e2']

subscriptionApi.delete_subscription_tags(subscription_id,
                                         tag_def=tagDefIds,
                                         created_by='demo',
                                         reason='reason',
                                         comment='comment')
