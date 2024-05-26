#!/bin/bash
pdfsearch() 
{
 # How quoting works
 # https://www.gnu.org/software/bash/manual/bash.html#Double-Quotes
 COMMAND="pdfgrep -n '$2[[:alpha:][:punct:][:space:]]{,20}$3' $1"
 echo $COMMAND
 echo 31
 eval $COMMAND
}

alias pdfs=pdfsearch
pdfs completebook.ocr.pdf ka ein
