
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import sys
import os 
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn import tree
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import warnings
warnings.filterwarnings("ignore")
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import GradientBoostingClassifier
#from IPython.display import display 


# In[2]:

X = pd.read_csv('file:/Users/apple/Desktop/projectFinal/HR_final.csv')
y = X['left']
print('Number of records: ', X.shape[0])


# In[3]:

print('Number of features: ', X.shape[1])


# In[4]:

X.isnull().values.ravel().sum() # missing data check


# In[5]:

X.dtypes # data type schema


# In[6]:

X.salary.unique()  # salary data display


# In[7]:

X.salary.replace({'low':1,'medium':2,'high':3},inplace=True) #salary data convertion


# In[8]:

X.salary.unique() # salary data convertion check


# In[9]:

X.department.unique() #department data display


# In[10]:

#department data convertion
X.department.replace({'sales':1,'accounting':2,'hr':3,'technical':4,
'support':5,'management':6,'IT':7,'product_mng':8,'marketing':9,'RandD':10},inplace=True) 


# In[11]:

#department data convertion check
X.department.unique() 


# In[12]:

features = X[['satisfaction_level','last_evaluation','number_project','average_montly_hours','time_spend_company','Work_accident','promotion_last_5years','department','salary',]]
X = features
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, random_state=0,test_size=0.2)
print('Training set volume:', X_train.shape[0])
print('Test set volume:', X_test.shape[0])


# In[13]:

# logistic regression
modelLogreg = LogisticRegression(max_iter=100,random_state=0,multi_class='ovr',n_jobs=2)
modelLogreg.fit(X_train,y_train)
print("modelLogreg Accuracy Rate, which is calculated by accuracy_score() is: %f" 
      % accuracy_score(y_test,modelLogreg.predict(X_test))) # %f float variable


# In[14]:

modelLogreg.predict_proba(X_test)


# In[15]:

modelLogreg.predict(X_test)


# In[16]:

modelLogreg.coef_


# In[17]:

modelLogreg.intercept_


# In[18]:

modelLogreg.n_iter_


# In[19]:

modelLogreg.decision_function(X_test)


# In[20]:

modelLogreg.predict(X_test)


# In[ ]:




# In[21]:

#NaiveBayes 
modelGaussianNB = GaussianNB()
modelGaussianNB.fit(X_train, y_train)
print("modelGaussianNB Accuracy Rate, which is calculated by accuracy_score() is: %f" 
      % accuracy_score(y_test,modelGaussianNB.predict(X_test)))


# In[22]:

modelGaussianNB.class_prior_


# In[23]:

modelGaussianNB.class_count_


# In[24]:

modelGaussianNB.predict(X_test)


# In[ ]:




# In[25]:

modelMultinomialNB = MultinomialNB()
modelMultinomialNB.fit(X_train, y_train)
print("modelMultinomialNB Accuracy Rate, which is calculated by accuracy_score() is: %f" 
      % accuracy_score(y_test,modelMultinomialNB.predict(X_test)))


# In[26]:

modelMultinomialNB.class_log_prior_ 


# In[27]:

modelMultinomialNB.coef_


# In[28]:

modelMultinomialNB.intercept_


# In[29]:

modelMultinomialNB.class_count_


# In[30]:

modelMultinomialNB.feature_count_


# In[31]:

modelMultinomialNB.feature_log_prob_


# In[ ]:




# In[32]:

modelBernoulliNB = BernoulliNB()
modelBernoulliNB.fit(X_train, y_train)
print("modelBernoulliNB Accuracy Rate, which is calculated by accuracy_score() is: %f" 
      % accuracy_score(y_test,modelBernoulliNB.predict(X_test)))


# In[33]:

modelBernoulliNB.class_count_


# In[34]:

modelBernoulliNB.class_log_prior_


# In[35]:

modelBernoulliNB.feature_count_


# In[36]:

modelBernoulliNB.feature_log_prob_


# In[ ]:




# In[37]:

#DecisionTree
modelDecisionTree = tree.DecisionTreeClassifier(max_depth=5,min_samples_split=100,min_samples_leaf=10,random_state=0)
modelDecisionTree.fit(X_train, y_train)
print("modelDecisionTree Accuracy Rate, which is calculated by accuracy_score() is: %f" 
      % accuracy_score(y_test, modelDecisionTree.predict(X_test)))


