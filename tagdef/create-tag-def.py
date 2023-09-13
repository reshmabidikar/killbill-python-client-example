import killbill
from killbill import TagDefinition, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

tagDefinitionApi = killbill.api.TagDefinitionApi()

tagDefinition = TagDefinition(name='tag_name', description='tag description', applicable_object_types=['BUNDLE', 'SUBSCRIPTION','ACCOUNT'], is_control_tag=False)
tagDefinitionApi.create_tag_definition(tagDefinition,
                                       created_by='demo',
                                       reason='reason',
                                       comment='comment')