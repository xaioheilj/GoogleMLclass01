# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from sklearn import tree
features = [[140,1],[130,1],[150,1],[170,0]] #[重量，是否光滑]
labels=[0,0,1,1] #[苹果，苹果，橘子，橘子]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels)
print(clf.predict([[160,0]]))
