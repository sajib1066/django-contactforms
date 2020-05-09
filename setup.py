import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='django-contactforms',  
     version='2.0',
     scripts=['django-contactforms'] ,
     author="Sajib Hossain",
     author_email="sajib1066@gmail.com",
     description="Django Contact Form Package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/sajib1066/django-contactforms",
     packages=setuptools.find_packages(),
     classifiers=[
         "Framework :: Django",
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )