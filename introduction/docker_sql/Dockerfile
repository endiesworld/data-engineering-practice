# Use the official PostgreSQL image as the base image
FROM postgres:16

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=root
ENV POSTGRES_DB=ny_taxi

# Expose the PostgreSQL default port
EXPOSE 5432

# Define a named volume for PostgreSQL data
VOLUME ny_taxi_postgres_data /var/lib/postgresql/data

# Command to run when the container starts
CMD ["postgres"]
