Multiple Choice Exercises
-------------------------

.. mchoice:: vectors_mc1

    Suppose you are collecting data for a science experiment. You are to perform three trials of eight temperature
    readings measured in degrees fahrenheit to the nearest hundredth and initialized to *freezing*.  Choose the vector 
    that has the proper amount of storage for this scenario.

    -   ``vector<int> temps (24, 32.00);``

        -   We can't declare the vector as an integer type because all temperature readings
            will be truncated.

    -   ``vector<double> temps (24, 32.00);``

        +   First comes the vector size, *then* the initial values.

    -   ``vector<double> temps (0.00, 24);``

        -   Freezing is 32 degrees fahrenheit.  The order of parameters is incorrect.

    -   ``vector<double> temps (32, 24.00);``

        -   This statement creates a vector size 32 with elements initialized to 24.00 degress fahrenheit.


.. mchoice:: vectors_mc2

    Suppose the following code is run:
    
    .. code-block::
    
       vector<string> lauren = {"happy", "to", "you", "September", "birthday", "girl"}

    How would you save the string ``"birthday"`` from ``lauren`` to the variable ``nurse``?

    -   ``nurse = lauren[3]``

        -   Remember, vectors are zero-indexed!

    -   ``nurse = lauren[4]``

        +   Vectors are zero-indexed, so the fifth element is the fourth index.

    -   ``nurse = lauren[5]``

        -   Remember, vectors are zero-indexed!

    -   ``nurse = lauren(3)``

        -   This is not proper indexing.  Also, vectors are zero-indexed.

    -   ``nurse = lauren(4)``

        -   This is not proper indexing.


.. mchoice:: vectors_mc3

    Select all of the following statments that correctly make a copy of ``lauren``.
    
    .. code-block::
    
       vector<string> lauren = {"happy", "to", "you", "September", "birthday", "girl"}

    How would you save the string ``"birthday"`` from ``lauren`` to the variable ``nurse``?

    -   ``vector<string> harry (lauren)``

        +   This syntax is correct, but isn't used often.

    -   ``vector<string> lauren (ella)``

        -   You make a copy of the vector in parentheses.

    -   ``vector<string> lauren = mariah``

        -   Remember how assignment statements work!

    -   ``vector<katie> string = lauren``

        -   This is not proper syntax.

    -   ``vector<string> mariah = lauren``

        +   This is the most common syntax.


.. mchoice:: vectors_mc4

    What is the value of nums after the following code executes?
    
    .. code-block::
    
       int main () {
           vector<int> nums = {0, 8, 5, 1, 4, 3};
           for (int i = 0; i < 6; i++) {
               if (nums[i] % 2 == 0) {
                  nums[i]--;   
               }
               nums[i] = nums[i] * 2;
           }
           cout << nums[1];
       }

    -   {0, 8, 5, 1, 4, 3}

        -   ``nums`` is modified inside of the loop.

    -   {0, 16, 10, 2, 8, 6}

        -   Take a look at the conditional.

    -   {0, 16, 8, 0, 8, 4}

        -   Take a closer look at the conditional.

    -   {-2, 14, 10, 2, 6, 6}

        +   All even numbers were decremeneted, then all numbers were multiplied by 2.

    -   {2, 18, 10, 2, 10, 6}

        -   Take a closer look at what happens inside of the conditional.


.. mchoice:: vectors_mc5

    **Multiple Response** Select all ways to print out the contents of ``ryan`` without
    going out of bounds.
    
    .. code-block::
    
       vector<int> ryan = {2, 3, 1, 5, 6, 0, 0, 5, 4};

    -   .. code-block::
           
           for (int i = 0; i < ryan.size(); ++i) {
               cout << ryan[i] << " ";
           }

        -   When we deal with the ``size`` function, we can't use type ``int``.

    -   .. code-block::
           
           for (size_t j = 0; j < ryan.size(); j++) {
               cout << ryan[j] << " ";
           }

        +   When we deal with the ``size`` function, we must use type ``size_t``.

    -   .. code-block::
           
           for (int k = 0; k < 8; ++k) {
               cout << ryan[k] << " ";
           }

        -   There are 9 elements, numbered 0 through 8, but here we only iterate through 8 of them.

    -   .. code-block::
           
           for (int n = 0; n < 9; n++) {
               cout << ryan[n] << " ";
           }

        +   There are 9 elements numbered 0 through 8, and this statement iterates over all of them.

    -   .. code-block::
           
           for (int m = 0; m <= 8; ++m) {
               cout << ryan[m] << " ";
           }

        +   There are 9 elements numbered 0 through 8, and this statement iterates over all of them.


.. mchoice:: vectors_mc6

    Suppose you want ``ryan`` to have the value

    .. code-block::
    
       vector<int> ryan = {2, 3, 1, 5, 6, 7, 8, 9};
    
    What vector functions will you use to achieve this, and how many times will you use them?
    Keep in mind, ``ryan`` is currently the following vector of integers.

    .. code-block::
    
       vector<int> ryan = {2, 3, 1, 5, 6, 0, 0, 5, 4};

    -   Use ``push_back`` 4 times with no arguments to get rid of the last 4 elements, then use ``push_back`` 3 times
        with arguments to specify which values you want to add to the end.

        -   You'll need to use two *different* functions to accomplish this task.

    -   Use ``push_back`` 4 times with no arguments to get rid of the last 4 elements, then use ``pop_back`` 3 times
        with arguments to specify which values you want to add to the end.

        -   ``push_back`` *pushes* new items onto the end of the vector, and ``pop_back`` *pops* old items off the end of the vector.

    -   Use ``pop_back`` 4 times with no arguments to get rid of the last 4 elements, then use ``pop_back`` 3 times
        with arguments to specify which values you want to add to the end.

        -   You'll need to use two *different* functions to accomplish this task.

    -   Use ``pop_back`` 4 times with no arguments to get rid of the last 4 elements, then use ``push_back`` 3 times
        with arguments to specify which values you want to add to the end.

        +   T``push_back`` *pushes* new items onto the end of the vector, and ``pop_back`` *pops* old items off the end of the vector.


.. mchoice:: vectors_mc7

    Suppose you are randomly assigning students to discussions 1-8.  How would you do this correctly?  Assume
    you have alreay implemented the following code.
    
    .. code-block::

       int x = random ();
    
    -   .. code-block ::
        
           int y = x % 7;
           y = y + 1;

        +   The first part creates a random number between 0 and 7 (8 numbers) and the second part adds 1 so that
            our random number is actually between 1 and 8.

    -   .. code-block ::
        
           int y = x % 8;
           y = y + 1;

        -   The first part creates a random number between 0 and 8 (9 numbers).  This is too many.

-   .. code-block ::
        
           int y = x % 7;

        -   This creates a random number between 0 and 7 (8 numbers), which are not the numbers we are looking for.

    -   .. code-block ::
        
           int y = x % 8;

        -   The first part creates a random number between 0 and 8 (9 numbers).  This is too many, and not the numbers we are looking for.

