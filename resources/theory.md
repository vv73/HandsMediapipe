# Mediapipe. Модуль Hands

## Чему научимся

На этом занятии мы:
* Познакомимся с библиотекой Mediapipe
* Научитесь использовать модуль Hands - распознавать положение кистей рук 

Эти знания можно будет использовать для проектов с управлением программой жестами руки.

## Введение

Сразу пример (Проект `Hands`, скрипт `intro.py`):

```python
1: # 0. Импортируем необходимое
2: # из библиотек OpenCV и MediaPipe
3: import cv2
4: import mediapipe as mp
5: from mediapipe.tasks import python
6: from mediapipe.tasks.python import vision
7: # и собственную функцию для рисования
8: from draw_landmarks import draw_landmarks_on_image
9: 
10: # 1. Создаем и настраиваем детектор
11: base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
12: options = vision.HandLandmarkerOptions(base_options=base_options,
13:                                        num_hands=2)
14: detector = vision.HandLandmarker.create_from_options(options)
15: 
16: # 2. Подготовливаем изображение
17: cv_mat = cv2.cvtColor(cv2.imread("pics/hand.jpg"), cv2.COLOR_RGB2BGR)
18: 
19: # Перводим его в формат Mediapipe-изображений
20: image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv_mat)
21: 
22: # 3. Самое главное: РАСПОЗНАЕМ
23: detection_result = detector.detect(image)
24: 
25: # Отрисовываем результат распознавания
26: annotated_image = draw_landmarks_on_image(image, detection_result)
27: cv2.imshow("Result", cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR))
28: 
29: # Задерживаем программу до нажатия на кнопку
30: cv2.waitKey(0)
```
Запустим эту программу  и получим окно с изображением руки, на которое наложены ключевые точки слово "Left" - детектировалась левая рука.

![enter image description here](https://github.com/vv73/HandsMediapipe/raw/master/_te/annotated_hand.png)

В этой программе много строк, но они просты для понимания, если не вдаваться в детали.

Наиболее сложные строчки, наверное, *11-13*
```python
11: base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
12: options = vision.HandLandmarkerOptions(base_options=base_options,
13:                                        num_hands=2)
```
Мы их разберем позже, а пока скажем, что это настройки (стандартные, которым передается модель, которая и распознает ладони и определяет их ключевые точки) по которым строится в строке 14 объект-распознаватель.

Функция `draw_landmarks_on_image()` в 14 строке вынесена в отдельный файл, ее мы тоже разберем позже.
