from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy import Column, Integer, String


class VideoImage(declarative_base()):
    # テーブル名やカラム定義は必須
    __tablename__ = 'video_image'
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer)
    video_path = Column(String(128))
    video_file = Column(String(128))
