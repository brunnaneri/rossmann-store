import pandas as pd
import numpy  as np

import math
import pickle
import datetime
import inflection


class Rossmann(object):
    def __init__(self):
        self_path = '/home/brunnaneri/repos/ds-em-producao/'
        self.competition_distance_scaler   = pickle.load(open(self_path + 'parameter/competition_distance_scaler.pkl', 'rb'))
        self.competition_time_month_scaler = pickle.load(open(self_path + 'parameter/competition_time_month_scaler.pkl', 'rb'))
        self.promo_time_week_scaler        = pickle.load(open(self_path + 'parameter/promo_time_week_scaler.pkl', 'rb'))
        self.year_scaler                   = pickle.load(open(self_path + 'parameter/year_scaler.pkl', 'rb'))
        self.store_type_encoding           = pickle.load(open(self_path + 'parameter/store_type_encoding.pkl', 'rb'))
        
    def data_cleaning(self,df1):
        old_columns = ['Store', 'DayOfWeek', 'Date', 'Open', 'Promo','StateHoliday', 'SchoolHoliday', 'StoreType', 'Assortment','CompetitionDistance', 'CompetitionOpenSinceMonth','CompetitionOpenSinceYear', 'Promo2', 'Promo2SinceWeek', 'Promo2SinceYear', 'PromoInterval']
        snake_case = lambda x : inflection.underscore(x)
        new_columns = list(map(snake_case,old_columns))
        #Rename Columns
        df1.columns = new_columns
        
        ## 1.3 Data Types
        #date to datetime
        df1['date'] = pd.to_datetime(df1['date'])
        
        ## 1.5 Fillout NA
        #competition_distance   
        df1['competition_distance'] = df1['competition_distance'].apply(lambda x: 200000 if math.isnan(x) else x)
        
        #competition_open_since_month    
        df1['competition_open_since_month'] = df1.apply(lambda x : x['date'].month if math.isnan(x['competition_open_since_month']) else x['competition_open_since_month'],axis=1)
        
        #competition_open_since_year     
        df1['competition_open_since_year'] = df1.apply(lambda x : x['date'].year if math.isnan(x['competition_open_since_year']) else x['competition_open_since_year'],axis=1)             
        
        #promo2_since_week    
        df1['promo2_since_week'] = df1.apply(lambda x : x['date'].week if math.isnan(x['promo2_since_week']) else x['promo2_since_week'],axis=1)
        
        #promo2_since_year               
        df1['promo2_since_year'] = df1.apply(lambda x : x['date'].year if math.isnan(x['promo2_since_year']) else x['promo2_since_year'],axis=1)
        
        #promo_interval                  
        df1['promo_interval'].fillna(0,inplace=True)     
                  
        dic_month = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sept',10:'Oct',11:'Nov',12:'Dec'}
        df1['month_of_date'] = df1['date'].dt.month.map(dic_month)
        df1['is_promo2'] = df1[['promo_interval','month_of_date']].apply(lambda x : 0 if x['promo_interval'] == 0 else 1 if x['month_of_date'] in x['promo_interval'].split(',') else 0, axis =1)
        
        ## 1.6 Change Types
        df1['competition_open_since_month'] = df1['competition_open_since_month'].astype(int)
        df1['competition_open_since_year'] = df1['competition_open_since_year'].astype(int)
        df1['promo2_since_week'] = df1['promo2_since_week'].astype(int)
        df1['promo2_since_year'] = df1['promo2_since_year'].astype(int)
        
        return df1
    
    def feature_engineering(self, df2):
        #year
        df2['year']=df2['date'].dt.year
        
        #month
        df2['month']=df2['date'].dt.month
        
        #week
        df2['day']=df2['date'].dt.day
        
        #week of year
        df2['week_of_year'] = df2['date'].dt.isocalendar().week
        
        #year week
        df2['year_week'] = df2['date'].apply(lambda x: x.strftime('%Y-%W'))
        
        #competition since (unidade: mês)
        df2['competition_since'] = df2['competition_open_since_year'].astype(str) + '-'+ df2['competition_open_since_month'].astype(str)+'-1'
        df2['competition_since'] = df2['competition_since'].apply(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d') )
        df2['competition_time_month'] = ((df2['date']-df2['competition_since'])/30).apply(lambda x: x.days).astype(int)
        
        ##promo since
        df2['promo2_since'] = df2['promo2_since_year'].astype(str) + '-'+ df2['promo2_since_week'].astype(str)+'-1'
        df2['promo2_since'] = (df2['promo2_since'].apply(lambda x: datetime.datetime.strptime(x,'%Y-%W-%w'))) - datetime.timedelta(days=7)
        df2['promo2_time_week'] = ((df2['date']-df2['promo2_since'])/7).apply(lambda x: x.days).astype(int)
        
        #assortment
        df2['assortment'] = df2['assortment'].apply(lambda x: 'basic' if x == 'a' else 'extra' if x =='b' else 'extended')
        
        #state holiday
        
        df2['state_holiday'] = df2['state_holiday'].apply(lambda x:'public_holiday' if x=='a' else 
                                                          'easter_holiday' if x=='b' else 'christmas' if x=='c' else 'regular_day')
        #Filtragem das linhas
        df2 = df2[(df2['open']!=0)]
        
        #Seleção das colunas
        cols_drop = ['open','month_of_date','promo_interval']
        df2 = df2.drop(cols_drop,axis=1)
        
        return df2
    
    def data_preparation(self,df5):
        
        #competition_distance - bastante outlier
        df5['competition_distance'] = self.competition_distance_scaler.transform(df5[['competition_distance']])
        
        #competition_time_month - bastante outlier
        df5['competition_time_month'] = self.competition_time_month_scaler.transform(df5[['competition_time_month']])
        
        #promo_time_week 
        df5['promo2_time_week'] = self.promo_time_week_scaler.transform(df5[['promo2_time_week']])
        
        #year
        df5['year'] = self.year_scaler.transform(df5[['year']])
        
        ## 5.2 - Encoding
        
        #state_holiday
        df5 = pd.get_dummies(df5, prefix='state_holiday',columns=['state_holiday'])
        
        #store_type
        df5['store_type'] = self.store_type_encoding.transform(df5[['store_type']])
        
        #assortment
        dic =  {'basic': 1,'extended':2, 'extra':3}
        df5['assortment'] = df5['assortment'].map(dic)
        
        ## 5.3 - Transformação
        
        ### 5.3.1 - Transformação de Grandeza
        
        # df5['sales'] = np.log1p(df5['sales'])
        
        ### 5.3.2 - Transformações de Natureza
        
        #day_of_week
        df5['day_of_week_sen'] = df5['day_of_week'].apply(lambda x: np.sin(x*(np.pi/7)))
        df5['day_of_week_cos'] = df5['day_of_week'].apply(lambda x: np.cos(x*(np.pi/7)))
        
        #month
        df5['month_sen'] = df5['month'].apply(lambda x: np.sin(x*(np.pi/12)))
        df5['month_cos'] = df5['month'].apply(lambda x: np.cos(x*(np.pi/12)))
        
        #day
        df5['day_sin'] = df5['day'].apply(lambda x: np.sin(x*(np.pi/30)))
        df5['day_cos'] = df5['day'].apply(lambda x: np.cos(x*(np.pi/30)))
        
        #week_of_year
        df5['week_of_year_sin'] = df5['week_of_year'].apply(lambda x: np.sin(x *(np.pi/52)))
        df5['week_of_year_cos'] = df5['week_of_year'].apply(lambda x: np.cos(x *(np.pi/52)))

        #colunas selecionadas
        cols_selected = ['store','promo','store_type','assortment','competition_distance','competition_open_since_month','competition_open_since_year',
                                'promo2','promo2_since_week','promo2_since_year','competition_time_month','promo2_time_week','day_of_week_sen','day_of_week_cos',
                                'day_sin','day_cos','week_of_year_sin','week_of_year_cos']

        return df5[cols_selected]
    
    def get_prediction(self,model,data_original,data_prepared):
        
        prediction = model.predict(data_prepared)
        data_original['prediction'] = np.expm1(prediction)

        return data_original.to_json(orient='records', date_format='iso')
