import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name='robotics_sympy',    # This is the name of your PyPI-package.
    version='1.0.0',
    url='https://github.com/ryanGT/robotics_sympy',
    author='Ryan Krauss',
    author_email='ryanwkrauss@gmail.com',
    description="package for symbolic robot kinematics analysis using sympy",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
