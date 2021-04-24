FROM continuumio/miniconda3

WORKDIR /home/biolib

RUN conda install -c bioconda --yes anarci scikit-learn pandas numpy \
    && \
    conda clean -afy

RUN wget https://www.dropbox.com/s/4sdu3b3u83voldy/finalized_model.sav

COPY . .

ENTRYPOINT [ "python", "src/predict.py" ]

