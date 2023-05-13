import cv2

FRAMES = 60


def convert_video_to_images(video_path: str):
    # 動画の読み込み
    cap = cv2.VideoCapture(video_path)

    images = []

    if not cap.isOpened():
        print("not opened file")
        return images

    cap.set(cv2.CAP_PROP_POS_FRAMES, FRAMES)
    frame_count = 0
    # 動画のフレームごとに処理
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if frame_count % FRAMES == 0:
                # 画像をリストに追加
                images.append(frame)
            frame_count += 1
        else:
            break

    # メモリ解放
    cap.release()

    return images
