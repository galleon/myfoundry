cmake_minimum_required(VERSION 2.8)

project (test)
#MACOSX_RPATH

add_library(testlib SHARED src/testlib.c)

#set(INSTALL_LIB_DIR lib)

install(TARGETS testlib LIBRARY DESTINATION ${INSTALL_LIB_DIR})
