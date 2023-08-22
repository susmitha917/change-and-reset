POST http://127.0.0.1:8000/api/user/register/
{
    "email": "hello@gmail.com",
    "name": "susmitha",
    "password": "susmi@123",
    "password2": "susmi@123",
    "tc": "True"
}
{
    "token": {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MTk0MjA5MywiaWF0IjoxNjkxODU1NjkzLCJqdGkiOiJlMzI4MGU2NGFmNWQ0ODA2YjE4ZGQ0NjQ2ODdmNDg0NSIsInVzZXJfaWQiOjF9.7Z6f0O9ehyvU1FaeTHGTJigSYFd82Aoq8YnTJ0bvPQc",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxODU2ODkzLCJpYXQiOjE2OTE4NTU2OTMsImp0aSI6ImFjYTAzMGM0YWZhZjQ1M2E5MDE2NjM3MDc0YTMzNGRkIiwidXNlcl9pZCI6MX0.FtkgJjHD8WR6BStNVqhUH1C0RkISvSPIGwIbMXVnTRk"
    },
    "msg": "Registration successfully !"
}

http://127.0.0.1:8000/api/user/login/ post
{
    "email":"hello@gmail.com",
    "password":"susmi@123"
}
{
    "token": {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MTk0MjUyOSwiaWF0IjoxNjkxODU2MTI5LCJqdGkiOiJkMzgxZTRjMTU2MWU0NTJkYmQ3NjU0NmE5MWU0NTdlOSIsInVzZXJfaWQiOjF9.fSS8gUU-4O-ccMx8sAHQ7-v0qB2TJALid2rOQSO1Um4",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxODU3MzI5LCJpYXQiOjE2OTE4NTYxMjksImp0aSI6ImVlNjU0NTEwMDk3OTRhN2RiMTY0NmMwY2EzNDRiYTAyIiwidXNlcl9pZCI6MX0.yOvCmGgw0xdWS2tLjEA8uwCdBxjCGzwmu8EXmMVbtMU"
    },
    "msg": "Login success"
}