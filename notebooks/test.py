from summarize import generate_summary, read_article
import os


import os
cwd = os.getcwd()
sentences = read_article(cwd + "/text.txt")
generate_summary(sentences, 5)
