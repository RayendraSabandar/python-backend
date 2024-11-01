# python-backend

1. create .env file
    ```
    touch .env
    ```
2. copy envs from example.env file
3. use the env values as stated in the email
4. create a virtual env using this code
    ```
    python -m venv .venv
    ```
5. activate the virtual env
    ```
    source .venv/bin/activate
    ```
6. use the .env file for this application
    ```
    source .env
    ```
7. install the necessary modules/packages
    ```
    pip install -r requirements.txt
    ```
8. Check for database migration history
    ```
    flask db history
    ```
9. Make sure you have created a new db in postgres db (Dbeaver)
10. Migrate
    ```
    flask db upgrade
    ```
11. run the app
    ```
    python app.py
    ```
12. run test using
    ```
    python -m pytest
    ```
13. Import env and collection for postman from `docs` directory
14. Run the endpoint from postman collections