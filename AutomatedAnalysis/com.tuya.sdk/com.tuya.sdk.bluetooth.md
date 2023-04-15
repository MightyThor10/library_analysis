In com.tuya.sdk.bluetooth.AES.java and com.tuya.sdk.bluetooth.BLEUtil.java, I found:
```java
aESUtil.setALGO("AES/" + ((char) ("AES/GCM/NoPadding".charAt(4) - 2)) + "AES/GCM/NoPadding".charAt(5) + ((char) ("AES/GCM/NoPadding".charAt(6) - 11)) + "/NoPadding");
```
The above statement consists of several String operations, which can be broken down to the following:

```java
System.out.println(((char) ("AES/GCM/NoPadding".charAt(4) - 2))); // "G" - 2- -> outputs "E"
System.out.println("AES/GCM/NoPadding".charAt(5)); //outputs "C"
System.out.println(((char) ("AES/GCM/NoPadding".charAt(6) - 11))); // "M" - 11 --> outputs "B"
```
Thus forming the Substring `ECB`.

This is insecure, as this snippet equates to `aESUtil.setALGO("AES/ECB/NoPadding);`.

The Cipher using `AES/ECB/PKCS5Padding` is possibly used for decrypting Media Transfer Protocol data in (com.tuya.sdk.blelib.receiver.listener.AbsBluetoothListener.java).