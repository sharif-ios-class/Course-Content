import pandas as pd
import coremltools
from sklearn.linear_model import LinearRegression



train = pd.read_csv("D:/Fall97-98/ML/HW2/House_Price/train.csv", )
test = pd.read_csv("D:/Fall97-98/ML/HW2/House_Price/test.csv")

ntrain = train.shape[0]


train.drop("Id", axis = 1, inplace = True)



Y_train = train['SalePrice']



#all_data = pd.concat((train, test)).reset_index(drop=True)
train.drop(['SalePrice'], axis=1, inplace=True)




#missing variables
train.drop(['PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu', 'LotFrontage',
               'GarageCond', 'GarageType', 'GarageYrBlt', 'GarageFinish', 'GarageQual',
               'BsmtExposure', 'BsmtExposure', 'BsmtFinType1', 'BsmtCond', 'BsmtQual',
               'Electrical'], axis=1, inplace=True)


#Remove correlated variables
train.drop(['GarageCars', 'TotRmsAbvGrd'], axis=1, inplace=True)


#Removing variables that are not important
train.drop(['MasVnrArea', 'MasVnrType'], axis=1, inplace=True)



#Removing bsmt variables
train.drop(['BsmtFinType2'], axis=1, inplace=True)


#train Categorical variables
train.drop(['MSZoning', 'Street', 'LotShape', 'LandContour', 'Utilities', 'LotConfig',
               'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle',
               'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'ExterQual',
               'ExterCond', 'Foundation', 'BsmtFinSF2', 'Heating', 'HeatingQC', 'CentralAir', 'LowQualFinSF',
               'HalfBath', 'KitchenQual', 'Functional', 'PavedDrive', 'EnclosedPorch',
               '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal',
               'MoSold', 'YrSold', 'SaleType', 'SaleCondition', 'YearRemodAdd', 'KitchenAbvGr', 'BsmtHalfBath',
               'BsmtFullBath', 'WoodDeckSF', 'WoodDeckSF', 'BsmtUnfSF', 'BsmtFinSF1', 'MSSubClass', 'OverallCond',
               'OverallQual'], axis=1, inplace=True)

# Adding total sqfootage feature
train['TotalSF'] = train['TotalBsmtSF'] + train['1stFlrSF'] + train['2ndFlrSF']


My_Model = LinearRegression()
My_Model.fit(train, Y_train)
predicted = My_Model.predict(train)


coreml_model = coremltools.converters.sklearn.convert(My_Model, ["1stFlrSF", "2ndFlrSF", "BedroomAbvGr", "Fireplaces", "FullBath", "GarageArea", "GrLivArea",
            "LotArea", "OpenPorchSF", "TotalBsmtSF", "YearBuilt", "TotalSF"], "SalePrice")
coreml_model.save('HousePrediction.mlmodel')