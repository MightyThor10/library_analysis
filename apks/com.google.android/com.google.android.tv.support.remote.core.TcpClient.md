In com.google.android.tv.support.remote.core.TcpClient#480, the SSLContext is instantiate using a variable "TLS" which is defaulted to TLSv.1 which is vulnerable and recommended to not use.

```java
    SSLContext sSLContext = SSLContext.getInstance(SSLSocketFactory.TLS);
```