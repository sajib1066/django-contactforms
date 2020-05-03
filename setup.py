import setuptools
with open("README.rst", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='django-contacts-us',  
     version='0.1',
     scripts=['django-contacts-us'] ,
     author="Sajib Hossain",
     author_email="sajib1066@gmail.com",
     description="Django Contact Us Form Package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/sajib1066/django-contacts-us",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )