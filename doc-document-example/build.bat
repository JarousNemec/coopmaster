@echo off
REM Skript pro kompilaci LaTeXového dokumentu s bibliografií a glosářem
REM s výstupem do složky "out" umístěné o úroveň výš než dokument.tex

REM Nastavení názvu dokumentu bez přípony .tex
set DOCUMENT_NAME=document

REM Nastavení výstupní složky (o úroveň výš než aktuální složka)
set OUTPUT_DIR=..\out

echo Spouštím kompilaci %DOCUMENT_NAME%.tex s výstupem do %OUTPUT_DIR%

REM Vytvoření výstupní složky, pokud neexistuje
if not exist "%OUTPUT_DIR%" (
    mkdir "%OUTPUT_DIR%"
)

REM Krok 1: Kompilace LaTeX dokumentu s nastavením výstupní složky
pdflatex -interaction=nonstopmode -shell-escape -output-directory="%OUTPUT_DIR%" "%DOCUMENT_NAME%.tex"

REM Kontrola, zda kompilace proběhla úspěšně
if errorlevel 1 (
    echo Chyba při kompilaci LaTeXu. Zkontrolujte log soubory.
    pause
    exit /b 1
)

REM Krok 2: Generování bibliografie
REM Pokud používáte Biber:
biber --input-directory="%OUTPUT_DIR%" --output-directory="%OUTPUT_DIR%" "%DOCUMENT_NAME%"
REM Pokud používáte BibTeX, místo toho použijte:
REM bibtex "%OUTPUT_DIR%\%DOCUMENT_NAME%"

REM Kontrola, zda biber/bibtex proběhl úspěšně
if errorlevel 1 (
    echo Chyba při generování bibliografie. Zkontrolujte log soubory.
    pause
    exit /b 1
)

REM Krok 3: Generování glosáře
makeglossaries -d "%OUTPUT_DIR%" "%DOCUMENT_NAME%"

REM Kontrola, zda makeglossaries proběhl úspěšně
if errorlevel 1 (
    echo Chyba při generování glosáře. Zkontrolujte log soubory.
    pause
    exit /b 1
)

REM Krok 4: Opětovná kompilace LaTeXu pro zahrnutí bibliografie a glosáře
pdflatex -interaction=nonstopmode -shell-escape -output-directory="%OUTPUT_DIR%" "%DOCUMENT_NAME%.tex"
pdflatex -interaction=nonstopmode -shell-escape -output-directory="%OUTPUT_DIR%" "%DOCUMENT_NAME%.tex"

echo Kompilace %DOCUMENT_NAME%.tex dokončena úspěšně! Výstupní soubory jsou ve složce %OUTPUT_DIR%
exit /b 0