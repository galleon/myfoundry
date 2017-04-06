# Use a native library from Jupyter

This repository contains information on how to compile a native library to be used from Python.
The sources of the library are supposed to be in src/


## Use Docker for development

My runtime environment being a CentOS machine but developping on a Mac, I will use a [Docker](https://www.docker.com/)  container to 
compile my code. I have therefore created a Dockerfile containing a minimum development environment.

I use the following command to create the container:
* docker build --tag centos-6.8-dev .

and run the compilation of my library using:
* docker run -t -i -v $(pwd):/home/shared centos-6.8-dev /bin/bash -c /home/shared/compile.sh 


I will zip my runtime environment in order to tranfer it easily to my runtime platform
* zip -r mytk.zip lib/


To add a bit a fun I am assuming that I can only tranfer csv file on my runtime machine. Dont be afraid, I use a small script to generate a csv out of my zip file
* zip2csv.py mytk.zip


Let's now install and run Jupyter
* conda create --name foundry python=2.7 jupyter numpy
* source activate foundry
* jupyter notebook

In which we will open the `Test.ipynb` notebook that will decode the csv and use the native library:
* open the Test notebook


Have fun!
