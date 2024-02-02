from setuptools import find_packages, setup

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)




setup(
    name="Credit_Card_Default_Prediction",
    version='0.0.1',
    author='Naveen Chaudhary',
    author_email='naveen14062001@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)


 # logging.info("Entered the train pipeline")

    # obj=DataIngestion()
    # raw_data_path=obj.initiate_data_ingestion('data')

    # DataCleaning_obj=DataCleaning()
    # train_data_path,test_data_path=DataCleaning_obj.DataCleaningConfig(raw_data_path)

    # data_transformation=DataTransformation()
    # train_arr,test_arr=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    # model_trainer_obj=ModelTrainer()
    # print(model_trainer_obj.initiate_model_trainer(train_arr,test_arr))

    # base_model = base_model()
    # print(base_model)