from googleapiclient import discovery
import pytz
import datetime
import sys
def main(sa_email, project_id):

    logging_api = discovery.build('logging','v2',cache_discovery=False)
    
    
    request_body = {
       "resourceNames": [
       "projects/" + str(project_id)
       ],
       "filter": "protoPayload.authenticationInfo.principalEmail = \""+str(sa_email)+"\" AND timestamp > \"2020-02-01T04:47:35\""
    }

    #print(request_body)
    response =  logging_api.entries().list(body=request_body).execute()
    perm_set = []
    for entry in response.get('entries'):
        if entry.get('protoPayload').get('authorizationInfo'):
            for auth_info in entry.get('protoPayload').get('authorizationInfo'):
                print(auth_info.get('permission'))
                perm_set.append(auth_info.get('permission'))
    perm_set = set(perm_set)
    print((perm_set))


if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
