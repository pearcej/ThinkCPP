Multiple Choice Exercises
-------------------------

Answer the following **Multiple Choice** questions to
assess what you have learned in this chapter.


.. mchoice:: cond_rec_mc1

    Say you run the following code.  What is the value of ``mod``?

    ::

        int x = 4;
        int y = 7;
        int mod = y % x;

    -   0

        +   There *is* a remainder.

    -   1

        -   Incorrect!

    -   2

        -   Incorrect!

    -   3

        +   The remainder of ``7 / 4`` is 3.

    -   4

        -   We can't have a remainder of 4, since 4 is the divisor.


.. mchoice:: cond_rec_mc2

    What is printed when the following code executes?

    ::

        int x = 8;

        if (x % 3 == 2) {
            cout << "hey!" << endl;
        }
        elif (x != 7) {
            cout << "hi!" << endl;
        }
        elif (x % 2 == 0) {
            cout << "hello!" << endl;
        }
        else {
            cout << "bye!" << endl;
        }

    -   ::

            hey!

        +   Since the first conditon is met, the rest of the chained
            conditional does not execute.

    -   ::

            hi!

        -   It's true that ``8 != 7``, but "hi!" is not printed here.

    -   ::

            hi!

        -   It's true that ``8 % 2 == 0``, but "hello!" is not printed!

    -   ::

            hey!
            hi!
            hello!

        -   All of these conditons are met, but only one expression is
            printed!

    -   ::

            bye!

        -   At least one of the conditons is met, so the ``else`` will not
            execute!


.. mchoice:: cond_rec_mc3

    What is printed when the following code executes?

    ::

        int x = 34;

        if (32 < x) {
            cout << "it's freezing!";
        }
        if (x < 50) {
            cout << "it's cold!";
        }
        if (x > 65) {
            cout << "sweater weather!"'
        }
        else {
            cout << "it's hot!";
        }

    -   ::

            it's freezing!

        -   Take a closer look at the conditions and the way they
            are written in the program.

    -   ::

            it's cold!

        -   Take a closer look at the conditions and the way they
            are written in the program.

    -   ::

            it's freezing!
            it's cold!

        -   You've identified some of the conditons that are met!
            Take another look at the *chain* of conditionals at the
            end!

    -   ::

            it's freezing!
            it's cold!
            it's hot!

        +   These statements are quite contradicting, but that's exactly
            what the output would be if we ran this code.

    -   ::

            it's hot!

        -   Take a closer look at the conditions and the way they
            are written in the program.


.. mchoice:: cond_rec_mc4

    Suppose you have defined the following function:

    ::

        void fortuneCookie (int a, bool b, char c) {
            if (c < 'm') {
                if (a % 2 == 0) {
                    cout << "An alien of some sort will be appearing to you shortly.";
                }
                else {
                    cout << "The fortune you seek is in another cookie.";
                }
            }
            elif (c < 'r') {
                if (b) {
                    cout << "He who laughs at himself never runs out of things to laugh at.";
                }
                else {
                    cout << "You will be hungry again in one hour.";
                }
            }
            else {
                cout << "Fortune not found? Abort, retry, ignore.";
            }
        }

    What will be your fortune if you run the following code?

    ::

        fortuneCookie('m', false, 14);

    -   ``An alien of some sort will be appearing to you shortly.``

        -   The nested conditional is true, but what about the outer condition?

    -   ``The fortune you seek is in another cookie.``

        -   Are either of the coditions met to reach this fortune?

    -   ``He who laughs at himself never runs out of things to laugh at.``

        -   The outer conditonal is true, but what about the inner condition?

    -   ``You will be hungry again in one hour.``

        +   ``'m' < 'r'`` is true and ``b`` is false.

    -   ``Fortune not found? Abort, retry, ignore.``

        -   The ``else`` never executes.


.. mchoice:: cond_rec_mc5

    Suppose you have defined the following function:

    ::

        void encourage (int a, int b, string mood) {
            if (mood == "bad") {
                if (a % b == 0) {
                    cout << "You're amazing!";
                }
                elif (b - a == 1) {
                    cout << "You will do great things!";
                }
                else {
                    cout << "You look good!";
                }
            }
            elif (mood == "good") {
                cout << "You don't need a compliment!";
            }
            else {
                if (a % 3 == 0) {
                    cout << "You go girl!";
                }
                elif (b % 7 == 0) {
                    cout << "Go get em!";
                }
            }
        }

    What words of encouragement will you hear if you run the following code?

    ::

        encourage (4, 5, "BAD");

    -   ``You will do great things!``

        -   The nested conditional is true, but what about the outer condition?
            Strings are case sensitive!

    -   ``You look good!``

        -   One of the inner conditions is met, so the ``else`` is not reached,
            but what about the outer condition?  Strings are case sensitive!

    -   ``You go girl!``

        -   The outer conditonal is true, but what about the inner condition?

    -   ``Go get em!``

        -   The outer conditonal is true, but what about the inner condition?

    -   None.

        +   None of the ``cout`` statements is reached.  You do not get any words
            of encouragement, but that's okay because you don't need any!  You're
            doing great!