import boto3 

# Bash script to install Wazuh components
user_data = """#!/bin/bash
yum update -y
curl -sO https://packages.wazuh.com/4.3/wazuh-install.sh && sudo bash ./wazuh-install.sh -a"""

# Method to get EC2 Instance Info 
def describe_EC2_instance():
    try:
        print("Describing EC2 instance")
        ec2 = boto3.client('ec2')
        response = ec2.describe_instances()['Reservations'][0]['Instances'][0]['InstanceId']
        print(response)
        return str(response)
    # Check for error messages and display in console
    except Exception as e:
        print(e)
# Method to create an EC2 instance
def create_EC2_instance():
    try:
        print("Creating EC2 instance")
        ec2 = boto3.resource('ec2')
        ec2.create_instances(
            ImageId='ami-0cff7528ff583bf9a', 
            MinCount=1, 
            MaxCount=1,
            InstanceType='t2.xlarge',
            KeyName='NewEC2TestKey',
            UserData= user_data,
            SecurityGroupIds=['sg-07adfb39e298f97a3','sg-02fa10e7166194e30'],
            BlockDeviceMappings=[
                { 'DeviceName': '/dev/xvda',
                    'Ebs': { 'VolumeSize': 100, 'VolumeType': 'gp2' }
                }]
            )
        print("Security groups added to instance")
        print("EC2 instance created... Attaching volume")
        print("Volume attached")
    except Exception as e:
        print(e)

create_EC2_instance()

