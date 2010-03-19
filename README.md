Django Email Preview
===================

This is a small app to aid in the development, if you do not have a working email setup.

Using a custom EmailBackend, emails are persisted to the database, where they can be viewed on the admin interface.
The admin change_form will render the email as HTML.

Setup
-----

Quick and dirty how to:

* Add 'emailreader' to your INSTALLED_APPS.
* Change the email backend to point to  'emailreder.dbbackend.EmailBackend'
* Run syncdb to crete the email table.
* Symlink 'emailreader/media' to your [MEDIA_ROOT]/emailreader/

And you are ready to go.