# In[38]:

modelDecisionTree.predict(X_test)


# In[39]:

modelDecisionTree.feature_importances_


# In[40]:

modelDecisionTree.tree_ 


# In[41]:

#modelDecisionTree.decision_path(X_test,check_input=True)


# In[42]:

modelDecisionTree.apply(X_test,check_input=True)


# In[ ]:




# In[43]:

# Support Vector Machine
modelSVM = svm.SVC(kernel='rbf',probability=False,shrinking=True,max_iter=1000,random_state=0)
modelSVM.fit(X_train,y_train)
print("modelSVM Accuracy Rate, which is calculated by accuracy_score() is: %f" 
      % accuracy_score(y_test, modelSVM.predict(X_test)))


# In[44]:

modelSVM.predict(X_test)


# In[45]:

modelSVM.support_


# In[46]:

modelSVM.support_vectors_


# In[47]:

modelSVM.dual_coef_


# In[ ]:




# In[48]:

#RandomForest
modelRandomForest = RandomForestClassifier(n_estimators =100 ,max_features='sqrt',max_depth=5,min_samples_split=100,min_samples_leaf=10,random_state=0)
modelRandomForest.fit(X_train, y_train)
print("modelRandomForest Accuracy Rate, which is calculated by accuracy_score() is: %f"
      % accuracy_score(y_test, modelRandomForest.predict(X_test)))


# In[49]:

modelRandomForest.predict(X_test)


# In[50]:

modelRandomForest.feature_importances_


# In[51]:

modelRandomForest.oob_score


# In[52]:

modelRandomForest.estimators_


# In[53]:

modelRandomForest.apply(X_test)


# In[ ]:




# In[54]:

#knn
modelKNN=KNeighborsClassifier(n_neighbors=10,leaf_size=10,algorithm='auto')
modelKNN.fit(X_train,y_train)
print("modelKNN Accuracy Rate, which is calculated by accuracy_score() is: %f"
      %accuracy_score(y_test,modelKNN.predict(X_test)))


# In[55]:

modelKNN.predict(X_test)


# In[56]:

modelKNN.kneighbors(X=None, n_neighbors=None, return_distance=True)


# In[57]:

modelKNN.kneighbors_graph(X=None, n_neighbors=None, mode='connectivity')


# In[ ]:




# In[58]:

modelBagging = BaggingClassifier(n_estimators=100,max_samples=0.5, max_features=0.5,random_state=0)
modelBagging.fit(X_train,y_train)
print("modelBagging Accuracy Rate, which is calculated by accuracy_score() is: %f"
      %accuracy_score(y_test,modelBagging.predict(X_test)))


# In[59]:

modelBagging.estimators_


# In[60]:

modelBagging.estimators_samples_


# In[61]:

modelBagging.estimators_features_


# In[62]:

modelBagging.classes_


# In[64]:

modelBagging.predict(X_test)


# In[ ]:




# In[63]:

modelBoosting = GradientBoostingClassifier(n_estimators =100 ,max_features='sqrt',max_depth=5,min_samples_split=100,min_samples_leaf=10,random_state=0)
modelBoosting.fit(X_train, y_train)
print("Accuracy is: %f"
     % accuracy_score(y_test, modelBoosting.predict(X_test)))


# In[65]:

modelBoosting.feature_importances_


# In[66]:

modelBoosting.train_score_


# In[67]:

modelBoosting.loss_


# In[68]:

modelBoosting.init_


# In[69]:

modelBoosting.estimators_


# In[70]:

modelBoosting.decision_function(X_test)


# In[71]:

modelBoosting.apply(X_test)


# In[72]:

modelBoosting.staged_decision_function(X_test)


# In[73]:

modelBoosting.predict(X_test)


# In[ ]:
s_level=float(sys.argv[1])
l_eva=float(sys.argv[2])
num_pro=float(sys.argv[3])
a_hours=float(sys.argv[4])
time_spent=float(sys.argv[5])
work_acc=float(sys.argv[6])
promo=float(sys.argv[7])

dpt=float(sys.argv[8])
slry=float(sys.argv[9])
result=modelBoosting.predict([s_level,l_eva,num_pro,a_hours,time_spent,work_acc,promo,dpt,slry])
print(result[0])



# In[ ]:



