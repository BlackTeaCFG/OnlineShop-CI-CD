#!/bin/bash

echo "Generating self-signed certificates for OnlineShop..."
mkdir -p certificates
openssl req -x509 -newkey rsa:4096 -keyout certificates/key.pem -out certificates/cert.pem -days 365 -nodes -subj "/C=US/ST=State/L=City/O=OnlineShop/CN=onlineshop.example.com"
echo "Certificates generated successfully!"