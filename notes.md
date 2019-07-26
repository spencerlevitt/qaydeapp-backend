accounts app
 --> users have friends
  --> many to many relationship with itself

models
    - user
        >id
        >name
        >email
    - friend request
        >id
        >from_user
        >to_user
        >timestamp (expiry date?)


JWT auth: https://medium.com/@dakota.lillie/django-react-jwt-authentication-5015ee00ef9a

https://github.com/andyalam/django_instagram

https://www.youtube.com/watch?v=IXJ46DitsIg&index=55&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj

https://briancaffey.github.io/2017/07/19/different-ways-to-build-friend-models-in-django.html