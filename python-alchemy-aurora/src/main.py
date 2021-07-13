from repository.video import VideoRepository


video = VideoRepository('sample')
video.save_video_meta()

print(video)
