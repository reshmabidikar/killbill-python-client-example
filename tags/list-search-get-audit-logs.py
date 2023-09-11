import killbill
from killbill import Tag, Configuration

config = Configuration()
api_key = 'bob'
api_secret= 'lazar'
config.api_key['X-Killbill-ApiKey'] = api_key
config.api_key['X-Killbill-ApiSecret'] =  api_secret

print("list tags")
tagApi = killbill.api.TagApi()
tags = tagApi.get_tags()
print(tags)

print ("search tags")
tagApi = killbill.api.TagApi()
search_key = "5ad7519f-3698-4c75-8d93-98c7a465010e"
tags = tagApi.search_tags(search_key)
print(tags)

print("get audit logs")
tagApi = killbill.api.TagApi()
tag_id = "5ad7519f-3698-4c75-8d93-98c7a465010e"
audit_logs = tagApi.get_tag_audit_logs_with_history(tag_id)
print(audit_logs)