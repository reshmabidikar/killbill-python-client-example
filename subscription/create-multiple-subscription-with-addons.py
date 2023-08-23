import killbill
from killbill import Subscription, BulkSubscriptionsBundle, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

subscriptionApi = killbill.api.SubscriptionApi()
account_id = '04779ade-11f9-48d1-88a1-a63be84d1cb7'
subscription_a = Subscription(account_id=account_id,
                              plan_name='pistol-thirty-days')

subscription_b = Subscription(account_id=account_id,
                              plan_name='cleaning-monthly')

bundle1 = BulkSubscriptionsBundle([subscription_a, subscription_b])

subscription_c = Subscription(account_id=account_id,
                              plan_name='shotgun-monthly')

subscription_d = Subscription(account_id=account_id,
                              plan_name='holster-monthly-regular')

bundle2 = BulkSubscriptionsBundle([subscription_c, subscription_d])

subscriptionApi.create_subscriptions_with_add_ons([bundle1, bundle2],
                                                  created_by='demo',
                                                  reason='reason',
                                                  comment='comment')
