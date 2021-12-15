# cloudwatch_exporter_metrics_config_builder
Bash script that generates all aws cloudwatch metrics and dimensions then builds the cloudwatch.yml file.

## Requirements
- aws cli
- python 3.7 or newer
- ansible

## How To
Before running make sure custom_gather.sh and pipeline.sh are executable. If not
simply run 'chmod 755 custom_gather.sh pipeline.sh'

To select what AWS namespaces you want in the cloudwatch.yml file set the boolean
flag in the cloudwatch_config_builder/config.yml.

To create the cloudwatch.yml run pipeline.sh <REGION> <CUSTOM_NAMESPACE>
- REGION: Required to run. The region of the aws account. (ex: us-west-1)
- CUSTOM_NAMESPACE: Optional to run. A list of custom namespaces separated by a comma. (ex: Billing,CloudTrailMetrics...)

Once the scripts are done running, all available metrics in json format will be in the cloudwatch_config_builder/files/cloudwatch_metrics folder separated via namespace.

The formatted cloudwatch.yml file will be located in the cloudwatch_exporter_metrics_config_builder folder.
