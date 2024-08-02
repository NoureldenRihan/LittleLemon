API endpoints to test
/api/menu/ ["GET"]
/api/bookings/ ["GET", "POST", "DELETE"]

POST calls to /api/bookings body in json format example:
{
    "first_name": "Perseon",
    "reservation_date": "2024-08-02",
    "reservation_slot": 5
}

DELETE calls to /api/bookings body in json format example:
{
    "id": 5
}

to run a unit test run "python manage.py test"

superuser credentials
    username: superuser
    email: super@user.com
    password: user1234
    Auth Token: 77688f0cbd89e4bcf79922919952473fb59fcd96