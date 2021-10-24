# Lets create EC2 instances using Python BOTO3
import boto3

def create_ec2_instance():
    try:
        print("Creating EC2 instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId="ami-041d6256ed0f2061c",
            MinCount = 1,
            MaxCount = 1,
            InstanceType = "t2.micro",
            KeyName = "myec2key"
        )
    except Exception as e:
        print(e)

def describe_ec2_instance():
    try:
        print("Describing EC2 instance")
        resource_ec2 = boto3.client("ec2")
        # print(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
        # return str(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
        print(resource_ec2.describe_instances(InstanceIds=['i-053404fc5a92e8547']))
    except Exception as e:
        print(e)

def reboot_ec2_instance():
    try:
        print("Reboot EC2 Instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.reboot_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)



def stop_ec2_instance():
    try:
        print("Stop EC2 Instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.stop_instances(InstanceIds=['i-053404fc5a92e8547']))
    except Exception as e:
        print(e)


def start_ec2_instance():
    try:
        print("Start EC2 Instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.start_instances(InstanceIds=['i-053404fc5a92e8547']))

    except Exception as e:
        print(e)

def terminate_ec2_instance():
    try:
        print("Terminate EC2 Instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.terminate_instances(InstanceIds=['i-053404fc5a92e8547']))
    except Exception as e:
        print(e)


#create_ec2_instance()
#describe_ec2_instance()
#reboot_ec2_instance()
#stop_ec2_instance()
#start_ec2_instance()
#terminate_ec2_instance()
