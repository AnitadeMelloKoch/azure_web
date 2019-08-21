import pandas as pd
import numpy as np
from sklearn import svm
import argparse

labels = ["day",
"hour",
"minute",
"lyingDown", 
"sitting", 
"walking", 
"running", 
"bicycling",
"sleeping", 
"drivingDriver",
"drivingPass",
"exercise",
"shopping", 
"strolling", 
"stairsUp",
"stairsDown",
"standing",
"labWork",
"inClass",
"inMeeting",
"cooking",
"drinkingAlcohol",
"shower",
"cleaning",
"laundry",
"washingDishes",
"watchTV",
"surfInternet",
"singing",
"talking",
"computerWork",
"eating",
"toilet",
"grooming",
"dressing",
"withCoworker", 
"withFriends",
"mainWorkplace",
"indoors",
"outdoors",
"inCar",
"onBus",
"home",
"restaurant",
"atParty",
"atBar",
'beach',
'atGym',
"elevator",
"atSchool",
"anomalie"]

def main(nor_data_train, data_to_analyze):


    # Setting the hyperparameters for Once Class SVM

    oneclass = svm.OneClassSVM(kernel='rbf', gamma=0.01, nu=0.2)

    print("Start training")

    oneclass.fit(nor_data_train)

    fraud_pred = oneclass.predict(data_to_analyze)

    # unique, counts = np.unique(fraud_pred, return_counts=True)
    # print (np.asarray((unique, counts)).T)
    # print(fraud_pred)
    fraud_pred[fraud_pred == 1] = 0
    fraud_pred[fraud_pred == -1] = 1
    print(fraud_pred)

    return fraud_pred

if __name__ == '__main__':
    AP = argparse.ArgumentParser()
    AP.add_argument("--train_data", type=list, help="List containing non-anomolous data")
    AP.add_argument("--data_to_analyze", type=list, help="List containing data to analyze")
    AP.add_argument("--points_to_analyze", type=int, default=96, help="Number of points for SVM to do anomaly detection on")

    parsed = AP.parse_args()

    main(   nor_data_train=parsed.train_data,
            data_to_analyze=parsed.data_to_analyze)