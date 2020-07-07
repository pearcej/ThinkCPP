Multiple Choice Questions
-------------------------

Answer the following **Multiple Choice** questions to
assess what you have learned in this chapter.


.. mchoice:: programming_1

    What is a **program** in computer science?

    -   a planned series of events, a schedule

        -   This is a definition of a program, just not in the computer science sense.

    -   a translated language that is easy for the computer to understand

        -   This is actually called a low-level language!

    -   a sequence of instructions that specifies how to perform a computation

        +   You can write these instructions to accomplish pretty much anything 
            you want!

    -   a general process for solving a category of problems

        -   This is actually called an algorithm!


.. mchoice:: programming_2

    What is the function of the compiler?

    -   It loads the program from its saved location and makes the computer execute it.

        -   This is the function of an executor.  If you use a compiler, you must also
            use an executer to run your code.

    -   It reads a high-level program and translates everything at once, before executing
        any of the commands.

        +   If there are any errors in your code, the program will not compile.  It is an
            all-or-nothing process.

    -   It translates the program from the low-level language you coded in to a high-level
        language that the computer can understand.

        -   You, the programmer, write your program in a HIGH-level language.  It is then
            translated to a LOW-level language that the computer can understand.

    -   It translates the program line-by-line, alternately reading lines and carrying 
        out commands.

        -   This is the function of an interpreter.


.. mchoice:: programming_3

    What is the difference between **source code** and **object code**?

    -   Source code can contain simple things like variables and values.  Object code 
        can contain more complex objects like data structures.

        -   Contrary to it's name, object code has nothing to do with creating objects!

    -   Object code can contain simple things like variables and values.  Source code 
        can contain more complex objects like data structures.

        -   Not quite!

    -   Object code is the code that your program is written in.  Source code is the
        translated version of this code that the computer can understand.

        -   You seem to have things a bit mixed up!

    -   Source code is the code that your program is written in.  Object code is the
        translated version of this code that the computer can understand.

        +   The computer can either use an interpreter or a compiler to make the 
            translation.


.. mchoice:: programming_4

    **Multiple Response**  What are the basic functions that appear in just about 
    every programming language?

    -   math operations

        +   This is how your program can carry out complex calculations!

    -   debugging

        -   Debugging is a process that is separate from the program.

    -   input/output from the terminal and saved files

        +   This allows your program to communicate with data either from the user, 
            or from the user's saved files.

    -   testing for conditions

        +   Typically, you'd want to test for certain conditions and then execute an
            appropriate sequence of statements depending on whether the conditions
            were met.

    -   repetition

        +   This is why you would consider using a loop in your program.


.. mchoice:: programming_5

    What type of error would the following generate?  Assume you are
    trying to calculate the volume of a cylinder:

    ::

        int radius = 7;
        int height = 8;
        double volume = 3.14 * radius * height;

    -   syntax error

        -   There is nothing wrong with the structure of this program.

    -   run-time error

        -   There are no errors that will surface at runtime.

    -   semantic error

        +   This is not the correct formula for calculating the volume of a
            cylinder.  This program will go on to calculate the wrong volume
            because it doesn't know any better.

    -   no error

        -   Take a look at the area formula.


.. mchoice:: programming_6

    What type of error would the following generate?  Assume you are
    trying to calculate the volume of a cylinder:

    ::

        int radius = 7;
        int height = 8
        double volume = 3.14 * r * r * height;

    -   syntax error

        +   You are missing a semicolon on the second line, and you are using
            the variable ``r`` without defining it on the third line.  your
            program will not compile.

    -   run-time error

        -   There are no errors that will surface at runtime.

    -   semantic error

        -   Everything looks good with your volume calculations.

    -   no error

        -   Take a closer look at the structure of the code.


.. mchoice:: programming_7

    **Multiple Response**  Which of the following are true about C++.

    -   Some statements can have more than one meaning.  You have to put
        things into context to understand what they mean.

        -   Statements in C++ are unambiguous.  Each statement has exactly
            one meaning, regardless of its context.

    -   Programs are verbose in efforts to reduce misunderstandings.

        -   Programmers actually try to use as few lines of code as possible to
            get the job done!

    -   Each statement means exactly what it says.

        +   Programming in C++ is not supposed to be tricky!  For instance, 
            an integer is an ``int``, a character is a ``char``, and a string 
            of text is a ``string``.

    -   Programs in C++ are short and to the point.

        +   Programs in C++ are very concise.


.. mchoice:: programming_8

    **Multiple Response** Which of the following is true about the ``int main()``.

    -   The compiler ignores anything after ``//``.

        +   This is called a comment, which you can use to describe your code to
            outsiders who might not understand.

    -   There is no limit the number of statements you can put in ``int main()``.

        +   You can include as many statments as you want to, but it is good 
            practice to keep the main as short as possible.

    -   Program execution begins at the first line of code, and ends at ``int main().``

        -   Program execution actually begins with ``int main()``.  Then, program
            execution happens in order, from top to bottom.

    -   ``int main()`` is enclosed by squiggly brackets ``{ }``.

        +   ``int main()`` and *all* functions in C++ are enclosed by squiggly brackets.

    -   The end of a statement is marked with a colon ``:``.

        -   Actually, each statement is terminated with a *semi* colon ``;``.


.. mchoice:: programming_9
   :multiple_answers:
   :answer_a: High-level programs are only used for a few special applications.
   :answer_b: Programs written in a high-level language must be translated before they can be run.
   :answer_c: It's easier to program in a high-level language.
   :answer_d: Computers can only execute programs written in high-level languages.
   :answer_e: High-level programs can only run on one kind of computer (you'd have to rewrite the program if you wanted to use a different machine).
   :correct: b,c
   :feedback_a: Almost all programs are written in high-level languages!
   :feedback_b: All high-level programs must be translated to a low-level programs before the computer can execute them!
   :feedback_c: It takes less time to write in a high-level language, the code is shorter and easier to read, and it's more likely to be correct!
   :feedback_d: Computers can only execute programs in LOW-level languages.
   :feedback_e: High-level programs are portable, meaning they can run on different kinds of computers with little to no modification.

   **Multiple Response** Which is true about a high-level programming language?


.. mchoice:: programming_10
   :answer_a: analyzing a the syntax of a sentence
   :answer_b: looking through a program for errors
   :answer_c: examining a the syntactic structure of a program
   :answer_d: trying to understand the meaning of a program
   :correct: c
   :feedback_a: This is how we parse in the literary sense.
   :feedback_b: This is actually called debugging!
   :feedback_c: Parsing can help you find syntax errors.
   :feedback_d: This is analying the semantics, not the syntax!

   What is parsing in the coding sense?