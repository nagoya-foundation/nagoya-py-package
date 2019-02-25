import setuptools
with open("README.md", "r") as fh:
   long_description = fh.read()
setuptools.setup(
   name='nagoya',
   version='0.0.1',
   author="Nagoya Foundation",
   author_email="nagoya@nagoya.com",
   description="The best python package in the world",
   long_description=long_description,
   long_description_content_type="text/markdown",
   url="https://github.com/nagoya-foundation/nagoya-py-package",
   packages=setuptools.find_packages(),
   install_requires=["required_packages"],
   classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
   ],
)
