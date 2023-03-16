In com.connectsdk.service.webos.WebOSTVServiceSocketClient.java, the trust manager does not properly check if the client is trusted, essentially bypassing the check and leaving the function blank. The piece of the code is as follows:

```java 
public class TrustManager implements X509TrustManager {
        X509Certificate expectedCert;
        X509Certificate lastCheckedCert;

        @Override // javax.net.ssl.X509TrustManager
        public void checkClientTrusted(X509Certificate[] x509CertificateArr, String str) throws CertificateException {
        }

        TrustManager() {
        }

        public void setExpectedCertificate(X509Certificate x509Certificate) {
            this.expectedCert = x509Certificate;
        }

        public X509Certificate getLastCheckedCertificate() {
            return this.lastCheckedCert;
        }

        @Override // javax.net.ssl.X509TrustManager
        public void checkServerTrusted(X509Certificate[] x509CertificateArr, String str) throws CertificateException {
            String str2 = Util.f1470T;
            StringBuilder sb = new StringBuilder();
            sb.append("Expecting device cert ");
            sb.append(this.expectedCert != null ? this.expectedCert.getSubjectDN() : "(any)");
            Log.d(str2, sb.toString());
            if (x509CertificateArr != null && x509CertificateArr.length > 0) {
                X509Certificate x509Certificate = x509CertificateArr[0];
                this.lastCheckedCert = x509Certificate;
                if (this.expectedCert != null) {
                    byte[] encoded = x509Certificate.getEncoded();
                    byte[] encoded2 = this.expectedCert.getEncoded();
                    String str3 = Util.f1470T;
                    Log.d(str3, "Device presented cert " + x509Certificate.getSubjectDN());
                    if (!Arrays.equals(encoded, encoded2)) {
                        throw new CertificateException("certificate does not match");
                    }
                    return;
                }
                return;
            }
            this.lastCheckedCert = null;
            throw new CertificateException("no server certificate");
        }

        @Override // javax.net.ssl.X509TrustManager
        public X509Certificate[] getAcceptedIssuers() {
            return new X509Certificate[0];
        }
    }
```