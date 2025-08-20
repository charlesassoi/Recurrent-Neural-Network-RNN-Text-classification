#telechargement des librairies necessaires
import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
import matplotlib.pyplot as plt



#loading the IMDb datasets

dataset=tfds.load('imdb_reviews',as_supervised=True)

train_dataset,test_dataset=dataset["train"],dataset["test"]
print(train_dataset)