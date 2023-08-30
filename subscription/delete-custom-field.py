import killbill
from killbill import Subscription, CustomField, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

subscriptionApi = killbill.api.SubscriptionApi()
subscription_id = '9eb5e295-70a1-4c0c-9b3c-951c934f410b'

custom_fields = ['cc3bd733-7014-4380-b15f-4660737bad45']

subscriptionApi.delete_subscription_custom_fields(subscription_id=subscription_id,
                                                  custom_field=custom_fields,
                                                  created_by='demo',
                                                  reason='reason',
                                                  comment='comment')
