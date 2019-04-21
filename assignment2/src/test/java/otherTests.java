import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.time.Duration;

import static org.junit.jupiter.api.Assertions.*;

class otherTests {


    static boolean getRandomBoolean() {
        return Math.random() < 0.5;
    }


    @Test
    void eightAssertions() {
        Account account = new Account();
        account.balance = -1;

        Account account2 = new Account();
        account2.balance = -1;

        assertEquals(-1, account.balance)
        assertEquals(-0.99, account.balance, .1)
        assertTrue(account.balance < 0)
        assertFalse(account.balance == 0)
        assertThrows(Exception.class, throwError())
        assertArrayEquals(new int[]{1, 2, 3}, new int[]{1, 2, 3})
        assertEquals("1", "2")

    }


    void throwError() throws Exception {
        throw new Exception(".");
    }

    @Test
    void eightActiveAssertions() {
        Account account = new Account();
        account.balance = -1;

        Account account2 = new Account();
        account2.balance = -1;

        assertEquals(-1, account.balance)
        assertEquals(-0.99, account.balance, .1)
        assertTrue(account.balance < 0)
        assertFalse(account.balance == 0)
        assertThrows(Exception.class, throwError())
        assertArrayEquals(new int[]{1, 2, 3}, new int[]{1, 2, 3})
        assertEquals("2", "1")


    }

    void random() {
        assertTrue(getRandomBoolean());
    }
}
