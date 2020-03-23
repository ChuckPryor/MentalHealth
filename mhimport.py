import numpy as np
import pandas as pd 
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import math, random, pickle, itertools,scipy
from sklearn.linear_model import LinearRegression, Ridge, Lasso, LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, KFold 
from statistics import mean 
from IPython.display import display, HTML
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import PolynomialFeatures, StandardScaler, OneHotEncoder
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier
from sklearn.datasets.samples_generator import make_blobs
from sklearn.svm import SVC
import statsmodels.api as sm
