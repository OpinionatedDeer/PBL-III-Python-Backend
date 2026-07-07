# A Backend
----
This is a basic python based backend designed to support real-time intercommuniation
----
## Capabilities
- Role based system (Admin, Teacher, Student).
- Robust security measures using Javascript Web Token to verify user and their permission before every request.
- Expandable BitMask based per user per channel permission system.
- Real time deletion, edition of messages.
- Complete logging of all changes on messages 
- Support for file upload

## Setup [Backend]
1. Setup PostGreSQL on same or different machine https://www.postgresql.org/
2. Create a virtual environment of python using 'python3 -m venv venv'
3. Activate virtual environment 'source venv/bin/activate'
4. Run 'pip install -r requirements.txt'
5. edit .env file 
6. Run the server 'python3 server.py'

## Compatible Frontend
[Frontend](https://github.com/KartikaySrivastava258/PBL-PYTHON-FRONTEND-MAIN)
- By [KartikaySrivastava258](https://github.com/KartikaySrivastava258)
