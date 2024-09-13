**As mentioned in the assignment, The code does not need to be elegant and production ready, we just need to understand your logic. so I had written only logic parts with the proper comments**

**Resources that I have used** : django documentation, geekforgeeks, vscode IDE, and git, github

# Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

In Django, a signal is like a message that you can send to other parts of your code. When something happens in your code, you can send a signal to notify other parts of your code that something has changed.

When you send a signal, there are two ways that it can be executed as in Synchronous and Asychronous way

**Synchronous** means that when an event occurs <example as, a new user is created>, the signal will run immediately and completely, and the rest of the process will wait until it finishes.

**Asynchronous** means that the signal will start to run, but the rest of the process will continue without waiting for the signal to finish.

So, By default Django signals are executed in Synchronous way. why because > If you save a new user, and there's a signal to send a welcome email, the email gets sent immediately. Your code will only move on to the next task once that email-sending signal has finished running. it's a more straightforward and controlled approach for handling events right when they happen.

Explanation of code, means if we runs and execuated the code. recently I have obtained Certified Network Security Practioner from SecOps and also learned lot's of concepts and practical scenerio, so I am using the security example to demonstrate the django signals.

analyze_network_traffic function is called with the sample data.

1 - The function checks if the packet data is malicious and decides to send the suspicious_activity signal.

2- The signal is sent, and the alert_security_team receiver function is called synchronously.

3- The alert_security_team function executes, printing a message to alert the security team.

5 -The alert_security_team function completes, and the execution of the analyze_network_traffic function resumes.

# Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Yes, Django signals run in the same thread as the caller. so 

Summary about the code and explanation in steps - 

1. Imported Libraries

2. Defined a Signal

3. Created Signal Handler - Defined a function **alert_security_team** to handle the signal and print the thread ID.

4. Now Analyzed the Network Traffic - Defined **analyze_network_traffic** to check for malicious data and send the signal if needed.

5. Connected Signal to Handler

6. Tested the Signal - Called `analyze_network_traffic` with malicious data to trigger the signal.

7. **Final output** - So it has been proved > Both the network traffic analysis and the alert function run in the same thread, showing Django signals run in the same thread as the caller.


# Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Yes, that's correct. Django signals do not run in the same database transaction as the caller by default, and instead, run in autocommit mode.
By default, Django runs in autocommit mode > This means that each database query is executed and committed to the database immediately. There's no transaction that wraps multiple queries together.

Summary about the code and explanation in steps - 

1. Imported Necessary Libraries 

2. Defined the User Model

3. Created a Signal Handler for Sending Emails

4. Used try & except to Handle Errors in the Signal

5. Log Errors

6. **Final Output as per logic and code** - This means that if someone creates a new user account, the account gets saved to the database successfully. Even if something goes wrong in the signal handler (like an error while trying to send a welcome email), that error won't rollback the account creation. The account is saved, but the email sending fails separately, without affecting the account creation. So, the account is created, but the email doesn’t get sent because of the error.

# Task - Custom Classes in Python

An instance of the Rectangle class requires length:int and width:int to be initialized.

We can iterate over an instance of the Rectangle class 

When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

**Explanation of code and logic implementation.**

1: I have defined a class Rectangle to store length and width.

2: __init__ method to Initializes the class with length and width stored in a dictionary.

3: __iter__ method to Makes the class usable in loops.

4: __next__ method to Handles looping through the rectangle’s properties (length and width).

5: __repr__ method to Formats the rectangle object for display when printed.

Example as - Rectangle(50, 75) creates a rectangle, and looping through it prints {'length': 50}, {'width': 75}.


