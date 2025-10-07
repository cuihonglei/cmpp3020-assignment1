# 1. Problem Statement

**Problem:**  
Given a set of numbers, calculate the average of these numbers.

**Example Input:**  [5, 8, 12, 4, 10]  
**Example Output:**  7.8

**Explanation:**  
The formula for average is:  
Average = (Sum of all numbers) / (Number of numbers)

Applying it to the input:  
Average = (5 + 8 + 12 + 4 + 10) / 5 = 7.8

# 2. Pseudo-Code

**Pseudo-code to calculate the average of a list of numbers**

**Input:** A list of numbers called `numbers`  
**Output:** The average of the numbers

```plaintext
PROCEDURE calculateAverage(numbers)  
    BEGIN  
        SET sum <- 0                 # Initialize sum to 0
        SET count <- length(numbers) # Get the number of elements in the list

        FOR each number IN numbers DO
            sum <- sum + number      # Add each number to the sum
        END FOR

        SET average <- sum / count   # Divide sum by count to get the average
        RETURN average               # Return the calculated average
    END
END PROCEDURE
```

# 3. BNF Grammar

**We can describe the syntax of “finding the average of a set of numbers” using BNF.**

```plaintext
<average-problem> ::= "Given" <number-list> "," "calculate" "the" "average"

<number-list> ::= "[" <numbers> "]"

<numbers> ::= <number> | <number> "," <numbers>

<number> ::= <digit> | <digit> <number>

<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

- `<average-problem>` describes the full problem statement.  
- `<number-list>` describes the list of numbers in square brackets.  
- `<numbers>` recursively defines one or more numbers separated by commas.  
- `<number>` defines a sequence of digits.  

# 4. Parse Tree (BNF version)

**For the input: Given [5, 8, 12, 4, 10], calculate the average.**

```plaintext
<average-problem>
|-- "Given"
|-- <number-list>
|   |-- "["
|   |-- <numbers>
|   |   |-- <number> 5
|   |   |-- ","
|   |   |-- <numbers>
|   |   |   |-- <number> 8
|   |   |   |-- ","
|   |   |   |-- <numbers>
|   |   |   |   |-- <number> 12
|   |   |   |   |-- ","
|   |   |   |   |-- <numbers>
|   |   |   |   |   |-- <number> 4
|   |   |   |   |   |-- ","
|   |   |   |   |   |-- <numbers>
|   |   |   |   |   |-- <number> 10
|   |-- "]"
|-- ","
|-- "calculate"
|-- "the"
|-- "average"
```

# 5. Ambiguity Analysis

- `<numbers>` ::= `<number>` | `<number>` "," `<numbers>`
- Can be right-recursive or left-recursive, creating multiple parse trees for the same list of numbers.
- The parse tree shows that the same sequence of numbers (5, 8) can be grouped differently depending on recursion direction, confirming the BNF grammar is ambiguous.
- Multiple interpretations could affect how a parser processes a list in more complex languages, potentially leading to different evaluation orders or grouping of elements.

**Example Input: 5, 8**  
Parse Tree Option 1 (Right-recursive)
```plaintext
<numbers>
|-- <number> 5
|-- ","
|-- <numbers>
    |-- <number> 8
```
Parse Tree Option 2 (Left-recursive)
```plaintext
<numbers>
|-- <numbers>
|   |-- <number> 5
|-- ","
|-- <number> 8
```

# 6. EBNF Grammar

**We can rewrite the BNF in EBNF to remove ambiguity and improve readability:**

```plaintext
<average-problem> = "Given" <number-list> "," "calculate" "the" "average"

<number-list> = "[" <numbers> "]"

<numbers> = <number> { "," <number> }

<number> = <digit> { <digit> }

<digit> = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

- { ... } denotes zero or more repetitions -> simplifies recursion.
- Easier to read than deeply nested recursive BNF.
- Reduces ambiguity by explicitly showing repetition.

# 7. Parse Tree (EBNF version)

```plaintext
<average-problem>
|-- "Given"
|-- <number-list>
|   |-- "["
|   |-- <numbers>
|   |   |-- <number> 5
|   |   |-- ","
|   |   |-- <number> 8
|   |   |-- ","
|   |   |-- <number> 12
|   |   |-- ","
|   |   |-- <number> 4
|   |   |-- ","
|   |   |-- <number> 10
|   |-- "]"
|-- ","
|-- "calculate"
|-- "the"
|-- "average"
```

- The EBNF parse tree produces a single, clear structure for the input [5, 8, 12, 4, 10].
- `<numbers>` = `<number>` { "," `<number>` } ensures each number after a comma is added sequentially, removing the left- vs right-recursive ambiguity from the BNF.
- In the BNF version, multiple parse trees could be generated for the same list due to recursion.
- The EBNF version is deterministic, making parsing unambiguous and easier to understand.
- Overall, it ensures consistent interpretation of any list of numbers and simplifies further processing.