import cv2
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter('videoAct.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (width, height))
while True: 
    ret,frame = cap.read()
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
    writer.write(frame)
    cv2.imshow('frame', frame)
cap.release()
writer.release()
cv2.destroyAllWindows()

recap = cv2.VideoCapture('videoAct.mp4')
width2 = int(recap.get(cv2.CAP_PROP_FRAME_WIDTH))
height2 = int(recap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter('videoActRe.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (width2, height2))
check, vid = recap.read()
frame_list =[]
while (check == True):
    check, vid = recap.read()
    frame_list.append(vid)
frame_list.pop()
frame_list.reverse()

for frame in frame_list:
    writer.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

recap.release()
writer.release()
cv2.destroyAllWindows()


videos = ["videoAct.mp4", "videoActRe.mp4"]

video = cv2.VideoWriter("new_video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 20, (width, height))

for i in videos:
    curr_v = cv2.VideoCapture(i)
    while curr_v.isOpened():
        r, frame = curr_v.read()
        if not r:
            break
        video.write(frame)

video.release()
writer.release()
cv2.destroyAllWindows()