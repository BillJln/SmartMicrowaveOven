import cv2
import os


def take_a_picture(camera):
    cap = cv2.VideoCapture(camera, cv2.CAP_DSHOW)  # 打开摄像头0 1

    while (1):
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)  # 将图像左右调换回来正常显示
        path = 'D:/AI_Microwave_Oven/Test'

        cv2.imshow("capture", frame)  # 摄像头窗口

        if cv2.waitKey(1) & 0xFF == ord('s'):  # 按下s就截图保存并退出
            cv2.imwrite(os.path.join(path, "test_picture.jpg"), frame)  # 保存路径
            break

    cap.release()
    cv2.destroyAllWindows()

# take_a_picture(0)
