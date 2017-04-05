Use Docker to compile your Python toolbox

* docker build --tag centos-6.8-dev .
* docker run -t -i -v $(pwd):/home/shared centos-6.8-dev /bin/bash -c /home/shared/compile.sh 
* zip mytk.zip testlibwrapper.py lib
* zip2csv.py mytk.zip
* conda create --name foundry python=2.7 jupyter
* source activate foundry
* jupyter notebook
