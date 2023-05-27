import numpy as np
from tensorflow.keras.models import load_model
# def cal_acc(label,prediction):
#     num=0
#     N = len(label)
#     for i in range(len(label)):
#         pred = np.argmax(prediction[i])
#         if label[i]==pred:
#             num+=1
#     return num/N
#
#
# def shuffle_data_label(data, label):
#     state = np.random.get_state()
#     np.random.shuffle(data)
#     np.random.set_state(state)
#     np.random.shuffle(label)
#     return data,label
#
#
# def generate_label(num):
#     label = []
#     for j in range(2):
#         for i in range(num):
#             label.append(j)
#     return np.array(label)
#
# def generate_label_2(t, num):
#     label = []
#     for i in range(t):
#         for k in range(2):
#             for j in range(num):
#                 label.append(k)
#
#     return np.array(label)

#原始推理代码

# def hs_inference(data):
#     dataset = np.load('./testdata20.npy')  # 20*128*128*3
#     print(dataset.shape)
#
#     test_data = dataset  # [0:1,:,:]         # 1*128*128*3
#
#
#     model = load_model('./HSmodel_cp01.h5')
#     test_predictions = model.predict(test_data)
#     for i in range(len(test_data)):
#         print(np.argmax(test_predictions[i]))
#
# if __name__ == '__main__':
#     hs_inference(0)

#更改后的推理代码
def hs_inference(input_data):
    # dataset = np.load('./testdata20.npy')  # 20*128*128*3
    # print(dataset.shape)
    # test_data = dataset  # [0:1,:,:]         # 1*128*128*3


    model = load_model('/home/bme/Documents/bme_ECG/django_ECG/apps/model_classification/HS/HSmodel_cp01.h5')
    test_predictions = model.predict(input_data)
    result = np.argmax(test_predictions)
    print(result)
    return result

if __name__ == '__main__':
    dataset = np.load('./testdata20.npy')
    test_data = dataset[0:1,:,:]
    hs_inference(test_data )

