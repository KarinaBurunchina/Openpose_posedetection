# Openpose_posedetection
The code detects 3 emotions: Happy, Disgust, and Fear using Openpose.


# In order to run the code:
1. Import video to 'videos' folder
2. Run parse_videos.py (it will save videos in 'outout' folder) 
    -> if you have any issues with CUDA. Try to decrease net_resolution by multiple of 16.
3. Run to_format.py (converts to csv file)
4. run pose_detection.py (make sure to change the path to your own for csv file)

-> the code counts seconds for videos with 30 fps. You should change it in the code, if you have higher/lower fps.

-> The output will be the number of each states in the video + each duration. The output does not shows the duration for states last for less than 1 second.
