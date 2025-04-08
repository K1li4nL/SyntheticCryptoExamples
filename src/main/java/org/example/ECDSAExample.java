package org.example;
import java.security.*;
import java.security.spec.ECGenParameterSpec;
import java.util.Base64;

public class ECDSAExample {

    public static void main(String[] args) throws Exception {
        // Generate ECDSA key pair using SECP256R1 curve
        KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("EC");
        ECGenParameterSpec ecSpec = new ECGenParameterSpec("secp256r1");
        keyPairGenerator.initialize(ecSpec);
        KeyPair keyPair = keyPairGenerator.generateKeyPair();

        // Get private and public keys
        PrivateKey privateKey = keyPair.getPrivate();
        PublicKey publicKey = keyPair.getPublic();

        // Original message to be signed
        String message = "Cryptography with elliptic curves in Java";

        // Sign the message with the private key
        Signature signature = Signature.getInstance("SHA256withECDSA");
        signature.initSign(privateKey);
        signature.update(message.getBytes());
        byte[] signedMessage = signature.sign();

        // Print the signed message (base64 encoded)
        String encodedSignature = Base64.getEncoder().encodeToString(signedMessage);
        System.out.println("Signed Message: " + encodedSignature);

        // Verify the signature with the public key
        signature.initVerify(publicKey);
        signature.update(message.getBytes());

        boolean isVerified = signature.verify(signedMessage);
        if (isVerified) {
            System.out.println("Signature is valid.");
        } else {
            System.out.println("Signature is invalid.");
        }
    }
}
