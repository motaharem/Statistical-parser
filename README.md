# Statistical-parser
implementation of the CYK statistical parser using the rules are extracting from a treebank .

In natural language processing we have several ways to pars a given sentence. The state-of-the-art methods parsing sentence are statistical ones.
CYK is one of the most popular parsers in NLP. Anyway, in this project I had a train set which was a treebank being a set of pars trees.
Since, CYK uses the rules with their probability in parsing sentence, I first extract the rule and assign each of them their probability.
After all, I implemented CYK algorithm. As a result, given a text in english my project is able to pars all of the sentence and write their pars tree in a text file.
