docker build -t trendline_image .
docker run -d --name trendline_container -p 8000:8000 trendline_image
