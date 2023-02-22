import java.nio.charset.Charset;
import java.util.Scanner;

// 
// Decompiled by Procyon v0.5.36
// 

class FlagChecker
{
    public static void main(final String[] array) {
        System.out.print("What's the flag? ");
        System.out.flush();
        final Scanner scanner = new Scanner(System.in);
        final String nextLine = scanner.nextLine();
        scanner.close();
        final byte[] bytes = nextLine.getBytes(Charset.forName("UTF-8"));
        if (bytes.length == 38 &&
 ((bytes[34] ^ bytes[23] * 7 ^ ~bytes[36] + 13) & 0xFF) == 0xB6 &&
 ((bytes[37] ^ bytes[10] * 7 ^ ~bytes[21] + 13) & 0xFF) == 0xDF &&
 ((bytes[24] ^ bytes[23] * 7 ^ ~bytes[19] + 13) & 0xFF) == 0xCD &&
 ((bytes[25] ^ bytes[13] * 7 ^ ~bytes[23] + 13) & 0xFF) == 0x90 &&
 ((bytes[6] ^ bytes[27] * 7 ^ ~bytes[25] + 13) & 0xFF) == 0x8A &&
 ((bytes[4] ^ bytes[32] * 7 ^ ~bytes[22] + 13) & 0xFF) == 0xE3 &&
 ((bytes[25] ^ bytes[19] * 7 ^ ~bytes[1] + 13) & 0xFF) == 0x6B &&
 ((bytes[22] ^ bytes[7] * 7 ^ ~bytes[29] + 13) & 0xFF) == 0x55 &&
 ((bytes[15] ^ bytes[10] * 7 ^ ~bytes[20] + 13) & 0xFF) == 0xBC &&
 ((bytes[29] ^ bytes[16] * 7 ^ ~bytes[12] + 13) & 0xFF) == 0x58 &&
 ((bytes[35] ^ bytes[4] * 7 ^ ~bytes[33] + 13) & 0xFF) == 0x54 &&
 ((bytes[36] ^ bytes[2] * 7 ^ ~bytes[4] + 13) & 0xFF) == 0x67 &&
 ((bytes[26] ^ bytes[3] * 7 ^ ~bytes[1] + 13) & 0xFF) == 0xD8 &&
 ((bytes[12] ^ bytes[6] * 7 ^ ~bytes[18] + 13) & 0xFF) == 0xA5 &&
 ((bytes[12] ^ bytes[28] * 7 ^ ~bytes[36] + 13) & 0xFF) == 0x97 &&
 ((bytes[20] ^ bytes[0] * 7 ^ ~bytes[21] + 13) & 0xFF) == 0x65 &&
 ((bytes[27] ^ bytes[36] * 7 ^ ~bytes[14] + 13) & 0xFF) == 0xF8 &&
 ((bytes[35] ^ bytes[2] * 7 ^ ~bytes[19] + 13) & 0xFF) == 0x2C &&
 ((bytes[13] ^ bytes[11] * 7 ^ ~bytes[33] + 13) & 0xFF) == 0xF2 &&
 ((bytes[33] ^ bytes[11] * 7 ^ ~bytes[3] + 13) & 0xFF) == 0xEB &&
 ((bytes[31] ^ bytes[37] * 7 ^ ~bytes[29] + 13) & 0xFF) == 0xF8 &&
 ((bytes[1] ^ bytes[33] * 7 ^ ~bytes[31] + 13) & 0xFF) == 0x21 &&
 ((bytes[34] ^ bytes[22] * 7 ^ ~bytes[35] + 13) & 0xFF) == 0x54 &&
 ((bytes[36] ^ bytes[16] * 7 ^ ~bytes[4] + 13) & 0xFF) == 0x4B &&
 ((bytes[8] ^ bytes[3] * 7 ^ ~bytes[10] + 13) & 0xFF) == 0xD6 &&
 ((bytes[20] ^ bytes[5] * 7 ^ ~bytes[12] + 13) & 0xFF) == 0xC1 &&
 ((bytes[28] ^ bytes[34] * 7 ^ ~bytes[16] + 13) & 0xFF) == 0xD2 &&
 ((bytes[3] ^ bytes[35] * 7 ^ ~bytes[9] + 13) & 0xFF) == 0xCD &&
 ((bytes[27] ^ bytes[22] * 7 ^ ~bytes[2] + 13) & 0xFF) == 0x2E &&
 ((bytes[27] ^ bytes[18] * 7 ^ ~bytes[9] + 13) & 0xFF) == 0x36 &&
 ((bytes[3] ^ bytes[29] * 7 ^ ~bytes[22] + 13) & 0xFF) == 0x20 &&
 ((bytes[24] ^ bytes[4] * 7 ^ ~bytes[13] + 13) & 0xFF) == 0x63 &&
 ((bytes[22] ^ bytes[16] * 7 ^ ~bytes[13] + 13) & 0xFF) == 0x6C &&
 ((bytes[12] ^ bytes[8] * 7 ^ ~bytes[30] + 13) & 0xFF) == 0x75 &&
 ((bytes[25] ^ bytes[27] * 7 ^ ~bytes[35] + 13) & 0xFF) == 0x92 &&
 ((bytes[16] ^ bytes[10] * 7 ^ ~bytes[14] + 13) & 0xFF) == 0xFA &&
 ((bytes[21] ^ bytes[25] * 7 ^ ~bytes[12] + 13) & 0xFF) == 0xC3 &&
 ((bytes[26] ^ bytes[10] * 7 ^ ~bytes[30] + 13) & 0xFF) == 0xCB &&
 ((bytes[20] ^ bytes[2] * 7 ^ ~bytes[1] + 13) & 0xFF) == 0x2F &&
 ((bytes[34] ^ bytes[12] * 7 ^ ~bytes[27] + 13) & 0xFF) == 0x79 &&
 ((bytes[19] ^ bytes[34] * 7 ^ ~bytes[20] + 13) & 0xFF) == 0xF6 &&
 ((bytes[25] ^ bytes[22] * 7 ^ ~bytes[14] + 13) & 0xFF) == 0x3D &&
 ((bytes[19] ^ bytes[28] * 7 ^ ~bytes[37] + 13) & 0xFF) == 0xBD &&
 ((bytes[24] ^ bytes[9] * 7 ^ ~bytes[17] + 13) & 0xFF) == 0xB9) {
            
            System.out.println("Correct!");
        }
        else {
            System.out.println("Not quite...");
        }
    }
}

