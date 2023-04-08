# SWAPI_Playground
This GitHub repository is a playground for experimenting with the Star Wars API (SWAPI). It includes sample code for various actions that can be performed using SWAPI, allowing developers to quickly test and explore the capabilities of this popular API.

## 1. Adding the appropriate modules
- Install virtualenv (in case you haven't) by executing:
    ```source
    pip install virtualenv
    ```

- Create your virtual enviroment by executing:
    ```
    <python version> -m venv <your venv name>
    ```
- In order to activate the virtual enviroment, execute the following command:
    ```
    source <your venv name>/bin/activate
    ```

-   After activating the virtual enviroment, install the appropriate modules, while in the root directory by executing:
    ```source
    pip install -r requirements.txt
    ```

## 2. Functionality Samples
- Search the SWAPI for any user given character. For example by executing:
    ```
    python main.py search <character name>
    ```
    Note: The character name should be enclosed in quotes

- If a character is found the program should print the following message on the screen:
    ```
    Name: <Character's name>
    Height: <Character's height>
    Mass: <Character's mass>
    Birth Year: <Character's birth year>
    ```

- If a character is not found the program prints the following message on the screen:
    ```
    The force is not strong within you
    ```

### 2.1 Getting more information about a character:
- In order to get more information about a the home world of a character we can provide the following argument, while executing the script:

    ```
    python main.py search <character name> --world
    ```

- If a character is found the program should print the following message on the screen:
    ```
    Name: <Character's name>
    Height: <Character's height>
    Mass: <Character's mass>
    Birth Year: <Character's birth year>

    Homeworld
    ____________
    Name: <Character's homeworld planet name>
    Population:<Character's homeworld planet population>

    On <character's homeworld panet's name>, 1 year on earth is <number of years> years and 1 day is <number of days> days
    ```

- If a character is not found the program prints the following message on the screen:
    ```
    The force is not strong within you
    ```

## 3. Implementing API requests caching

- In order to implement api request caching a functionality has been added to store the api request, the search term and the request timestamp into a .json file, that would be the cache memory. To do so, the script should be executed by typing the following command:

    ```
    python main.py search <character name>
    ```
    or, in case we need more information about the character' world:
    ```
    python main.py search <character name> --world
    ```

- If a character is found the program should print the following message on the screen:
    ```
    Name: <Character's name>
    Height: <Character's height>
    Mass: <Character's mass>
    Birth Year: <Character's birth year>

    cached: <the timestamp>
    ```
    or in case we need more information about the character' world:

    ```
    Name: <Character's name>
    Height: <Character's height>
    Mass: <Character's mass>
    Birth Year: <Character's birth year>

    Homeworld
    ____________
    Name: <Character's homeworld planet name>
    Population:<Character's homeworld planet population>

    On <character's homeworld panet's name>, 1 year on earth is <number of years> years and 1 day is <number of days> days

    cached: <the timestamp>
    ```
- In both cases, if a character is not found the program prints the following message on the screen:
    ```
    The force is not strong within you
    ```


## 3.1 In order to clean the cache, execute the following command:
    ```
    python main.py cache --clean
    ```