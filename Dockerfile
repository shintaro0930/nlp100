ARG nvidia_cuda_version=11.4.0-cudnn8-devel-ubuntu20.04

FROM nvidia/cuda:${nvidia_cuda_version}

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get install -y git && \
    apt-get install -y tree && \
    apt-get install -y wget && \
    apt install unzip

RUN pip3 install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html

RUN pip3 install gdown && \
    pip3 install gensim && \
    pip3 install matplotlib && \
    pip3 install scikit-learn && \ 
    pip3 install numpy && \
    pip3 install Cython && \
    pip3 install bhtsne