from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='The analysis aims to predict health insurance costs using factors like age, gender, BMI, children number, smoking status, and region, essential for insurers to accurately price policies. The model's high R2 and low MAPE suggest its effectiveness in practical application, advising insurers to consider factors like smoking habits, BMI, and number of children in their pricing strategy and to account for regional variations.',
    author='Fabio Olivei',
    license='MIT',
)
