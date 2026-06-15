# 1. Usa uma imagem leve oficial do Python
FROM python:3.11-slim

# 2. Define o diretório de trabalho dentro do container
WORKDIR /app

# 3. Copia o arquivo de dependências e instala as bibliotecas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copia todo o código do projeto para dentro do container
COPY . .

# 5. Expõe a porta padrão que o Flask vai escutar
EXPOSE 5000

# 6. Comando para rodar a aplicação simulando o ambiente correto
CMD ["python", "todo_project/run.py"]