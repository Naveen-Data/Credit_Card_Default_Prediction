# import sys
# import pandas as pd
# from src.exception import CustomException
# from src.utils import load_object


# class PredictPipeline:
#     def __init__(self):
#         pass

#     def predict(self,features):
#         try:
#             model_path=os.path.join("artifacts","model.pkl")
#             preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
#             print("Before Loading")
#             model=load_object(file_path=model_path)
#             preprocessor=load_object(file_path=preprocessor_path)
#             print("After Loading")
#             data_scaled=preprocessor.transform(features)
#             preds=model.predict(data_scaled)
#             return preds
        
#         except Exception as e:
#             raise CustomException(e,sys)



# class CustomData:
#     def __init__(  self,
#         gender: str,
#         race_ethnicity: str,
#         parental_level_of_education,
#         lunch: str,
#         test_preparation_course: str,
#         reading_score: int,
#         writing_score: int):

#         self.gender = gender

#         self.race_ethnicity = race_ethnicity

#         self.parental_level_of_education = parental_level_of_education

#         self.lunch = lunch

#         self.test_preparation_course = test_preparation_course

#         self.reading_score = reading_score

#         self.writing_score = writing_score

#     def get_data_as_data_frame(self):
#         try:
#             custom_data_input_dict = {
#                 "gender": [self.gender],
#                 "race_ethnicity": [self.race_ethnicity],
#                 "parental_level_of_education": [self.parental_level_of_education],
#                 "lunch": [self.lunch],
#                 "test_preparation_course": [self.test_preparation_course],
#                 "reading_score": [self.reading_score],
#                 "writing_score": [self.writing_score],
#             }

#             return pd.DataFrame(custom_data_input_dict)

#         except Exception as e:
#             raise CustomException(e, sys)
# import os
# import sys
# import pandas as pd
# from src.DiamondPricePrediction.exception import customexception
# from src.DiamondPricePrediction.logger import logging
# from src.DiamondPricePrediction.utils.utils import load_object


# class PredictPipeline:
#     def __init__(self):
#         pass
    
#     def predict(self,features):
#         try:
#             preprocessor_path=os.path.join("Artifacts","preprocessor.pkl")
#             model_path=os.path.join("Artifacts","model.pkl")
            
#             preprocessor=load_object(preprocessor_path)
#             model=load_object(model_path)
            
#             scaled_data=preprocessor.transform(features)
            
#             pred=model.predict(scaled_data)
            
#             return pred
            
            
        
#         except Exception as e:
#             raise customexception(e,sys)
    
    
    
# class CustomData:
#     def __init__(self,
#                  carat:float,
#                  depth:float,
#                  table:float,
#                  x:float,
#                  y:float,
#                  z:float,
#                  cut:str,
#                  color:str,
#                  clarity:str):
        
#         self.carat=carat
#         self.depth=depth
#         self.table=table
#         self.x=x
#         self.y=y
#         self.z=z
#         self.cut = cut
#         self.color = color
#         self.clarity = clarity
            
                
#     def get_data_as_dataframe(self):
#             try:
#                 custom_data_input_dict = {
#                     'carat':[self.carat],
#                     'depth':[self.depth],
#                     'table':[self.table],
#                     'x':[self.x],
#                     'y':[self.y],
#                     'z':[self.z],
#                     'cut':[self.cut],
#                     'color':[self.color],
#                     'clarity':[self.clarity]
#                 }
#                 df = pd.DataFrame(custom_data_input_dict)
#                 logging.info('Dataframe Gathered')
#                 return df
#             except Exception as e:
#                 logging.info('Exception Occured in prediction pipeline')
#                 raise customexception(e,sys)