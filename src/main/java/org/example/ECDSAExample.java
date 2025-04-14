package org.example;
import java.security.*;
import java.io.*;

public class ECDSAExample {

    public static void main(String[] args) throws Exception {
      KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
      kpg.initialize(2048);
      KeyPair kp = kpg.generateKeyPair();
      Files.write(new File("pub.der").toPath(), kp.getPublic().getEncoded());
      Files.write(new File("priv.der").toPath(), kp.getPrivate().getEncoded());
    }
}
