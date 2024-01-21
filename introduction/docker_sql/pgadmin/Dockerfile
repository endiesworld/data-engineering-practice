# Use the official pgAdmin 4 image as the base image
FROM dpage/pgadmin4:latest

# Set environment variables for pgAdmin
ENV PGADMIN_DEFAULT_EMAIL=admin@admin.com
ENV PGADMIN_DEFAULT_PASSWORD=root

# Expose the pgAdmin default port
EXPOSE 80

# Command to run when the container starts
CMD ["/entrypoint.sh"]
