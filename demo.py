import etcd3
import json


etcd = etcd3.client(
    host='192.168.50.249',
    port='2379'
)

service_name = 'my.service'
results = etcd.get_prefix('/micro-registry/' + service_name)
for result, md in results:
    service_info = json.loads(result.decode('utf-8'))

    # print(service_info['name'])
    # print(service_info['version'])
    # print(services['endpoints'])
    # print(service_info['nodes'])

    nodes_info = service_info['nodes']
    for node_info in nodes_info:
        # print(json.dumps(node_info, indent=4))
        id = node_info['id']
        address = node_info['address']
        port = node_info['port']
        print('id address port: ', id, address, port)
        break
