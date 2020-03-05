Greetings
---------

Instructions for Linux/MacOS.

Setup:
------
1. Install MySQL; Note down root user password

2. Start MySQL Server

3. Login to MySQL Server and create a database
   - mysql
   - create database greetings_db;

4. Set environment variables on the shell
   export DB=greetings_db
   export USER=root
   export PASSWORD=<root-user-password>
   export HOST=localhost


Run application:
----------------
1. Create VirtualEnv
   python3.8 -m venv venv

2. Activate VirtualEnv
   . venv/bin/activate

3. Install Python libraries and dependencies
   pip install -r requirements.txt

4. Start application
   python application.py

5. Access the application in browser
   http://localhost:5000/

   This should show the application form
   -> Enter some message in the text box.
   -> It should show up in the form.

The application creates table named 'greetings'
inside the database which you specified via 
the DB environment variable.


Verify:
-------
1. Login to MySQL Server

   $ mysql --user=root --password=<root-password> --host=localhost

   mysql>show databases;
   mysql>use greetings_db;
   mysql>show tables;
   mysql>describe greetings;
   mysql>select * from greetings;  
         --> Verify that the message that you added is in the table.
