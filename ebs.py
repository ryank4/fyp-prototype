import json

import config
import extract


class EBS:
    def __init__(self):
        self.client = config.ConfigureClient().client

    def get_storage_volume(self, volume_type, iops, throughput, storage_amount):
        try:
            data = self.client.get_products(ServiceCode='AmazonEC2', Filters=
            [
                {'Type': 'TERM_MATCH', 'Field': 'volumeType', 'Value': 'General Purpose'},
                {'Type': 'TERM_MATCH', 'Field': 'volumeApiName', 'Value': volume_type},
                {'Type': 'TERM_MATCH', 'Field': 'usagetype', 'Value': 'USE2-EBS:VolumeUsage.'+volume_type},
            ])
            usage_types = []
            for value in data['PriceList']:
                json_value = json.loads(value)
                usage_type = json_value['product']['attributes']['usagetype']
                usage_types.append(usage_type)

            price = extract.extract_values(json_value, 'USD')
            price_per_gb = price[0]

            total = 0

            if volume_type == 'gp3':
                iops = (float(iops) - 3000)
                if iops > 0:
                    iops = iops * 0.005
                    total = total + iops
                storage_amount = float(storage_amount) * float(price_per_gb)
                total = total + storage_amount
                throughput = (float(throughput) - 125)
                if throughput > 0:
                    throughput = (throughput * 40.96) / 1024
                    total = total + throughput

            if volume_type == 'gp2':
                total = total + (storage_amount * 0.1)

            #l = sorted((usage_types))
            #print(*l, sep="\n")

        except Exception as e:
            print(str(e))

        return total


def main():
    region = 'us-east-2'
    volume_type = 'gp2'
    throughput = 1000
    iops = 1000
    storage_amount = 100

    ebs = EBS()
    value = ebs.get_storage_volume(volume_type, iops, throughput, storage_amount)
    print(value)


#main()
