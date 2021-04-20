from sklearn import svm
import pickle
import os, sys
data = []
label = []
with open(os.path.join(sys.path[0], "data_train.txt"), "r") as f: 
    for line in f:
        words = line.strip().split()
        label.append(float(words[0]))
        text = []
        for i in range(1,len(words)):
            text.append(float(words[i]))
        data.append(text)

# Build model
svc = svm.SVC(C=1, kernel="rbf", gamma=0.5)
svc.fit(data,label)

# Run model
while True:
    a=input()
    if (a=="-1"):
        break
    b=input()
    c=input()
    d=input()
    print(int(svc.predict([[a,b,c,d]])))


