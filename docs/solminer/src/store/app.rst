src/store/app.js
================

Last edited: 2020-07-22 13:30:11

Contents:

.. code-block:: js

    import LocalStore from 'electron-store';
import { reaction, action, observable } from 'mobx';
import i18n from '../i18n';

const localStore = new LocalStore();

class AppStore {
  constructor() {
    reaction(
      () => this.locale,
      locale => {
        i18n.changeLanguage(locale);
      }
    );
  }

  @observable depositPublicKey = localStore.get('depositPublicKey', '');

  @observable screen = 'whatYouNeed';

  @observable alertType = '';

  @observable locale = 'en';

  @observable secretKey = '';

  @observable gb = [20];

  @observable state = 'disabled';

  @action.bound
  setScreen(screen) {
    this.screen = screen;
  }

  @action.bound
  showAlert(alertType) {
    this.alertType = alertType;
  }

  @action.bound
  hideAlert() {
    this.alertType = null;
  }

  @action.bound
  switchLanguage(locale) {
    this.locale = locale;
    localStore.set('locale', locale);
  }

  @action.bound
  setSecretKey(secretKey) {
    this.secretKey = secretKey;
  }

  @action.bound
  setGB(gb) {
    this.gb = gb;
  }

  @action.bound
  setDepositPublicKey(key) {
    this.depositPublicKey = key;
  }

  @action.bound
  setState(state) {
    this.state = state;
  }
}

const store = new AppStore();

store.switchLanguage(localStore.get('locale') || 'en');

export default store;


