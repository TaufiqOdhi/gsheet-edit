import json

def extract_gpu_memory_usage(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    memory_usage = []
    process_list = []

    for line in lines:
        if 'MiB' in line and 'MiB /' in line:
            parts = line.split()
            used_memory = parts[8]  # Adjust the index as per the format
            memory_usage.append(used_memory[:-3])
        elif 'python' in line and 'MiB' in line:
            parts = line.split()
            # Find the index for 'python' and then get the memory usage
            try:
                python_index = parts.index('python')
                used_memory = parts[python_index + 1]  # Memory usage is right after 'python'
                process_list.append(used_memory[:-3])
            except ValueError:
                continue  # 'python' not found in this line

    return dict(memory_usage=memory_usage, process_list=process_list)

# Replace 'your_file.txt' with the path to your file
base_dir = 'C:/Users/taufi/MyFile/Projects/hasil/paper_tesis_conference_1/'
request_type = ['request_sequential', 'request_konkuren']
ai_model = ['l1_norm', 'l2_norm', 'no_prune', 'random_unstructured']
list_result = dict(l1_norm=[], l2_norm=[], no_prune=[], random_unstructured=[])
for rtype in request_type:
    for amodel in ai_model:
        for i in range (12):
            list_result[amodel].append(extract_gpu_memory_usage(f'{base_dir}/{rtype}/{amodel}/{i+1}.txt'))
print(json.dumps(list_result))
