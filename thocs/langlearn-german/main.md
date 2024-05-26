Language Learning Toolbox
===========================================================
First 





The Toolbox
===========================================================
- Anki
  * Cutomizing cards
  * CSV
  * Python scripting
- OCRed book 
  * Please read this post [how-to-ocr-linux]
  * pdfgrep REGEX document
- A Thesaurus Zertificat. It is mentionen in this pages in the verbe overview [here](https://www.verbformen.com/?w=wegmachen)
- LibreOffice and styles


`pdfgrep`
===========================================================
This command will let you to search efficiently through eny PDF file.
```sh
pdfgrep -n 'kauf[[:alpha:][:punct:][:space:]]{,20}ein' completebook.ocr.pdf
```

This command will search for any line of text that contains the word `kauf` and the ending `ein`. This is util for example to search examples where the verb `einkaufen` is used.
Since this two parameters can be tedious, here is an function in bash script that let you call that command with customized parameters:
```sh
#!/bin/bash
# $1 filename 
# $2 the space between word1 and word2
# $3 word1
# $4 word2
pdfsearch() 
{
 # How quoting works
 # https://www.gnu.org/software/bash/manual/bash.html#Double-Quotes
 COMMAND="pdfgrep -n ' $3[[:alpha:][:punct:][:space:]]{,$2}$4' $1"
 echo $COMMAND
 eval $COMMAND
}

alias pdfs=pdfsearch
```
Copy and past into your terminal, then call as `pdfs completebook.ocr.pdf 40 ka ein`, it is also recomendable to switch the words i.e. `pdfs completebook.ocr.pdf 40 mit disk`, because of the following result:
```
Ich möchte das mit meinen Kollegen diskutieren.
```
Here you see that `mit` appears before the root verb `disk`.

. This will search the book for that workd as it where a separable verb.

Phrase Mining
===========================================================
I made data mining in my quest for phrase examples in the folowing files
- Book: completebook.ocr.pdfgrep
- Goethe-Zertifikat_A2_Wortliste_1300_Worte.pdf
- Wiktionary
- Leo Dictonary





