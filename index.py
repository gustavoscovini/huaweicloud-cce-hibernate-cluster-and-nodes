from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcce.v3.region.cce_region import CceRegion
from huaweicloudsdkcce.v3 import *
from huaweicloudsdkecs.v2.region.ecs_region import EcsRegion
from huaweicloudsdkecs.v2 import *
from huaweicloudsdkcore.exceptions import exceptions


def handler(event, context):
    ak = context.getSecurityAccessKey()
    sk = context.getSecuritySecretKey()
    token = context.getSecurityToken()
    project_id = context.getUserData('project_id')
    cluster_id =  context.getUserData('cluster_id')
    region =  context.getUserData('region')
    credentials = BasicCredentials(ak, sk, project_id).with_security_token(token)

    cce_client = CceClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(CceRegion.value_of(region)) \
        .build()

    try:
        # Retrieve list of nodes
        response = cce_client.list_nodes(ListNodesRequest(cluster_id=cluster_id))
        ids = [item.status.server_id for item in response.items]

    except exceptions.ClientRequestException as e:
        print_error("listing nodes", e)
        ids = []

    ecs_client = EcsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(EcsRegion.value_of(region)) \
        .build()

    try:
        # Stop servers
        request = BatchStopServersRequest()
        list_servers_to_stop = [ServerId(id=uid) for uid in ids]
        request.body = BatchStopServersRequestBody(os_stop=BatchStopServersOption(servers=list_servers_to_stop))

        response = ecs_client.batch_stop_servers(request)
        print(response)

        try:
            response_hibernate_C = cce_client.hibernate_cluster(HibernateClusterRequest(cluster_id=cluster_id))
            print(response_hibernate_C)
        except exceptions.ClientRequestException as e:
            print("could not hibernate cluster")
            print("trying to wake up cluster")
            try:
                response_awake_C = cce_client.awake_cluster(AwakeClusterRequest(cluster_id=cluster_id))
                print(response_awake_C)
            except exceptions.ClientRequestException as e:
                print_error("stopping cluster", e)
            try:
                print("trying to start server")
                request = BatchStartServersRequest()
                list_servers_to_start = [ServerId(id=uid) for uid in ids]
                request.body = BatchStartServersRequestBody(os_start=BatchStartServersOption(servers=list_servers_to_start))

                response = ecs_client.batch_start_servers(request)
                print(response)
            
            except exceptions.ClientRequestException as e:
                print_error("stopping servers". e)

    except exceptions.ClientRequestException as e:
        print("Could not stop servers")
        
        

def print_error(action, e):
    print(f"Error occurred while {action}:")
    print(f"Status Code: {e.status_code}")
    print(f"Request ID: {e.request_id}")
    print(f"Error Code: {e.error_code}")
    print(f"Error Message: {e.error_msg}")
