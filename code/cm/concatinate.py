from moviepy.editor import *

# load clips
clip_01 = VideoFileClip('video/lavi.m4v')
clip_02 = VideoFileClip('video/laviMom.m4v')

# join + write
result_clip = concatenate_videoclips([clip_01, clip_02])
result_clip.write_videofile('out/combined.mp4')

