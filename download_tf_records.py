
import os
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('split', choices=['training', 'validation', 'testing', 'domain_adaptation'])
parser.add_argument('--out-dir', default='./tmp')
parser.add_argument('--tf_files', default='missing_tfs.txt')
args = parser.parse_args()

url_template = 'gs://waymo_open_dataset_v_1_2_0_individual_files/{split}/%s'.format(split=args.split)
num_segs = {
    'training': 32,
    'validation': 8,
    'testing': 8
}

assert args.split in num_segs, 'Split does not exist. Please try another'

path = Path(args.out_dir)
path.mkdir(parents=True, exist_ok=True)

with open(args.tf_files, 'r') as f:
    tf_files = f.read().splitlines()

for tf_file in tf_files:
    url = url_template % tf_file
    print(f'Downloading {tf_file}')
    if (path/tf_file).is_file():
        print(f'{tf_file} is already downloaded. Skipping.')
        continue
    flag = os.system('gsutil cp ' + url + ' ' + args.out_dir)
    assert flag == 0, f'Failed to download {tf_file}. Make sure gsutil is installed'


# for seg_id in range(num_segs[args.split]):
#     url = url_template % seg_id
#     filename = url.split('/')[-1]
#     print("Downloading " + filename)
#     if (path/filename).is_file():
#         print(filename + ' already downloaded. Skipping.')
#         continue

#     flag = os.system('gsutil cp ' + url + ' ' + args.out_dir)
#     assert flag == 0, 'Failed to download segment %d. Make sure gsutil is installed' % seg_id
