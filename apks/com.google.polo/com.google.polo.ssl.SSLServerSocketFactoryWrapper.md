In com.google.polo.ssl.SSLServerSocketFactoryWrapper#31, SSLContext is instantiated with TLS which defaults to TLSv.1, which is vulnerable and not recommended to use.

```java
SSLContext sSLContext = SSLContext.getInstance("TLS");
 ```