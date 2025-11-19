FROM fluent/fluentd:v1.16-debian

USER root

RUN gem install faraday -v "~> 1.10" --no-document \
 && gem install elasticsearch-transport -v "~> 7.17" --no-document \
 && gem install elasticsearch -v "~> 7.17" --no-document \
 && gem install fluent-plugin-elasticsearch -v 5.1.1 --no-document

USER fluent
