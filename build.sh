#!/usr/bin/env bash
# Build script for Render deployment
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Creating staticfiles directory..."
mkdir -p staticfiles

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running migrations..."
python manage.py migrate

echo "Creating sample data..."
python manage.py create_sample_data || echo "Sample data creation failed or already exists"

echo "Build completed successfully!"
