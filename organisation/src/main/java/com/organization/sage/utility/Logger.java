package com.organization.sage.utility;

import com.organization.sage.config.ConsoleColors;
import com.organization.sage.model.LogType;

public class Logger {
    /**
     * Prints a message to the console with color coding based on the log type.
     *
     * @param message The message to print.
     * @param type    The type of log (SUCCESS or ERROR).
     */
    public static void print(String message, LogType type) {
        switch (type) {
            case SUCCESS:
                System.out.println(ConsoleColors.GREEN + message + ConsoleColors.RESET);
                break;
            case ERROR:
                System.out.println(ConsoleColors.RED + message + ConsoleColors.RESET);
                break;
            default:
                System.out.println(message);
        }
    }
}
