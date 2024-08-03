#!/bin/bash

# Reload the systemd manager configuration
sudo systemctl daemon-reload

# Restart the Gunicorn service
sudo systemctl restart gunicorn

# Test the Nginx configuration
sudo nginx -t

# If the Nginx configuration test is successful, restart Nginx
if [ $? -eq 0 ]; then
    sudo systemctl restart nginx
else
    echo "Nginx configuration test failed. Not restarting Nginx."
    exit 1
fi
