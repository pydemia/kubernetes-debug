FROM --platform=amd64 adoptopenjdk/openjdk11:alpine-jre

ENV HOST=0.0.0.0
ENV PORT=8000
ENV DEBUG_PORT=5678

# Refer to Maven build -> finalName
ARG JAR_PATH=./spring-boot-2-rest-service-with-swagger/target
ARG JAR_FILE=spring-boot-2-rest-service-swagger-0.0.1-SNAPSHOT.jar

# cd /workdir
WORKDIR /workdir

# cp target/spring-boot-web.jar /opt/app/app.jar
COPY ${JAR_PATH}/${JAR_FILE} app.jar

# ENTRYPOINT ["java","-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=${DEBUG_PORT},quiet=y", "-jar", "-Dserver.port=${PORT}" "app.jar"]
ENTRYPOINT java -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=${DEBUG_PORT},quiet=y -jar -Dserver.port=${PORT} app.jar
