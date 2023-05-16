```

public class EmailNotValidException extends Exception{
	//*****************START*****************Solution 3.1 + 3.2*****************

    public EmailNotValidException(String message) {
        super(message);
    }


    //*****************END*****************Solution 3.1 + 3.2*****************
    
    public static void main(String[] args) {
		try {
			throw new EmailNotValidException("Custom Message");
		} catch (EmailNotValidException e) {
			System.out.println(e.getMessage());
		}

		/**
		 * Your output should look like this.
		 * Custom Message
		 */
	}
}

```