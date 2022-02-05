import json
import os
from pathlib import Path

output_dir = 'output/'
csv_dir = 'csv/'

if not os.path.exists(csv_dir):
    os.mkdir(csv_dir)

for vid in os.listdir(output_dir): 
    print(vid)
    resfile = open(csv_dir + vid + ".csv", 'w')
    resfile.write("frame_id")

    for i in range(25):
        resfile.write(", p_x" + str(i))
        resfile.write(", p_y" + str(i))
        resfile.write(", p_c" + str(i))
    resfile.write("\n")

    for i, js in enumerate(os.listdir(output_dir + vid)):
        
        with open(output_dir + vid + '/'+ js) as f:
            data = json.load(f)
        
        try:
            resfile.write(str(i))
            p = data['people'][-1]['pose_keypoints_2d'] 

            for datapoint in p:
                resfile.write("," + str(datapoint))                  
            resfile.write("\n")                                  
        except:
            continue                                    