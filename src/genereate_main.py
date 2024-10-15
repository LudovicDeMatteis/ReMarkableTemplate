import numpy as np

def write_header(filename):
    content = r"""
\documentclass[11pt]{article}

\usepackage[utf8]{inputenc}

\input{Imports/librairies.tex}
\input{Imports/commands.tex}
\input{Imports/notations.tex}
\input{Imports/operators.tex}
\usepackage{forloop}
\usepackage{fmtcount}
\usepackage{array}

\DeclareFontFamily{U}{matha}{\hyphenchar\font45}
\DeclareFontShape{U}{matha}{m}{n}{
<5>matha5<6>matha6<7>matha7<8>matha8<9>matha9
<10><10.95>matha10
<12><14.4><17.28><20.74><24.88>matha12
}{}
\DeclareSymbolFont{matha}{U}{matha}{m}{n}
\DeclareFontSubstitution{U}{matha}{m}{n}
\DeclareMathSymbol{\ovoid}{\mathbin}{matha}{"6C}

\title{Latex project template}
\author{Ludovic De Matteis - Initial project by Côme Perrot}
\date{}

\begin{document}
\pagenumbering{gobble}
\newcounter{hour}
\newcounter{counter}
\newcommand{\jumpsize}{0.45cm}
\newcommand{\dotspaces}{0.4cm}
    """
    with open(filename, 'a') as file:
        file.write(content)

def write_title(filename, day, month, year, date):
    content = r"""
\Huge{\bf{ """ + day + ' ' + str(date) + ' ' + month + ' ' + str(year) + r"""}} \hfill \normalsize{Mood: $\ovoid$ $\ovoid$ $\ovoid$ $\ovoid$ $\ovoid$}\\
    """
    with open(filename, 'a') as file:
        file.write(content)

def write_core(filename):
    content = r"""
\vspace{0.3cm}
\begin{center}
    \huge{\underline{To Do List}}\\[0.5cm]
    $\square$ \dotfill\\[\dotspaces]
    $\square$ \dotfill\\[\dotspaces]
    $\square$ \dotfill\\[\dotspaces]
    $\square$ \dotfill\\[\dotspaces]
    $\square$ \dotfill\\[\dotspaces]
    $\square$ \dotfill\\[\dotspaces]
\end{center}

\vspace{0.5cm}
\begin{minipage}{0.5\textwidth}
    \begin{center}
        \huge{\underline{Notes}}\\[0.5cm]
        \dotfill\\[\dotspaces]
        \dotfill\\[\dotspaces]
        \dotfill\\[\dotspaces]
        \dotfill\\[\dotspaces]
        \dotfill\\[\dotspaces]
        \dotfill\\[\dotspaces]
        \dotfill\\[\dotspaces]
        \dotfill\\[\dotspaces]
        \dotfill\\[\dotspaces]
        \dotfill\\[\dotspaces]
        \dotfill\\[\dotspaces]
    \end{center}
\end{minipage}
\begin{minipage}{0.5\textwidth}
    \begin{center}
        \huge{\underline{Planning}}\\[0.7cm]
        \normalsize
        \newcolumntype{Y}{>{\raggedright\arraybackslash}X}
        \begin{tabularx}{0.9\textwidth}{|m{1cm}|Y|}
            \hline
            \multirow{2}{=}{07h} & \\[\jumpsize] \cdashline{2-2}
            \forloop{hour}{8}{\value{hour}<20}{
                \multirow{2}{*}{\padzeroes[2]\decimal{hour}h} & \\[\jumpsize] \cdashline{2-2}
            }
            \multirow{2}{*}{\padzeroes[2]\decimal{hour}h} & \\[\jumpsize] \cdashline{2-2}
                &  \\ \hline
        \end{tabularx}
    \end{center}
\end{minipage}
\newpage
    """
    with open(filename, 'a') as file:
        file.write(content)

def write_footer(filename):
    content = r"""
\end{document}
    """
    with open(filename, 'a') as file:
        file.write(content)

write_header('/home/ldematteis/TexProjects/ReMarkableTemplate/src/main.tex')
# write_title('/home/ldematteis/TexProjects/ReMarkableTemplate/src/main.tex', 'Mardi', 'Octobre ', 2024, 15)
# write_core('/home/ldematteis/TexProjects/ReMarkableTemplate/src/main.tex')

days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
n_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = 2024
start_date = 15

current_day_index = days.index('Mardi')
current_month_index = 9  # October is the 10th month, index 9
current_date = start_date

for _ in range(90):  # Loop for the whole year
    day = days[current_day_index % len(days)]
    date = current_date
    month = months[current_month_index]
    
    write_title('/home/ldematteis/TexProjects/ReMarkableTemplate/src/main.tex', day, month, year, date)
    write_core('/home/ldematteis/TexProjects/ReMarkableTemplate/src/main.tex')
    
    current_day_index += 1
    current_date += 1
    
    # Check if we need to move to the next month
    if current_date > n_days[current_month_index]:
        current_date = 1
        current_month_index += 1
        
        # Check if we need to move to the next year
        if current_month_index >= len(months):
            current_month_index = 0
            year += 1

write_footer('/home/ldematteis/TexProjects/ReMarkableTemplate/src/main.tex')