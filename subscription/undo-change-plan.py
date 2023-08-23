import killbill
from killbill import Subscription, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

subscriptionApi = killbill.api.SubscriptionApi()
subscription_id = 'ea131df0-5612-4c73-ac19-0aab7a87bfd9'

subscriptionApi.undo_change_subscription_plan(subscription_id,
                                              created_by='demo',
                                              reason='reason',
                                              comment='comment')
