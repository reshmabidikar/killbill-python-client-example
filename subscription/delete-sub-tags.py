import killbill
from killbill import Subscription, CustomField, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

subscriptionApi = killbill.api.SubscriptionApi()
subscription_id = '92820d1c-1d4c-46eb-9010-26b0626a1927'
tagDefIds = ['30363fe5-310d-4446-b000-d7bb6e6662e2']

subscriptionApi.delete_subscription_tags(subscription_id,
                                         created_by='demo',
                                         reason='reason',
                                         comment='comment',
                                         tag_def=tagDefIds)
