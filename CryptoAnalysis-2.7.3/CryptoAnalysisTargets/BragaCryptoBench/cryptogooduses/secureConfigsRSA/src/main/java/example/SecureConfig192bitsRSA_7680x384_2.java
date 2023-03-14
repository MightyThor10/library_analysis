package example;

import javax.crypto.*;
import java.security.*;
import org.bouncycastle.jce.provider.*;

public final class SecureConfig192bitsRSA_7680x384_2 {

	public static void main(String args[])
			throws NoSuchAlgorithmException, NoSuchPaddingException, InvalidKeyException, BadPaddingException,
			IllegalBlockSizeException, NoSuchProviderException, InvalidAlgorithmParameterException {

		Security.addProvider(new BouncyCastleProvider());

		int ksize = 7680;
		int hsize = 384;
		int maxLenBytes = (ksize - 2 * hsize) / 8 - 2;

		KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA", "BC");
		kpg.initialize(ksize);
		KeyPair kp = kpg.generateKeyPair();

		Cipher c = Cipher.getInstance("RSA/None/OAEPwithSHA384andMGF1Padding", "BC");

		Key pubk = kp.getPublic();
		c.init(Cipher.ENCRYPT_MODE, pubk);
		byte[] pt1 = "demo text".substring(0, maxLenBytes).getBytes();
		byte[] ct = c.doFinal(pt1);

		Key privk = kp.getPrivate();
		c.init(Cipher.DECRYPT_MODE, privk);
		byte[] pt2 = c.doFinal(ct);

	}
}
