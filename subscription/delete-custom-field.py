import killbill
from killbill import Subscription, CustomField, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

subscriptionApi = killbill.api.SubscriptionApi()
subscription_id = 'e5254822-680f-4720-b5e1-a7146cefb904'

custom_fields = ['194bcfc8-340f-4592-acd2-ffc1fc461e96']

subscriptionApi.delete_subscription_custom_fields(subscription_id=subscription_id,
                                                  created_by='demo',
                                                  custom_field=custom_fields,
                                                  reason='reason',
                                                  comment='comment')
