Returning from main
-------------------

Now that we have functions that return values, I can let you in on a
secret. main is not really supposed to be a void function. It’s supposed
to return an integer:

::

    int main ()
    {
      return 0;
    }

The usual return value from main is 0, which indicates that the program
succeeded at whatever it was supposed to do. If something goes wrong, it
is common to return -1, or some other value that indicates what kind of
error occurred.

Of course, you might wonder who this value gets returned to, since we
never call main ourselves. It turns out that when the system executes a
program, it starts by calling main in pretty much the same way it calls
all the other functions.

There are even some parameters that are passed to main by the system,
but we are not going to deal with them for a little while.


.. mchoice:: return_main_1
   :answer_a: string
   :answer_b: integer
   :answer_c: nothing
   :answer_d: anything
   :correct: b
   :feedback_a: Look at the function definition for main.
   :feedback_b: Correct!  You should always return an integer to avoid issues down the road.
   :feedback_c: Main is supposed to return something!
   :feedback_d: Main has a return type, check its function definition.

   What data type is the main function supposed to return?


.. fillintheblank:: return_main_2

    Usually, we return |blank| to exit main.  However, if there are
    any errors that we catch, we might return |blank|.

    - :[0]: Correct!
      :x: Try again!
    - :-1: Correct!
      :.*: Try again!

