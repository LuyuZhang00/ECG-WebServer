import numpy as np
import cv2
from keras.models import load_model
from keras.utils import to_categorical



# 原始推理代码
# def ecg_inference(data):
#     for i in range(0, 5):
#         im_gray = cv2.imread('./Data/V/'+str(i)+'.png')
#         im_gray = im_gray.reshape((1, 128, 128, 3))
#         pred = model.predict(im_gray)
#         pred_class = pred.argmax(axis=-1)
#         print(pred_class[0])
#
# if __name__ == '__main__':
#     ecg_inference(0)


def ecg_inference(input_data):
    model = load_model('/home/bme/Documents/bme_ECG/django_ECG/apps/model_classification/ECG/ECGmodel_cp1.h5')
    # print(input_data)
    pred = model.predict(input_data)
    pred_class = pred.argmax(axis=-1)
    result=pred_class[0]
    # print(result)
    return result


if __name__ == '__main__':
    for i in range(0, 5):
        im_gray = cv2.imread('./Data/V/' + str(i) + '.png')
        im_gray = im_gray.reshape((1, 128, 128, 3))

        ecg_inference(im_gray)


#
# def cal_acc(label,prediction):
#     num=0
#     N = len(label)
#     for i in range(len(label)):
#         pred = np.argmax(prediction[i])
#         if label[i]==pred:
#             num+=1
#     return num/N
#
# def generate_label_2(t, num):
#     label = []
#     for i in range(t):
#         for k in range(7):
#             for j in range(num):
#                 label.append(k)
#
#     return np.array(label)
#
# def shuffle_data_label(data, label):
#     state = np.random.get_state()
#     np.random.shuffle(data)
#     np.random.set_state(state)
#     np.random.shuffle(label)
#     return data,label


# if __name__ == '__main__':
#     dataset = np.load('D:/Project/ECG/save/testdata700.npy')
#     label = generate_label_2(1, 100)
#     labels = to_categorical(label, num_classes=7)
#     img_data, labels = shuffle_data_label(dataset, labels)
#     test_data = img_data
#     test_label = labels
#
#     from keras.models import load_model
#     model = load_model('apps/model_classification/ECG/ECGmodel_cp1.h5')
#
#     test_predictions = model.predict(test_data)
#     acc = cal_acc(test_label, test_predictions)
#     print(acc)