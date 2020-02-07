# Dockerfile for Group 409: Bike Sharing Machine Learning Model
# Aman Kumar Garg, Victor Cuspinera-Contreras, Yingping Qian
# February 6, 2020
# 
# This dockerfile contains the programs requiered to run the driver
# script for the project that return the explanatory data analysis and
# fit machine learning models for bike sharing dataset.
#

# initialize the dockerfile
FROM rocker/tidyverse
#RUN apt-get update -qq && apt-get -y --no-install-recommends install \
#  && install2.r --error \
#    --deps TRUE \
#    knitr \
#    caret \
#    kableExtra
RUN R -e "install.packages(c('knitr', 'caret', 'kableExtra'), \
                           dependencies=TRUE, \
                           repos='https://cran.microsoft.com/snapshot/2019-10-19/')"

# install the anaconda distribution of python
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy && \
    /opt/conda/bin/conda update -n base -c defaults conda

# install docopt python package
RUN /opt/conda/bin/conda install -y -c anaconda docopt \
                                        selenium \
                                        altair

# install scikit-learn version 0.22                                        
RUN /opt/conda/bin/pip install scikit-learn==0.22

# install chrome                                        
RUN apt-get update && apt install -y chromium && apt-get install -y libnss3 && apt-get install unzip
# Install chromedriver
RUN wget -q "https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && rm /tmp/chromedriver.zip && chown root:root /usr/bin/chromedriver && chmod +x /usr/bin/chromedriver
    
# install vega-datasets
RUN /opt/conda/bin/conda install -y vega_datasets

# put anaconda python in path
ENV PATH="/opt/conda/bin:${PATH}"
ENV PATH="/usr/bin/chromedriver:${PATH}"
CMD ["/bin/bash"]
