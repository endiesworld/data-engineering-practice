FROM python:3.9

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app

# Copy the Python script and the shell script into the container
COPY ingest_data.py run_data_ingest_script.sh /app/

# Make the shell script executable
RUN chmod +x run_data_ingest_script.sh

# ENTRYPOINT ["bash"]
# ENTRYPOINT [ "python", "ingest.py" ]

# Define the default command to run when the container starts
CMD ["./run_data_ingest_script.sh"]