FROM debian:latest
RUN apt-get update && apt-get install python3-pip -y && pip3 install requests==2.27.1 && pip3 install passlib==1.7.4
ADD projet2_test_authentication.py /test/projet2_test_authentication.py
ADD projet2_test_rating.py /test/projet2_test_rating.py
ADD projet2_test_performances.py /test/projet2_test_performances.py
WORKDIR /test/
EXPOSE 8000
ENV LOG 1
CMD python3 projet2_test_authentication.py && python3 projet2_test_rating.py && python3 projet2_test_performances.py
#CMD python3 projet2_test_rating.py
#CMD python3 projet2_test_performances.py

