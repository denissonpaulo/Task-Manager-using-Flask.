#!/bin/bash
echo "======= INICIANDO ANÁLISE ESTÁTICA COM BANDIT ======="
# Ativa o seu ambiente virtual para garantir o uso do python correto
source venv/bin/activate
# Instala o bandit se ele não estiver presente
pip install bandit -q
# Roda o Bandit na subpasta do projeto gerando um relatório em texto e salvando em output/
bandit -r todo_project/ -f txt -o output/sast_report.txt
cat output/sast_report.txt