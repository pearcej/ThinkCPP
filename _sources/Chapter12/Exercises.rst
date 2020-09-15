Multiple Choice Exercises
-------------------------

.. mchoice:: mce_12_1
    :practice: T

    You can have a vector that stores a vector of objects.

    - True

      + C++ allows for a variety of different compositions.

    - False
    
      - Vectors can store objects and vectors can store vectors. Can a vector store a vector that stores objects?

.. mchoice:: mce_12_2
    :practice: T

    What is the value of ``card``?

    .. code-block:: cpp

        struct Card {
          int suit, rank;
          Card ();
          Card (int s, int r);
        };

        Card::Card () {
          suit = 0;  rank = 0;
        }

        Card::Card (int s, int r) {
          suit = s;  rank = r;
        }

        int main() {
          Card card (2, 8);
        }

    - Ace of Clubs

      - How did we define our mapping earlier in the chapter?

    - 8 of Hearts
    
      + ``card`` has a ``suit`` value of 2 corresponding to Hearts, and a ``rank`` value of 8.

    - King of Hearts
    
      - How did we define our mapping earlier in the chapter?

    - ``card`` does not have a value.
    
      - We initialized ``card`` with a ``suit`` value of 2 and a ``rank`` value of 8.

.. mchoice:: mce_12_3
    :practice: T

    There is an error with the code below. Can you find it?

    .. code-block:: cpp

        struct Card {
          int suit, rank;
          Card ();
          Card (int s, int r);
          void print () const;
        };

        int main() {
          Card card (1,3);
          print (card);
        }

    - ``card`` is not a valid ``Card``.

      - A ``suit`` of 1 and a ``rank`` of 3 maps to the 3 of Diamonds.

    - There shouldn't be a semicolon after the ``struct`` definition.
    
      - A ``struct`` definition always ends with a semicolon.

    - ``print`` is a member function.
    
      + Since ``print`` is a member function, we need to use the dot operator.

    - There is nothing wrong with the code.
    
      - There is an error with the code. Can you find it?

.. mchoice:: mce_12_4
    :practice: T

    In order to check to see if two ``Card``\s are equal, we can use the ``==`` operator.

    - True

      - The ``==`` operator does not work for user-defined types like ``Card``.

    - False
    
      + We have to write a function that compares two ``Card``\s.

.. mchoice:: mce_12_5
    :practice: T

    What is the output of the code below?

    .. code-block:: cpp

       struct Card {
         int suit, rank;
         Card ();
         Card (int s, int r);
         void print () const;
         bool isGreater (const Card& c2) const;
       };

       int main() {
         Card card1 (2,12);
         Card card2 (2,2);
         cout << card1.isGreater (card2) << endl;
       }

    - True

      - The output of a ``bool`` is either a 0 or 1.

    - False
    
      - The output of a ``bool`` is either a 0 or 1.

    - 0
    
      - Is ``card1`` greater than ``card2``?

    - 1
    
      + The Queen of Hearts is greater than the 2 of Hearts.

.. mchoice:: mce_12_6
    :practice: T

    What is the output of the code below?

    .. code-block:: cpp

       struct Card {
         int suit, rank;
         Card ();
         Card (int s, int r);
         void print () const;
         bool isGreater (const Card& c2) const;
       };

       vector<Card> buildDeck();

       bool equals (const Card& c1, const Card& c2){
         return (c1.rank == c2.rank && c1.suit == c2.suit);
       }

       void printDeck(const vector<Card>& deck);

       int find (const Card& card, const vector<Card>& deck);

       int main() {
         vector<Card> deck = buildDeck();
         Card card (3, 13);
         cout << find(card, deck);
       }

    - 51

      + The ``card`` is the King of Spades, which is located at the end of the deck.

    - 52
    
      - Since the ``vector`` is size 52, it cannot have an index of 52.

    - 12
    
      - What is the value of ``card``?

    - -1
    
      - What is the value of ``card``?

.. mchoice:: mce_12_7
    :practice: T

    There is no faster way to search through an unsorted vector than using a linear search.

    - True

      + If the ``vector`` were sorted, then there are faster search methods.

    - False
    
      - Since the ``vector`` is unsorted, we must go through the vector and check every element.

.. mchoice:: mce_12_8
    :practice: T

    How many times does ``findBisect`` need to call itself in order to find the King of Diamonds?

    .. code-block:: cpp
    
        struct Card {
          int suit, rank;
          Card ();
          Card (int s, int r);
          void print () const;
          bool isGreater (const Card& c2) const;
        };

        vector<Card> buildDeck();
        bool equals (const Card& c1, const Card& c2);
        void printDeck(const vector<Card>& deck);
        int find (const Card& card, const vector<Card>& deck);
        int findBisect (const Card& card, const vector<Card>& deck, int low, int high);

        int main() {
          vector<Card> deck = buildDeck();
          Card card (1, 13);
          cout << findBisect(card, deck, 0, 51);
        }

    - 0

      + The King of Diamonds is right in the middle of the deck, so it doesn't need to call itself.

    - 1
    
      - Where is the King of Diamonds located relative to the sorted deck?

    - 3
    
      - Where is the King of Diamonds located relative to the sorted deck?

    - 4
    
      - Where is the King of Diamonds located relative to the sorted deck?

.. mchoice:: mce_12_9
    :practice: T

    There is no such thing as an empty object.

    - True

      + All variables are given default values unless otherwise specified by the user.

    - False
    
      - All variables have values at all times.

.. mchoice:: mce_12_10
    :practice: T

    What is the process of modeling a complex system with a simplified description in order to suppress unnecessary details while capturing relevant behavior?

    - Generalization

      - Generalization means to take something specific and make it more general.

    - Encapsulation
    
      - Encapsulation means taking a piece of code and wrapping it up in a function.

    - Abstraction
    
      + Using this process, we can remove unnecessary details to focus on the more important aspects.

    - Implementation
    
      - Implementation is the process of taking an idea and making it real.