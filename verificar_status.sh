#!/bin/bash

echo "Checking the status of the 'gerenciador-tarefas' container..."

# Verifica se o container está na lista de ativos (Up)
if [ "$(docker ps -q -f name=gerenciador-tarefas)" ]; then
    echo "Excellent! The container is UP and running perfectly."
    docker ps -f name=gerenciador-tarefas
else
    echo "Warning: Container is DOWN or does not exist. Starting up now..."
    
    # Se ele existir mas estiver apenas parado, remove para evitar conflitos de nome
    docker rm -f gerenciador-tarefas 2>/dev/null
    
    # Sobe o container de forma limpa e em background (-d) para liberar o terminal
    docker run -d --name gerenciador-tarefas -p 5000:5000 task-manager-app
    
    echo "Success! The container has been loaded and is running on http://127.0.0.1:5000"
fi
