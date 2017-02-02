1. First build the container. This must be done the first time or in case that you modify the data.yml

``` docker build -t oauthv1_app . ```

2. Once it is built, execute the app

``` docker run --rm oauthv1_app ```
