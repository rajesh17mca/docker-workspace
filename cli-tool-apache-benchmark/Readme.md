## Apache Benchmark
Apache Benchmark (ab) is a simple, single-threaded, command-line tool for load testing and benchmarking HTTP web servers. It is designed to measure how many requests a server can handle and how quickly, by simulating traffic to a specified URL. 

- Performance Metrics: ab reports crucial metrics like requests per second (throughput), mean time per request, total time for the test, and the number of failed requests.
- Simple Load Simulation: It can send a specified number of requests (-n) with a set level of concurrency (-c), simulating multiple users accessing a site simultaneously.
- Versatility: Although part of the Apache HTTP Server project, it can test any web server that supports HTTP/1.0 or HTTP/1.1 protocols.
- Identifying Bottlenecks: The results can help identify if performance degradation is due to server configuration, network constraints, or slow application code. 

More Information: https://httpd.apache.org/docs/2.4/programs/ab.html

Basic Usage:
```
ab -n 1000 -c 10 http://www.google.com/
```

docker build -t ab-rajesh .