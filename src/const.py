import os
# プロジェクトの相対パス
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def video_path():
    return os.path.join(base_path,'option','test.mp4')