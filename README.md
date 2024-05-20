# HUAWEI CLOUD Hibernate cluster and nodes

This repository contains Python scripts that hibernate a cluster and its nodes using FunctionGraph service in Huawei Cloud.

## DISCLAIMER

The developers of this tool are not responsible for data loss neither for unexpected cost increases. You, the user of this tool, are the sole responsible for checking the source code.

## Requirements

- Function Graph: <https://www.huaweicloud.com/intl/en-us/product/functiongraph.html>
- Huawei Python SDK: <https://support.huaweicloud.com/intl/en-us/ssdk-live/live_18_0003.html>

## Importing CCE and ECS libraries to FunctionGraph

1. Clone the  [Huawei Python SDK](https://github.com/huaweicloud/huaweicloud-sdk-python-v3) repository, extract and search for `huaweicloudsdkcce` and `hauweicloudsdkecs` folders and zip them separately into two files: `huaweicloudsdkecs.zip` and `huaweicloudsdkcce.zip`
2. On the FunctionGraph console, click on `Functions > Dependencies` and "Create Dependency"
3. Enter the information of each of the libraries and upload each one of them to Huawei Cloud and change the runtime to **Python.3.9**.
4. Do that for the two dependencies.

## FunctionGraph

1. Download the latest release, we will use the `main.zip` file.

2. In Huawei Cloud Console, choose the FunctionGraph service

3. In the Agency field, **Create an Agency** for **Cloud services**. Select **FunctionGraph** and assign the following permissions to this agency: **CCE Administrator**, **ECS CommonOperations**, and **APIG Administrator**.

4. Create a Event Function from scratch, selecting **Python 3.9** as Runtime.

5. In the Code Source, click on "Upload" on the top right corner, select "Local ZIP" and upload the `main.zip` file.

6. In the Basic Information, click on "Edit" and change the "Execution Timeout(s)" to 30 seconds.

7. In the Dependencies, click "Add" and add `huaweicloudskecs` and `huaweicloudsdkcce` private libraries that were previous imported.

8. In the configuration, click on **Environment Variables** and add three variables:

    - `project_id`: The project ID of your region
    - `cluster_id`: The ID of your cluster
    - `region`: The [region](https://developer.huaweicloud.com/intl/en-us/endpoint) The region where your cluster is deployed

9. Click on "Test" and run the code.

## References

- Huawei Cloud Function Graph: <https://www.huaweicloud.com/intl/en-us/product/functiongraph.html>
- How Do I Create an IAM Agency? <https://support.huaweicloud.com/intl/en-us/ims_faq/ims_faq_0042.html>
- Huawei Cloud API: <https://console-intl.huaweicloud.com/apiexplorer/#/openapi/Live/debug?api=UpdateDomainHttpsCert>
- How Do I Create a Dependency on the FunctionGraph Console?: <https://support.huaweicloud.com/intl/en-us/functiongraph_faq/functiongraph_03_0888.html>
