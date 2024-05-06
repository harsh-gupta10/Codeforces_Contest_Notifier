# Codeforces Contest Notifier

## Introduction
Welcome to Codeforces Contest Notifier! This is a Whatsapp-based notifier designed to keep you updated on upcoming Codeforces contests. With this tool, you'll receive daily notifications about contests scheduled within the next 48 hours, including comprehensive details about each contest.

## Constraints
This notifier is developed to cater to personal needs due to financial constraints. However, it's designed in a way that can be easily expanded for wider usage. Currently, it utilizes Twilio, a third-party service for sending messages to Whatsapp. Please note that the free version of Twilio supports sending messages to a single phone number only. Additionally, for hosting, PythonAnywhere is utilized, which allows hosting only one script and has computational constraints.

## Getting Started
If you're interested in building your notifier, follow these steps:

1. Clone this repository to your local machine.
2. Create an account on Twilio and set up the required configurations for sending messages on Whatsapp.
3. Set the following parameters in your environment variables:

    ```python
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    from_no = os.environ.get('TWILIO_FROM_NUMBER')
    to_no = os.environ.get('TWILIO_TO_NUMBER')
    ```

4. If you our from outside India Then change your timezone ie the line 
  ``` 
  india_timezone = pytz.timezone('Asia/Kolkata')
  ```

5. Run the script on your preferred hosting platform or locally. Ensure it runs daily to provide timely notifications about upcoming contests.

6. You're now all set! Never miss any Codeforces contest again.

## Contribution
Contributions to this project are welcome. If you have any suggestions for improvements or would like to contribute new features, feel free to fork this repository and submit a pull request.


