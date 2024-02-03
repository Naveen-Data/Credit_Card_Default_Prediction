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


