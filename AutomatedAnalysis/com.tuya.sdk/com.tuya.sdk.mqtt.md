In com.tuya.sdk.mqtt.TLSSocketFactory, either TLSv1.3 or TLSv1.2 is accepted, which we know TLSv1.2 are vulnerable to racoon attacks:

```java
public static String[] bdpdqbp(SSLSocket sSLSocket) {
        String[] supportedProtocols = sSLSocket.getSupportedProtocols();
        if (supportedProtocols != null && supportedProtocols.length != 0) {
            ArrayList arrayList = new ArrayList();
            for (String str : supportedProtocols) {
                C8114L.m38064d(com.tuya.smart.android.network.util.TLSSocketFactory.TAG, "support protocol: " + str);
                if ("TLSv1.3".equals(str) || "TLSv1.2".equals(str)) {
                    C8114L.m38064d(com.tuya.smart.android.network.util.TLSSocketFactory.TAG, "add " + str);
                    arrayList.add(str);
                }
            }

```