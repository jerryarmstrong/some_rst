src/i18n/index.js
=================

Last edited: 2020-07-22 13:30:11

Contents:

.. code-block:: js

    import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from './LanguageDetector';

import en from './en.json';
import ru from './ru.json';

i18n
  .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    fallbackLng: 'en',
    debug: true,
    defaultNS: 'common',
    whitelist: ['en', 'ru'],
    resources: {
      en: { common: en },
      ru: { common: ru },
    },
    react: {
      wait: false,
      bindI18n: 'languageChanged loaded',
      bindStore: 'added removed',
      nsMode: 'default',
    },
  });
export default i18n;


