Django Q Email Changelog
------------------------


#### Version 5.0.0 (2019-11-28)

- Enqueue human-readable objects by default instead of pickled objects (set `DJANGO_Q_EMAIL_USE_DICTS` to `False` to disable)


#### Version 4.1.0 (2019-08-11)

- Import `EMAIL_ERROR_HANDLER` instead of calling it directly


### Version 4.0.0 (2019-07-25)

- Add `DJANGO_Q_EMAIL_ERROR_HANDLER` to handle errors


### Version 3.0.0 (2019-05-26)

- **Python 3.7+ support**

- Fix installation steps in README


### Version 2.0.0 (2018-09-04)

- **Django Q 1.0+ support**

- Fix typo in README ([#1](https://github.com/joeyespo/django-q-email/pull/1) - thanks, [@ankitch][]!)


### Version 1.0.0 (2017-02-09)

- First public release


[@ankitch]: https://github.com/ankitch
