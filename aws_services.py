import json

import config


class AWS_Services:
    def __init__(self):
        self.client = config.ConfigureClient().client

    def get_all_services(self):
        try:
            service_code_list = []
            data = self.client.describe_services()
            for value in data['Services']:
                service_code_list.append(json.dumps(value['ServiceCode']))
            print(service_code_list)

        except Exception as e:
            print(str(e))

    def describe_service(self, ServiceCode):
        try:
            service = self.client.describe_services(ServiceCode=ServiceCode)
            print(service)
        except Exception as e:
            print(str(e))

    def get_attribute_values(self, ServiceCode, AttributeName):
        try:
            attribute = self.client.get_attribute_values(
                ServiceCode=ServiceCode,
                AttributeName=AttributeName,
            )
            print(attribute)
        except Exception as e:
            print(str(e))


aws = AWS_Services()
'''
aws.get_all_services()
aws.describe_service('AmazonEC2')
aws.get_attribute_values('AmazonEC2', 'volumeType')
aws.get_attribute_values('AmazonEC2', 'volumeApiName')
aws.get_attribute_values('AmazonEC2', 'maxThroughputvolume')
aws.get_attribute_values('AmazonEC2', 'maxIopsvolume')
aws.get_attribute_values('AmazonEC2', 'maxVolumeSize')
'''
aws.get_all_services()
aws.describe_service('AmazonEC2')
aws.get_attribute_values('AmazonEC2', 'operatingSystem')
aws.get_attribute_values('AmazonEC2', 'instanceType')
aws.get_attribute_values('AmazonEC2', 'location')