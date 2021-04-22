from subprocess import PIPE
import subprocess
import sys, os
# import pickle
# import os

def check_python():
    data = []
    label = []
    for line in open(os.path.join(sys.path[0], "data_train.txt"), 'r'):
        words = line.strip().split()
        label.append(words[0])
        text = []
        for i in range(1,len(words)):
            text.append(words[i])
        data.append(text)
    for line in open(os.path.join(sys.path[0], "data_test.txt"), 'r'):
        words = line.strip().split()
        label.append(words[0])
        text = []
        for i in range(1,len(words)):
            text.append(words[i])
        data.append(text)
    count=0
    s=""
    for i in range(len(data)):
        x=data[i]
        s=s+x[0]+"\n"+x[1]+"\n"+x[2]+'\n'+x[3]+'\n'
    s=s+"-1\n"
    s=s.encode()
    result = subprocess.run(
        ['python3', os.path.join(sys.path[0], "model.py")], stdout=PIPE, stderr=PIPE, input=s
    )
    res = result.stdout.decode().split("\n")
    print(res)
    for i in range(len(label)):
        if int(res[i])==int(label[i]):
            count+=1
    # test = model.predict(data)
    # count=0
    # for i in range(len(test)):
    #     if test[i] == label[i]:
    #         count +=1
    return str(count/len(data)*100)+"%"

def check_cpp():
    data = []
    label = []
    for line in open(os.path.join(sys.path[0], "data_train.txt"), 'r'):
        words = line.strip().split()
        label.append(words[0])
        text = []
        for i in range(1,len(words)):
            text.append(words[i])
        data.append(text)
    for line in open(os.path.join(sys.path[0], "data_test.txt"), 'r'):
        words = line.strip().split()
        label.append(words[0])
        text = []
        for i in range(1,len(words)):
            text.append(words[i])
        data.append(text)
    count=0
    s=""
    for i in range(len(data)):
        x=data[i]
        s=s+x[0]+"\n"+x[1]+"\n"+x[2]+'\n'+x[3]+'\n'
    s=s+"-1\n"
    s=s.encode()
    result_c = subprocess.run(
        ['g++', os.path.join(sys.path[0], "model_c.cpp"), '-o', 'model_c'])
    result_c = subprocess.run(
        [os.path.join(sys.path[0], "model_c")], stdout=PIPE, stderr=PIPE, input=s
    )
    res = result_c.stdout.decode().split("\n")
    for i in range(len(label)):
        if int(res[i])==int(label[i]):
            count+=1
    # test = model.predict(data)
    # count=0
    # for i in range(len(test)):
    #     if test[i] == label[i]:
    #         count +=1
    return str(count/len(data)*100)+"%"

# x=input()
print(check_python())
# print(check_cpp())



# result = subprocess.run(
#     ['python', os.path.join(sys.path[0], "model.py")], stdout=PIPE, stderr=PIPE, input=b"4.2\n2.3\n4.5\n3.5\n4.2\n2.3\n4.5\n3.5\n"
# )
# res = result.stdout.decode().split("\n")
# print(len(res))
# for x in res:
#     print(x)
# result_c = subprocess.run(
#     ['g++', os.path.join(sys.path[0], "model_c.cpp"), '-o', 'model_c'])
# result_c = subprocess.run(
#     [os.path.join(sys.path[0], "model_c")], stdout=PIPE, stderr=PIPE, input=b"4.2\n2.3\n4.5\n3.5\n4.2\n2.3\n4.5\n3.5\n"
# )
# print(result_c.stdout.decode())
