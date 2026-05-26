import java.util.logging.Logger;
import java.util.logging.Level;

public class LogApp {

    private static final Logger logger = Logger.getLogger(LogApp.class.getName());

    public static void main(String[] args) throws InterruptedException {
        while (true) {
            logger.info("User login successful");
            logger.warning("Permission denied");
            logger.severe("Database connection failed");
            Thread.sleep(1000);
        }
    }
}

