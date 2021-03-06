# Cinema-System
## Introduction
A cinema system design that builds on Django 3.1.1.  
Adding movies (data to the database) is done via admin site.
In order to reserve a seat in the cinema, the user must complete the form and select the seat. If successful, an email will be sent.
### Database
Sqlite3
#### Model
![My app model](myapp_models.png)
## Example images
### main window
![Main window](main.png)
### Repertoire window
![Repertoire window](repertoire.png)
### Reservation window
![Reservation window](reservation.png)
## Comments
* You only can "buy" one ticket.
* You need to set up an email in views.py and configure smtp in settings.py
* <span style="color:red">**This is an apllication here not project**</span>.
## References
https://docs.djangoproject.com/en/3.1/  
https://github.com/lmirkowski/Projekt-KINO-mysql/blob/master/kino_erd.pdf
