Notes Summarizer

Motivation:
When in class, I often write long, messy notes that are hard to understand later.
I wanted a simple tool to quickly condense and clarify my notes so I can review them more effectively.
This app was created to solve that problem by providing easy text summarization with export options and a clean interface.

Overview:
This is a desktop application designed to help students and note-takers summarize long text inputs into concise summaries.
Users can type or paste their notes into the input box, generate a summary, and export the result as either a PDF or a text file.
The app features a simple GUI built with CustomTkinter and supports light/dark mode toggling.

Features:
Input text box for entering notes.
Summarization powered by Hugging Face’s facebook/bart-large-cnn model.
Autocorrection applied to the summarized text using the autocorrect library.
Export summaries as PDF or plain text files.
Switch between dark and light themes.

Usage:
Enter your notes in the main text box.
Click the "Summarize" button to generate a summary in a new window.
Choose to export the summary as a PDF or text file via the dropdown menu.
Access the settings via the gear icon to toggle between light and dark modes.

Notes
The summarization model (facebook/bart-large-cnn) may require a relatively powerful computer to run smoothly.
If you experience performance issues, modify this line to use a smaller Hugging Face summarization model: ("summarization", model="facebook/bart-large-cnn").
