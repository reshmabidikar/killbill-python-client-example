import killbill
from killbill import Subscription, CustomField, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

subscriptionApi = killbill.api.SubscriptionApi()
subscription_id = '33aa2952-cea2-4cad-900a-9731c1042e54'
custom_field_id = '3a26be42-a153-4894-ac3d-93ad2e38e05b'
body = CustomField(custom_field_id=custom_field_id,
                   value='modified_value')

subscriptionApi.modify_subscription_custom_fields(subscription_id,
                                                  [body],
                                                  created_by='demo',
                                                  reason='reason',
                                                  comment='comment')
