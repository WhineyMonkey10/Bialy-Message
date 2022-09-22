# Message Engine
A ´simple´ messaging engine using mainly ReplIT databases to run.

The way this engine works is when you send a message through your client, it will add a 'key' to the ReplIT database with your message. Then, through a constant loop other clients will be continuously looking for changes in the the database. Once one it is detected, it will take the database message and locally store it. Then, it will display this message in the user's CLI. One flaw with this system is that if a message is sent at the exact same time it will conflict with the other message and one will be voided.

Using Python, ReplIT databases and maybe Flask, HTML & CSS
