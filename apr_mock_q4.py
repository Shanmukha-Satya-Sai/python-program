"""Description:
Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k.

Now Bob will ask Alice to perform the following operation forever:

Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

Print the value of the kth character in word, after enough operations have been done for word to have at least k characters.

Note:  That the character 'z' can be changed to 'a' in the operation.

Input:  First line of input consists of one integer value which represetns

Output: Print the kth character after enough games


Constraints:
Constraints:

k value must be greater than zero and less than 500 otherwise print "INVALID INPUT"


Example:
Input 1 :  5
Output 1 : b
Input 2 :  10
Output 2 : c
Explanation:
Input 1 : k = 5
Output 1 : b
Explanation:
Initially, word = "a". We need to do the operation three times:
Generated string is "b", word becomes "ab".
Generated string is "bc", word becomes "abbc".
Generated string is "bccd", word becomes "abbcbccd".
Input 2 : k = 10
Output 2 : c
Explanation:
Initially, word = "a". We need to do the operation four times:
Generated string is "b", word becomes "ab".
Generated string is "bc", word becomes "abbc".
Generated string is "bccd", word becomes "abbcbccd".
Generated string is "abbcbccd", word becomes "abbcbccdbccdcdde".