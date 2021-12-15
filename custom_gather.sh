echo "Custom Metrics:" $2

IFS=',' read -r -a array <<< $2

for e in ${array[@]}
do
  aws --region $1 cloudwatch list-metrics --namespace=$e >> cloudwatch_config_builder/files/cloudwatch_metrics/$e.json
done
