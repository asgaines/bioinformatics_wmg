FROM debian:bullseye

RUN apt update

RUN apt install -y \
    bowtie2 \
    samtools \
    python3-pip

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "sh", "pipeline.sh" ]
