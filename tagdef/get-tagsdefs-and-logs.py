import killbill
from killbill import TagDefinition, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

print("get all tag definitions")
tagDefinitionApi = killbill.api.TagDefinitionApi()

tag_definitions = tagDefinitionApi.get_tag_definitions()
print(tag_definitions)

print("get tag definition by ID")
tagDefinitionApi = killbill.api.TagDefinitionApi()
tag_definition_id = '3ba41ebd-71f0-4a27-981b-86c6054f58dd'

tag_definition = tagDefinitionApi.get_tag_definition(tag_definition_id)
print(tag_definition)

print("get logs")
tagDefinitionApi = killbill.api.TagDefinitionApi()
tag_definition_id = '3ba41ebd-71f0-4a27-981b-86c6054f58dd'
audit_logs = tagDefinitionApi.get_tag_definition_audit_logs_with_history(tag_definition_id)
print(audit_logs)