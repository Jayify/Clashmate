# Publishing Python Projects

Summarised from: [Convert Python Files To EXE using PyInstaller | PyGame Tutorial by Coding With Russ](https://www.youtube.com/watch?v=2X9rxzZbYqg).

# Installing PyInstaller

1. Open the Command Prompt.
2. Run `pip install PyInstaller`.
3. Wait for successful install.
4. Note: I had to delete all old versions of python and reinstall the current one.

# Publishing Project

1. Copy the project into a location of your choosing to avoid accidental modification or deletion of the main project.
2. In VS Code, 'Reveal in File Explorer' on any file in the top level of the project.
3. In the File Explorer path bar, replace the current path with 'cmd' and press enter. The Command Prompt should now be open, and at the path of the project.
4. Run the command `pyinstaller <filename>.py --onefile --windowed`, where <filename> is the main file of the project.
5. Move the .exe file from the dist folder into the root folder.
6. Delete ALL unwanted files (i.e. script modules, dist and build folder, unnecessary markdown/text files, etc.). Ensure to keep any separate referenced files, such as database or media files, as well as the executable.

# Running the Executable

1. Open the executable location in File Explorer.
2. If available: right-click the executable open with Command Prompt.
3. Else, in the File Explorer path bar, replace the current path with 'cmd' and press enter. The Command Prompt should now be open, and at the path of the executable.
4. Run `<filename>.exe`, where <filename> is the name of the executable.