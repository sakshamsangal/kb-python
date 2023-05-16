# RSA Algorithm

## Code

``` java
import java.math.BigInteger;
import java.security.SecureRandom;

public class RSA {

    // this is e parameter after calculations
    private BigInteger publicKey;

    // this is d parameter after calculations
    private BigInteger privetKey;

    // this is n = p * q
    private BigInteger n;

    // we need random number generator
    private SecureRandom secureRandom;

    public RSA() {
        secureRandom = new SecureRandom();
    }

    public BigInteger encryptText(String message) {
        return encrypt(publicKey, n, message);
    }

    public String decryptText(BigInteger cipherText) {
        return decrypt(privetKey, n, cipherText);
    }

    private String decrypt(BigInteger d, BigInteger n, BigInteger cipherText) {

        // we use modular exponentiation in decryption as well
        // cipher^d mod n
        BigInteger messageInt = cipherText.modPow(d, n);

        // we want to end up with string
        return new String(messageInt.toByteArray());
    }


    // cipher text is huge integer
    private BigInteger encrypt(BigInteger e, BigInteger n, String message) {

        // first we transform original message into array of bytes
        byte[] messageBytes = message.getBytes();

        // we want to convert this messageBytes into huge integer
        // because we want to do modular exponentiation
        BigInteger messageInt = new BigInteger(messageBytes);

        // we have to use modular exponentiation message^e mod n
        return messageInt.modPow(e, n);

    }

    public void generateKeys(int keyDigits) {

        // p is large prime number
        BigInteger p = BigInteger.probablePrime(keyDigits, secureRandom);

        // q is large prime number
        BigInteger q = BigInteger.probablePrime(keyDigits, secureRandom);

        // n = p * q this is trap door function
        n = p.multiply(q);

        // Euler's totient phi function
        BigInteger phi = (p.subtract(BigInteger.ONE)).multiply(q.subtract(BigInteger.ONE));

        // 0 < e < phi is co-prime to phi so gcd(e, phi) = 1
        BigInteger e = generatePublicFactor(phi);

        publicKey = e;

        // d is modular inverse of e (with mod phi)
        BigInteger d = e.modInverse(phi);

        privetKey = d;
    }

    private BigInteger generatePublicFactor(BigInteger phi) {

        BigInteger e = new BigInteger(phi.bitLength(), secureRandom);

        // we are in search of co-prime of e and phi (gcd(e, phi) = 1)
        while (!e.gcd(phi).equals(BigInteger.ONE)) {
            e = new BigInteger(phi.bitLength(), secureRandom);
        }

        return e;
    }

}


class App {
    public static void main(String[] args) {

        RSA rsa = new RSA();

        rsa.generateKeys(1024);

        String text = "Saksham Sangal";

        BigInteger cipherText = rsa.encryptText(text);

        System.out.println("Cipher text = " + cipherText);

        String plainText = rsa.decryptText(cipherText);

        System.out.println("Plain text = " + plainText);


    }
}
```

## Output

```
Cipher text = 16019983055019732776452430753234979314823561297004446928082954176273144791665895294272346956620296112688119686023149949103390709500964460695279209800867728958696459479772734669216126750050665904099231930732713341749600342489810832931038012512897260739864966412118256603480561186848893897513818772744922249935994893645421511355356061655165256044838598371921078763728033718098476555230710250370997550510246602735083631816831494451151146698192785184196618038285950335783311665811138660762311482079760140691239713352902800241382347510277272782971921568426358506303083942271282167344719409439581993132991473350678808990789
Plain text = Saksham Sangal
```