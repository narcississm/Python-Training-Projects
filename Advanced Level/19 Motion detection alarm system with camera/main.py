import cv2

def main():
    print("Kamera ile Hareket Algılama Alarm Sistemi Başlatıldı...")
    cap = cv2.VideoCapture(0)

    # İlk frame'i al ve gri tonlamaya çevir
    ret, frame1 = cap.read()
    frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame1_gray = cv2.GaussianBlur(frame1_gray, (21, 21), 0)

    while True:
        ret, frame2 = cap.read()
        if not ret:
            break
        frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        frame2_gray = cv2.GaussianBlur(frame2_gray, (21, 21), 0)

        # Frame'ler arasındaki farkı al
        delta_frame = cv2.absdiff(frame1_gray, frame2_gray)
        thresh = cv2.threshold(delta_frame, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion_detected = False

        for contour in contours:
            if cv2.contourArea(contour) < 5000:  # Çok küçük hareketleri yok say
                continue
            motion_detected = True
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame2, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if motion_detected:
            cv2.putText(frame2, "HAREKET ALGILANDI!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

        cv2.imshow("Hareket Algılama", frame2)

        frame1_gray = frame2_gray

        key = cv2.waitKey(30)
        if key == 27:  # ESC tuşu ile çıkış
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
