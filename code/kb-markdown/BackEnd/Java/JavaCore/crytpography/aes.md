# AES (Advanced Encryption Standard)

## Code

``` java 
import java.security.NoSuchAlgorithmException;
import java.util.Base64;
import javax.crypto.*;

public class AdvancedEncryptionStandard {

    public String encrypt(String plainText, SecretKey key) {

        // the key is a 64 bits long sequence in AES
        // we are going to deal with byte arrays
        byte[] cipherText = null;

        try {

            // we use Advance Encryption Standard (AES)
            Cipher encryptionCipher = Cipher.getInstance("AES");

            // we use AES for encryption
            encryptionCipher.init(Cipher.ENCRYPT_MODE, key);

            // first convert the plaintext into bytes (ASCII value)
            byte[] bytes = plainText.getBytes();

            // this is when the encryption happens
            cipherText = encryptionCipher.doFinal(bytes);

            // we want to represent and encode the byte sequence as Base64 string
            cipherText = Base64.getEncoder().encode(cipherText);

            return new String(cipherText);

        } catch (Exception e) {
            e.printStackTrace();
        }

        return null;
    }

    public String decrypt(String cipherText, SecretKey key) {

        byte[] utfDecrypted = null;

        try {

            Cipher decryptionCipher = Cipher.getInstance("AES");

            decryptionCipher.init(Cipher.DECRYPT_MODE, key);

            // Base64 is an encoding to represent any byte sequence by a sequence of printable characters
            // we want to deal with bytes
            byte[] bytedDecrypted = Base64.getDecoder().decode(cipherText.getBytes());

            // this is where the decryption happens
            utfDecrypted = decryptionCipher.doFinal(bytedDecrypted);

            return new String(utfDecrypted, "UTF8");

        } catch (Exception e) {
            e.printStackTrace();
        }

        return null;
    }
}

class Main {

    public static void main(String[] args) throws NoSuchAlgorithmException {

        String plainText = "Saksham Sangal";

        // the private key is a 64 bits long sequence
        SecretKey key = KeyGenerator.getInstance("AES").generateKey();

        AdvancedEncryptionStandard aes = new AdvancedEncryptionStandard();

        String cipherText = aes.encrypt(plainText, key);

        System.out.println("Encrypted text: " + cipherText);

        System.out.println("Decrypted text: " + aes.decrypt(cipherText, key));
    }
}
```

## output

```
Encrypted text: EVJRi3UCRl+6FHN0XF9cNA==
Decrypted text: Saksham Sangal
```