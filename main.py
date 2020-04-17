from docx import Document
import gui
import os


# Function for replacing the words
def find_replace(paragraph_keyword, draft_keyword, paragraph):
    if paragraph_keyword in paragraph.text:
        paragraph.text = paragraph.text.replace(paragraph_keyword, draft_keyword)


# Function which invokes replacing the words. Gets executed when the button 'Apstiprinat' is pressed
def replace_words():
    # Get string entered from the user
    def get_entry_from():
        global entry_from
        entry_from = gui.e1.get()

    # Get string enered from the user
    def get_entry_to():
        global entry_to
        entry_to = gui.e2.get()

    get_entry_from()
    get_entry_to()

    # Get all .docx files in directory
    for file in os.listdir():
        if file.endswith(".docx"):
            document = Document(file)
            for paragraph in document.paragraphs:
                find_replace(entry_from, entry_to, paragraph)
                document.save(file)


