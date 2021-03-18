# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# compile C with /usr/bin/cc
# compile CUDA with /usr/bin/nvcc
# compile CXX with /usr/bin/c++
C_FLAGS = -Wall -Wno-unused-result -Wno-unknown-pragmas -Wfatal-errors -Wno-deprecated-declarations -Wno-write-strings    -fopenmp

C_DEFINES = -DGPU -DUSE_CMAKE_LIBS

C_INCLUDES = -I/home/minhhieu/Desktop/Hieu/FIRFaceDetection/darknet/include -I/home/minhhieu/Desktop/Hieu/FIRFaceDetection/darknet/src -I/home/minhhieu/Desktop/Hieu/FIRFaceDetection/darknet/3rdparty/stb/include 

CUDA_FLAGS = -gencode arch=compute_75,code=sm_75 --compiler-options " -Wall -Wno-unused-result -Wno-unknown-pragmas -Wfatal-errors -Wno-deprecated-declarations -Wno-write-strings -DGPU -fPIC -fopenmp -Ofast "   

CUDA_DEFINES = -DGPU -DUSE_CMAKE_LIBS

CUDA_INCLUDES = -I/home/minhhieu/Desktop/Hieu/FIRFaceDetection/darknet/include -I/home/minhhieu/Desktop/Hieu/FIRFaceDetection/darknet/src -I/home/minhhieu/Desktop/Hieu/FIRFaceDetection/darknet/3rdparty/stb/include 

CXX_FLAGS = -Wall -Wno-unused-result -Wno-unknown-pragmas -Wfatal-errors -Wno-deprecated-declarations -Wno-write-strings    -fopenmp -std=gnu++11

CXX_DEFINES = -DGPU -DUSE_CMAKE_LIBS

CXX_INCLUDES = -I/home/minhhieu/Desktop/Hieu/FIRFaceDetection/darknet/include -I/home/minhhieu/Desktop/Hieu/FIRFaceDetection/darknet/src -I/home/minhhieu/Desktop/Hieu/FIRFaceDetection/darknet/3rdparty/stb/include 

