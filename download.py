import os
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('split', choices=['training', 'validation', 'testing', 'domain_adaptation'])
parser.add_argument('--out-dir', default='./tmp')
args = parser.parse_args()

url_template = 'gs://waymo_open_dataset_v_1_2_0/{split}/{split}_%04d.tar'.format(split=args.split)
num_segs = {
    'training': 32,
    'validation': 8,
    'testing': 8
}

assert args.split in num_segs, 'Split does not exist. Please try another'

path = Path(args.out_dir)
path.mkdir(parents=True, exist_ok=True)

for seg_id in range(num_segs[args.split]):
    filename = (url_template % seg_id).split('/')[-1]
    print("Downloading " + filename)
    if (path/filename).is_file():
        print(filename + ' already downloaded. Skipping.')
        continue

    flag = os.system('gsutil cp ' + filename + ' ' + args.out_dir)
    assert flag == 0, 'Failed to download segment %d. Make sure gsutil is installed' % seg_id
