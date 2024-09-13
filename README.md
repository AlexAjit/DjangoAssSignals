#Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

#concept
#In Django, a signal is like a message that you can send to other parts of your code. When something happens in your code, you can send a signal to notify other parts of your code that something has changed.

# So now, Synchronous vs Asynchronous

# When you send a signal, there are two ways that it can be executed as in Synchronous and Asychronous way

#Synchronous means that when an event occurs <example as, a new user is created>, the signal will run immediately and completely, and the rest of the process will wait until it finishes.

#Asynchronous means that the signal will start to run, but the rest of the process will continue without waiting for the signal to finish.

#So, By default Django signals are executed in Synchronous way. why because > If you save a new user, and there's a signal to send a welcome email, the email gets sent immediately. Your code will only move on to the next task once that email-sending signal has finished running. it's a more straightforward and controlled approach for handling events right when they happen.
