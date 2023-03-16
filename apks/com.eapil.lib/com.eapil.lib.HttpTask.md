### 1:


In com.eapil.lib.HttpTask under the HttpTask class, the trustAllHosts function attempts to bypass checks for trusted clients and servers. It references xtmArray which itself references xtmArray.java which is an insecure implementation of a trust manager that does nothing for checking trusted servers and clients. 

The code in com.eapil.lib.HttpTask:

```java
    private static void trustAllHosts() {
        try {
            SSLContext sSLContext = SSLContext.getInstance("TLS");
            sSLContext.init(null, xtmArray, new SecureRandom());
            HttpsURLConnection.setDefaultSSLSocketFactory(sSLContext.getSocketFactory());
        } catch (Exception unused) {
        }
    }
```

The xtmArray is defined at the beginning of the main class in the java file as:

```java
    static TrustManager[] xtmArray = {new MytmArray()};
```


The code inside MytmArray is as follows, which evidently does nothing to certify and check servers and clients:

```java
package com.eapil.lib;

import java.security.cert.CertificateException;
import java.security.cert.X509Certificate;
import javax.net.ssl.X509TrustManager;

/* compiled from: HttpUtils.java */
/* loaded from: classes.dex */
class MytmArray implements X509TrustManager {
    @Override // javax.net.ssl.X509TrustManager
    public void checkClientTrusted(X509Certificate[] x509CertificateArr, String str) throws CertificateException {
    }

    @Override // javax.net.ssl.X509TrustManager
    public void checkServerTrusted(X509Certificate[] x509CertificateArr, String str) throws CertificateException {
    }

    @Override // javax.net.ssl.X509TrustManager
    public X509Certificate[] getAcceptedIssuers() {
        return new X509Certificate[0];
    }
}
```




### 2:

 In the same file, com.eapil.lib.HttpTask, an insecure implementation of hostnameverifier also exists which explicitly names the hostnameverifier object as DO_NOT_VERIFY and returns true for the verifying every hostname:

 ```java
     static HostnameVerifier DO_NOT_VERIFY = new HostnameVerifier() { // from class: com.eapil.lib.HttpTask.1
        @Override // javax.net.ssl.HostnameVerifier
        public boolean verify(String str, SSLSession sSLSession) {
            return true;
        }
    };
```