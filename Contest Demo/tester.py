from subprocess import PIPE
import subprocess
import sys, os

def check_python(name):
    data = []
    label = []
    path = os.path.dirname(os.path.realpath(__file__))
    for line in open(os.path.join(path, "data_train.txt"), 'r'):
        words = line.strip().split()
        label.append(words[0])
        text = []
        for i in range(1,len(words)):
            text.append(words[i])
        data.append(text)
    for line in open(os.path.join(path, "data_test.txt"), 'r'):
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
    name=name+".py"
    result = subprocess.run(
        ['python3', os.path.join(path, name)], stdout=PIPE, stderr=PIPE, input=s
    )
    res = result.stdout.decode().split("\n")
    for i in range(len(label)):
        if int(res[i])==int(label[i]):
            count+=1
    return str(count/len(data)*100)+"%"

def check_cpp(name):
    data = []
    label = []
    path = os.path.dirname(os.path.realpath(__file__))
    for line in open(os.path.join(path, "data_train.txt"), 'r'):
        words = line.strip().split()
        label.append(words[0])
        text = []
        for i in range(1,len(words)):
            text.append(words[i])
        data.append(text)
    for line in open(os.path.join(path, "data_test.txt"), 'r'):
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
        ['g++', os.path.join(os.path.join(path, name+'.cpp')), '-o', os.path.join(os.path.join(path, name))]
    )
    result_c = subprocess.run(
        [os.path.join(os.path.join(path, name))], stdout=PIPE, stderr=PIPE, input=s
    )
    res = result_c.stdout.decode().split("\n")
    for i in range(len(label)):
        if int(res[i])==int(label[i]):
            count+=1
    return str(count/len(data)*100)+"%"

def check_java(dir,name):
    data = []
    label = []
    path = os.path.dirname(os.path.realpath(__file__))
    for line in open(os.path.join(path, "data_train.txt"), 'r'):
        words = line.strip().split()
        label.append(words[0])
        text = []
        for i in range(1,len(words)):
            text.append(words[i])
        data.append(text)
    for line in open(os.path.join(path, "data_test.txt"), 'r'):
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
    path = os.path.join(os.path.join(path, dir))
    result_java = subprocess.run(
        ['javac', os.path.join(os.path.join(path, name+'.java'))]
    )
    result_java = subprocess.run(
        ['java', '-cp', path, name], stdout=PIPE, stderr=PIPE, input=s
    )
    res = result_java.stdout.decode().split("\n")
    for i in range(len(label)):
        if int(res[i])==int(label[i]):
            count+=1
    return str(count/len(data)*100)+"%"

# x=input()
# print(check_python())
# print(check_cpp('test'))
# print(check_java('java1','test'))



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
