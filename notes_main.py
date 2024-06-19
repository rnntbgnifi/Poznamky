from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout
import json

app = QApplication([])





#region Aplikacia -  rozhranie - widgety
#application window parameters
notes_win = QWidget()
notes_win.setWindowTitle('Smart Notes')
notes_win.resize(900, 600)


#application window widgets
list_notes = QListWidget()
list_notes_label = QLabel('List of notes')


button_note_create = QPushButton('Create note') #a window appears with the field "Enter note name"
button_note_del = QPushButton('Delete note')
button_note_save = QPushButton('Save note')


field_tag = QLineEdit('')
field_tag.setPlaceholderText('Enter tag...')
field_text = QTextEdit()
button_add = QPushButton('Add to note')
button_del = QPushButton('Untag from note')
button_search = QPushButton('Search notes by tag')
list_tags = QListWidget()
list_tags_label = QLabel('List of tags')


#arranging widgets by layout
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)


col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)


col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_add)
row_3.addWidget(button_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_search)


col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)

#endregion
def add_note():
    note_name, ok = QInputDialog.getText(notes_win, "Add note", "Note name: ")
    if ok and note_name != "":
        notes[note_name] = {"text" : "", "tags" : []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]["tags"])
        print(notes)

def show_note():
    #get the text from the note with the title highlighted and display it in the edit field
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["text"])
    list_tags.clear()
    list_tags.addItems(notes[key]["tags"])

def save_not():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["text"] = field_text.toPlainText()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Note to save is notselected!")

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensurce_ascii=False)
        print(notes)
    else:
        print("Note to delete is not selected")

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]["tags"]:
            notes[key]["tags"].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Note to add a tag is not selected!")
 
def del_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]["tags"].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]["tags"])
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("Tag to delete is not selected!")
 
def search_tag():
    print(button_search.text())
    tag = field_tag.text()
    if button_search.text() == "Search notes by tag" and tag:
        print(tag)
        notes_filtered = {} #notes with the highlighted tag will be here
 
        for note in notes:
            if tag in notes[note]["tags"]: 
                notes_filtered[note]=notes[note]
        button_search.setText("Reset search")
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
        print(button_search.text())
    elif button_search.text() == "Reset search":
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        button_search.setText("Search notes by tag")
        print(button_search.text())
    else:
        pass

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    for note in notes:
        if note[0] == key:
            field_text.setText(note[1])
            list_tags.clear()
            list_tags.sddItems(note[2])
def add_note():
    note_name, ok = QInputDialog.getText(notes_win, "Add note", "Note name: ")
    if ok and note_name != "":
        note = list()
        note = [note_name, "", []]
        notes.append(note)
        list_notes.addItems(note[0])
        list_tags.addItems(note[2])
        print(notes)
        with open(str(len(notes)-1)+".txt", "w") as file:
            file.write(note[0]+"\n")

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        index = 0
        for note in notes:
            if note[0] == key:
                note[1] = field_text.toPlainText()
                with open(str(index)+".txt", "w") as file:
                    file.write(note[0]+"\n")
                    file.write(note[1]+"\n")
                    for tag in note[2]:
                        file.write(tag+" ")
            index += 1
        print(notes)
    else:
        print("Note to save is not selected")



button_note_create.clicked.connect(add_note)
list_notes.itemClicked.connect(show_note)
button_note_save.clicked.connect(save_not)
button_note_del.clicked.connect(del_note)
      
button_add.clicked.connect(add_tag)
button_del.clicked.connect(del_tag)
button_search.clicked.connect(search_tag)


notes_win.show()

name = 0
notes = []
while True:
    filename = str(name)+".txt"
    try:
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                line = line.replace('\n', '')
                note.append(line)
        tags = note[2].split(' ')
        note[2] = tags
 
        notes.append(note)
        note = []
        name += 1
 
    except IOError:
        break



with open("notes_data.json", "r") as file:
    notes = json.load(file)

list_notes.addItems(notes)

app.exec_()