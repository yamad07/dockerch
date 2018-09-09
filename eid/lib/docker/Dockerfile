FROM nvidia/cuda:8.0-runtime-ubuntu16.04

RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    sudo \
    git \
    bzip2 \
    libx11-6 \
 && rm -rf /var/lib/apt/lists/*

RUN mkdir /src
WORKDIR /src

RUN adduser --disabled-password --gecos '' --shell /bin/bash user \
 && chown -R user:user /src
RUN echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-user
USER user

ENV HOME=/home/user
RUN chmod 777 /home/user

RUN curl -so ~/miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-4.5.1-Linux-x86_64.sh \
 && chmod +x ~/miniconda.sh \
 && ~/miniconda.sh -b -p ~/miniconda \
 && rm ~/miniconda.sh
ENV PATH=/home/user/miniconda/bin:$PATH
ENV CONDA_AUTO_UPDATE_CONDA=false

RUN /home/user/miniconda/bin/conda install conda-build \
 && /home/user/miniconda/bin/conda create -y --name py36 python=3.6.5 \
 && /home/user/miniconda/bin/conda clean -ya
ENV CONDA_DEFAULT_ENV=py36
ENV CONDA_PREFIX=/home/user/miniconda/envs/$CONDA_DEFAULT_ENV
ENV PATH=$CONDA_PREFIX/bin:$PATH

RUN conda install -y -c pytorch \
    cuda80=1.0 \
    magma-cuda80=2.3.0 \
    "pytorch=0.4.1=py36_cuda8.0.61_cudnn7.1.2_1" \
    torchvision=0.2.1 \
 && conda clean -ya

RUN conda install -y h5py=2.8.0 \
 && conda clean -ya
RUN pip install h5py-cache==1.0

RUN pip install torchnet==0.0.4

RUN conda install -y requests=2.19.1 \
 && conda clean -ya

RUN conda install -y graphviz=2.38.0 \
 && conda clean -ya
RUN pip install graphviz==0.8.4

RUN sudo apt-get update && sudo apt-get install -y --no-install-recommends \
    libgtk2.0-0 \
    libcanberra-gtk-module \
    python-opengl \
 && sudo rm -rf /var/lib/apt/lists/*
RUN conda install -y -c menpo opencv3=3.1.0 \
 && conda clean -ya

COPY ./requirements.txt .
RUN pip install -r requirements.txt
