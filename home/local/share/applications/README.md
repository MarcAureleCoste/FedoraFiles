# XDG 

Desktop files are used to determine witch application must be used to open a URL or a file.

For example in the file `code-url-handler.desktop` the line `MimeType=` explain that URL(s) starting
with **vscode://** must be opened with vscode.

These file are generaly included with the RPM packages but with electron app that most of the time are just
archive creating desktop file can be usefull to manage these urls.