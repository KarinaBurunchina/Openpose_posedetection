
# -*- coding: utf-8 -*-

import os
from pathlib import Path
from subprocess import Popen

root = Path().parent.absolute()

videos_dir = 'videos'
output_dir = 'output'
openpose_dir = 'openpose'

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

for vid in os.listdir(videos_dir):
    vid_fullpath = os.path.join(root, videos_dir, vid)
    vid_output = os.path.join(root, output_dir, vid[:-4])
    if not os.path.exists(vid_output):
        os.mkdir(vid_output)

    f = open("run.bat", 'w', encoding="utf-8")
    content = 'cd {} \nbin\\OpenPoseDemo.exe --video {} --write_json {} --display 0 --render_pose 0 --net_resolution "-1x192"'.format(openpose_dir, vid_fullpath, vid_output)
    f.write(content)
    f.close()
    p = Popen("run.bat")
    p.wait()
    