
# Use official PHP image from Docker Hub
FROM php:8.0-apache

# Install PHP extensions (like mysqli for MySQL)
RUN docker-php-ext-install mysqli

# Set up Apache document root
COPY ./src/ /var/www/html/

# Expose port 80 to access the application
EXPOSE 80
