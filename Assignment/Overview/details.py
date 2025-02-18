import boto3

def list_services_in_apsouth1():
    session = boto3.Session(region_name='ap-south-1')
    client = session.client('resourcegroupstaggingapi')

    response = client.get_resources()

    services = set()
    for resource in response['ResourceTagMappingList']:
        arn = resource['ResourceARN']
        service = arn.split(':')[2]
        services.add(service)

    print("List of services in ap-south-1 region:")
    for service in services:
        print(service)
        if service == 'ec2':
            ec2_client = session.client('ec2')
            ec2_response = ec2_client.describe_instances()
            if ec2_response['Reservations']:
                for reservation in ec2_response['Reservations']:
                    for instance in reservation['Instances']:
                        print(f"Instance ID: {instance['InstanceId']}")
                        print(f"Instance Type: {instance['InstanceType']}")
                        print(f"Public IP: {instance.get('PublicIpAddress', 'N/A')}")
                        print(f"State: {instance['State']['Name']}")
                        print("------") # Add a separator
            else:
                print("No EC2 instances found.")
        elif service == 'rds':
            rds_client = session.client('rds')
            rds_response = rds_client.describe_db_instances()
            if rds_response['DBInstances']:
                for db_instance in rds_response['DBInstances']:
                    print(f"DB Instance ID: {db_instance['DBInstanceIdentifier']}")
                    print(f"DB Instance Class: {db_instance['DBInstanceClass']}")
                    print(f"Engine: {db_instance['Engine']}")
                    print(f"DB Instance Status: {db_instance['DBInstanceStatus']}")
                    print("------")
            else:
                print("No RDS instances found.")
        else:
            print(f"No detailed output available for service: {service}")

if __name__ == "__main__":
    list_services_in_apsouth1()
