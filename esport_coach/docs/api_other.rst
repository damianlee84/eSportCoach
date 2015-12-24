=========================
API & Other Configuration
=========================

API
###

**steamOpenID** <https://steamcommunity.com/dev>
  - Valve provides these APIs so website developers can use data from Steam
    in new and interesting ways. They allow developers to query Steam for
    information that they can present on their own sites. At the moment the
    only APIs we offer provide item data for Team Fortress 2, but this list
    will grow over time.

  - Bad thing about this API is Valve don't allow developer to grab match-making
    ranking(MMR) because of privacy term. And there is no other API out there at the
    moment to get the ranking information.

  - There one other API that allow developer to grab information from steam, but
    due to high volume of usage and the owner of the API stop distributing the API.

**Stripe** <https://stripe.com/docs/api>
  - Stripe API provide developer to integrate stripe payment method into their application.

------

Database
########

**Postgres**

PostgreSQL is a powerful, open source object-relational database system. It is
fully compatible with Django. The main reason Postgres was used in this project
is because the database is store in the cloud instead of a local copy like MySQL
did. It make our team access the database with ease, and very convenient.
