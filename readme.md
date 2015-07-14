# thesis_bubble
Creates a bubble display of the keywords in my PhD thesis using Python and Javascript

thesis_pdf.txt: Copy paste of my thesis, directly from the pdf file

read_thesis.py: Imports "thesis_pdf.txt" and returns "thesis.json", that contains a dictionnary with all words and their number of occurences.

thesis.json: Output of "read_thesis.py"

thesis_bubbles.html: Takes "thesis.json" in entry and plots the bubbles using d3.js
