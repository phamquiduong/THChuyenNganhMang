from sklearn import svm
import pickle
import os
data = []
label = []
for line in open('data_train.txt', 'r'):
    words = line.strip().split()
    label.append(float(words[0]))
    text = []
    for i in range(1,len(words)):
        text.append(float(words[i]))
    data.append(text)

# Build model
svc = svm.SVC(C=1, kernel="rbf", gamma=0.1)
svc.fit(data,label)

# Save model
s=input()
pickle.dump(svc,open(os.path.join(s+".py"), 'wb'))