#Python program to replace multiple words in k
string1 = "Geeksforgeeks is best for geeks and cs"
word_list = ["best", "for", "cs"]
repl_word = "gfg"
for i in word_list:
    string1 = string1.replace(i,repl_word)
print(string1)