# RUN THIS APP:
1. Open the root directory of this application
2. Run command: \
    docker compose up -d
3. Follow link for use FastAPI with Swagger UI: \
    http://localhost/docs 
4. Or connect to mysql server from within container with next command: \
    docker exec -it mysqlserver mysql -uroot -ppassword
5. Stop application with next command (if you are in root directory): \
    docker compose down