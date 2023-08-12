src/i18n/LanguageDetector.js
============================

Last edited: 2020-07-22 13:30:11

Contents:

.. code-block:: js

    import { app, remote } from 'electron';

export default {
  init: Function.prototype,
  type: 'languageDetector',
  detect: () => (app || remote.app).getLocale().split('-')[0],
  cacheUserLanguage: Function.prototype,
};


