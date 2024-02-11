import json

def extract_container_distribution(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    list_container = []
    for line in lines[1:]:
        list_container.append(line.split('   ')[3])
    return list_container

# Replace 'your_file.txt' with the path to your file
base_dir = '/mnt/Windows/Users/taufi/MyFile/Projects/hasil/paper_tesis_journal_2/worker_logs/'
request_type = ['default_docker_swarm']
ai_model = ['no_prune', 'l1_norm', 'l2_norm', 'random_unstructured']
list_result = dict(l1_norm=[], l2_norm=[], no_prune=[], random_unstructured=[])
for rtype in request_type:
    for amodel in ai_model:
        for i in range (12):
            list_result[amodel].append(extract_container_distribution(f'{base_dir}/{rtype}/{amodel}/{i+1}.txt'))
print(json.dumps(list_result))
