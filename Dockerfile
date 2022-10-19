FROM python:3.7-slim
WORKDIR ./Python_Package_Modules_Concepts
COPY ./requirement.txt ./requirement.txt
RUN pip install -r ../Python_Package_Modules_Concepts/requirement.txt
COPY ./Python_Package_Modules_Concepts ./Python_Package_Modules_Concepts
EXPOSE 5000
