FROM python:3.8-slim

# We copy just the requirements.txt first to leverage Docker cache
WORKDIR /rosetta

RUN RUN apt-get update -y && \
    apt-get install -y build-essential && \
    pip install rosetta-cipher

# ENTRYPOINT [ "rosetta" ]

CMD ["rosetta-cipher", "--help"]
