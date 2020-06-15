import functools
import numpy as np 
import tensorflow as tf 
# load data
train_path = "C:/Users/asus/Documents/Learning Machine Learning"
test_path = "C:/Users/asus/Documents/Learning Machine Learning"
train_data = tf.keras.utils.get_file('train.csv',train_path)
test_data = tf.keras.utils.get_file('eval.csv',test_path)