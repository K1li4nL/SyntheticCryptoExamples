package org.example;
import javax.crypto.*;
import javax.crypto.spec.IvParameterSpec;
import java.security.SecureRandom;
import java.util.Arrays;

public class ECDSAExample {

    public static void main(String[] args) throws Exception {
      SecretKey key = generateKey();
      String data = "Hello";
      String iv = "bad iv 123456789";
      
      byte[] ct = encrypt(key, data.getBytes(), iv.getBytes());
      System.out.println(Arrays.toString(ct));
   }

    public static SecretKey generateKey() throws Exception {
        KeyGenerator kg = KeyGenerator.getInstance("AES");
        kg.init(256);
        return kg.generateKey();
    }

    public static byte[] encrypt(SecretKey key, byte[] data, byte[] iv) throws Exception {
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, key, new IvParameterSpec(iv));
        return cipher.doFinal(data);
    }
}
