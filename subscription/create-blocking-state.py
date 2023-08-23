import killbill
from killbill import Subscription, BlockingState, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

subscriptionApi = killbill.api.SubscriptionApi()
body = BlockingState(state_name='STATE1',
                     service='ServiceStateService',
                     is_block_change=False,
                     is_block_entitlement=False,
                     is_block_billing=False)
subscription_id = '33aa2952-cea2-4cad-900a-9731c1042e54'

subscriptionApi.add_subscription_blocking_state(subscription_id,
                                                body,
                                                created_by='demo',
                                                reason='reason',
                                                comment='comment')
