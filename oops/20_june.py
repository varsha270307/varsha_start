class NoteManager:
    def __init__(self, filename):
        self.filename = filename

    def write_note(self, content):
        try:
            with open(self.filename, 'w') as file:
                file.write(content + '\n')
            print("Note written successfully.")
        except Exception as e:
            print("Error writing note:", e)

    def append_note(self, content):
        try:
            with open(self.filename, 'a') as file:
                file.write(content + '\n')
            print("Note appended successfully.")
        except Exception as e:
            print("Error appending note:", e)

    def read_notes(self):
        try:
            with open(self.filename, 'r') as file:
                print("\n--- Your Notes ---")
                print(file.read())
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
        except Exception as e:
            print("Error reading notes:", e)

# -------------------------
# Usage Example
# -------------------------

note_app = NoteManager("notes.txt")

note_app.write_note("This is my first note.")
note_app.append_note("This is an additional thought.")
note_app.read_notes()



import os

class NoteManager:
    def __init__(self, filename):
        self.filename = filename

    def write_note(self, content):
        try:
            with open(self.filename, 'w') as file:
                file.write(content + '\n')
            print("Note written successfully.")
        except Exception as e:
            print("Error writing note:", e)

    def append_note(self, content):
        try:
            with open(self.filename, 'a') as file:
                file.write(content + '\n')
            print("Note appended successfully.")
        except Exception as e:
            print("Error appending note:", e)

    def read_notes(self):
        if not os.path.exists(self.filename):
            print(f"File '{self.filename}' not found.")
            return
        try:
            with open(self.filename, 'r') as file:
                print("\n--- Your Notes ---")
                print(file.read())
        except Exception as e:
            print("Error reading notes:", e)

    def delete_notes(self):
        if os.path.exists(self.filename):
            try:
                os.remove(self.filename)
                print(f"File '{self.filename}' deleted successfully.")
            except Exception as e:
                print("Error deleting file:", e)
        else:
            print(f"File '{self.filename}' does not exist.")

# -------------------------
# Usage Example
# -------------------------

note_app = NoteManager("notes.txt")

note_app.write_note("This is my first note.")
note_app.append_note("This is a follow-up note.")
note_app.read_notes()
note_app.delete_notes()
note_app.read_notes()


