import json
import os


def format_metrics_yml_file(namespace, metric_dict, file_name):
    if file_name == "auto_scaling.json" or file_name == "billing.json" or file_name == "dynamo_db.json" \
            or file_name == "ebs.json" or file_name == "ec2.json" or file_name == "elasti_cache.json" \
            or file_name == "events.json" or file_name == "lambda.json" or file_name == "logs.json" \
            or file_name == "network_elb.json" or file_name == "rds.json" or file_name == "s3.json" \
            or file_name == "transit_gateway.json" or file_name == "trusted_advisor.json" or file_name == "usage.json":
        fp = f"cloudwatch_config_builder/files/cloudwatch_metrics/{file_name.replace('.json', '.yml')}"
    else:
        fp = f"cloudwatch_config_builder/files/cloudwatch_metrics/custom.yml"

    with open(fp, "a+") as write_file:
        if os.path.getsize(fp) == 0:
            write_file.write("---\n")

        write_file.write(f"{file_name.replace('.json', '')}_metrics:\n")

        for key, value in metric_dict.items():
            write_file.write(f"- aws_namespace: {namespace}\n")
            write_file.write(f"  aws_metric_name: {key}\n")
            write_file.write(f"  aws_dimensions: [{', '.join(map(str, value))}]\n")
            write_file.write(f"  aws_statistics: []\n")
            write_file.write("\n")
    write_file.close()
    return


def main(file_name):
    x = list(json.load(open(f"cloudwatch_metric_json/{file_name}")).values())[0]
    metric_name_set = {''}
    metric_namespace = x[0].get("Namespace")

    for metric in x:
        metric_name_set.add(metric.get("MetricName"))

    metric_name_set.remove('')
    sorted_metric_name_list = list(metric_name_set)
    sorted_metric_name_list.sort()

    metric_name_dimension_dict = dict.fromkeys(sorted_metric_name_list)

    for metric_name in metric_name_dimension_dict.keys():
        dimensions_set = {''}
        for metric in x:
            if metric_name == metric.get("MetricName"):
                for dimension in metric.get("Dimensions"):
                    dimensions_set.add(dimension.get("Name"))

        dimensions_set.remove('')
        sorted_dimensions_list = list(dimensions_set)
        sorted_dimensions_list.sort()
        metric_name_dimension_dict[metric_name] = sorted_dimensions_list

    format_metrics_yml_file(metric_namespace, metric_name_dimension_dict, file_name)


if __name__ == '__main__':
    files = os.listdir("cloudwatch_metric_json")
    for file in files:
        main(file)
