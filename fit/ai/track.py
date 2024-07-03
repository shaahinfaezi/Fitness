import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pickle



def get_dataset():

  
    dataframe1 = pd.read_csv('C:/Users/YEKTA-PC/Desktop/Fitness/fit/ai/exercise_dataset.csv')
    print(dataframe1)
    x=[]
    y=[]
    for i in range(130):
        x.append([dataframe1["Actual Weight"][i],dataframe1["Age"][i],dataframe1["BMI"][i]])
        y.append(dataframe1["Exercise Intensity"][i])
    return x,y
    



def plot_losses(train_losses, test_losses):
    epochs = range(len(train_losses))
    plt.figure(figsize=(8, 5))
    plt.plot(epochs, train_losses, label='Train Loss')
    plt.plot(epochs, test_losses, label='Test Loss', color='red')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()



def train_mlp(x_train, y_train, x_test, y_test, hidden_layer_sizes, activation, learning_rate=0.01, max_iter=1000, alpha=0.0001):
    mlp = MLPRegressor(hidden_layer_sizes=hidden_layer_sizes, activation=activation, 
                       learning_rate_init=learning_rate, max_iter=max_iter, solver='adam', alpha=alpha)
    
    train_losses = []
    test_losses = []

    for epoch in range(max_iter):
        # fit and prediction on train and test
        mlp.partial_fit(x_train,y_train)
        y_pred_train=mlp.predict(x_train)
        y_pred_test=mlp.predict(x_test)

        # calculate loss for each epoch
        train_loss=mean_squared_error(y_train, y_pred_train)
        test_loss=mean_squared_error(y_test,y_pred_test)
        train_losses.append(train_loss)
        test_losses.append(test_loss)

        
        

        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Train Loss: {train_loss:.4f}, Test Loss: {test_loss:.4f}")
    
    return mlp, train_losses, test_losses

def train():

    x, y = get_dataset()

    x=np.array(x)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    # define network architecture
    architectures = [
        ((1000,500,100,100), 'relu',0.01)
    ]



    for arc in architectures:
        # train the Neural Networks using mlp_train
        mlp,train_losses,test_losses=train_mlp(x_train,y_train,x_test,y_test,arc[0],arc[1],0.01,1000,arc[2])
        plot_losses(train_losses, test_losses)
        pickle.dump(mlp, open("MLP_object", 'wb'))

#train()
# y_pred = mlp.predict([[96,45,29.42627467]])
# print(y_pred)
