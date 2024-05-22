# HUAWEI CLOUD Hibernate cluster and nodes

This repository contains Python scripts that hibernate a cluster and its nodes using FunctionGraph service in Huawei Cloud.

## DISCLAIMER

The developers of this tool are not responsible for data loss neither for unexpected cost increases. You, the user of this tool, are the sole responsible for checking the source code.

## Requirements

- Function Graph: <https://www.huaweicloud.com/intl/en-us/product/functiongraph.html>
- Huawei Python SDK: <https://support.huaweicloud.com/intl/en-us/ssdk-live/live_18_0003.html>

## Importing CCE and ECS libraries to FunctionGraph

1. In the releases of this repository, find the `huaweicloudsdkcce.zip` and `huaweicloudsdkecs.zip` and download it.
2. In the FunctionGraph console, click on `Functions > Dependencies` and "Create Dependency", set the name as **huaweicloudskdecs**, upload the `huaweicloudsdkecs.zip` and change the runtime to **Python.3.9**.
3. Create another dependency, setting the name **huaweicloudskdcce** and upload `huaweicloudsdkcce.zip` and also change the runtime to **Python.3.9**.

## FunctionGraph

1. Download the latest [release](https://github.com/gustavoscovini/huaweicloud-cce-hibernate-cluster-and-nodes/releases), we will use the `index.zip` file.

2. In Huawei Cloud Console, choose the FunctionGraph service

3. Click on **Create Function > Create from Scratch**

4. Create a Event Function, select **Python 3.9** as Runtime.

5. In the Agency field, click **Create an Agency > Create Agency**, select **Cloud services** and in the Cloud service box, select **FunctionGraph** and assign the following permissions to this agency: **CCE Administrator**, **ECS CommonOperations**, and **APIG Administrator**.

6. In the Code Source, click on "Upload" on the top right corner, select "Local ZIP" and upload the `index.zip` file.

7. In the Basic Information, click on "Edit" and change the "Execution Timeout(s)" to 30 seconds.

8. In the Dependencies, click "Add" and add `huaweicloudsdkecs` and `huaweicloudsdkcce` private libraries that were previously imported.

9. In the configuration, click on **Environment Variables** and add three variables:

    - `project_id`: The project ID of your region
    - `cluster_id`: The ID of your cluster
    - `region`: The [region](https://developer.huaweicloud.com/intl/en-us/endpoint) where your cluster is deployed

10. Click on "Test" and run the code.

## References

- Huawei Cloud Function Graph: <https://www.huaweicloud.com/intl/en-us/product/functiongraph.html>
- How Do I Create an IAM Agency? <https://support.huaweicloud.com/intl/en-us/ims_faq/ims_faq_0042.html>
- Huawei Cloud API: <https://console-intl.huaweicloud.com/apiexplorer/#/openapi/Live/debug?api=UpdateDomainHttpsCert>
- How Do I Create a Dependency on the FunctionGraph Console?: <https://support.huaweicloud.com/intl/en-us/functiongraph_faq/functiongraph_03_0888.html>
