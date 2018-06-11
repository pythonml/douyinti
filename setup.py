import setuptools
from distutils.core import setup
setup(
    name='douyinti',
    version='0.1',
    description='add douyin effect to text',
    author='Zhongqiang Shen',
    author_email='shenzhongqiang@msn.com',
    url='https://github.com/pythonml/douyinti',
    packages=setuptools.find_packages(),
    package_data={
        'douyinti': ['fonts/*.ttf'],
    },
    install_requires=['Pillow>=5.1.0', 'numpy==1.14.4'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'douyinti=douyinti:main'
        ],
    },
)
