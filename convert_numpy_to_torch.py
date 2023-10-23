import os
import shutil

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('numpy.py'):
                original_path = os.path.join(root, file)
                new_path = os.path.join(root, file.replace('numpy.py', 'torch.py'))
                shutil.copyfile(original_path, new_path)
                with open(new_path, 'r') as f:
                    lines = f.readlines()
                with open(new_path, 'w') as f:
                    f.write('import torch\n')
                    for line in lines:
                        if line.startswith('def '):
                            f.write('@torch.compile\n')
                        f.write(line)

if __name__ == "__main__":
    directory = "npbench/benchmarks/"
    process_directory(directory)
