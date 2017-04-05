FROM centos:6.8
RUN yum --assumeyes install gcc gcc-c++ make cmake && yum -y clean all
