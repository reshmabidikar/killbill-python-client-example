import killbill
from killbill import TagDefinition, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

tagDefinitionApi = killbill.api.TagDefinitionApi()
tag_definition_id = '2a4b9f36-6a53-4553-a2ef-d0bddf8e831a'

tagDefinitionApi.delete_tag_definition(tag_definition_id,
                                       created_by='demo',
                                       reason='reason',
                                       comment='comment')