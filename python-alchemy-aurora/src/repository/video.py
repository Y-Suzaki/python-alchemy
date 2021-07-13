from repository.session_context import SessionContext
from repository.model.video_image import VideoImage


class VideoRepository:
    def __init__(self, db_name: str):
        self.session_context = SessionContext(db_name)

    def save_video_meta(self):
        with self.session_context.make() as session:
            video_image = VideoImage(id=1, event_id=10, video_path='aaa', video_file='vvv')
            session.add(video_image)
