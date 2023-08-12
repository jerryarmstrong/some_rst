src/updater.js
==============

Last edited: 2020-07-22 13:30:11

Contents:

.. code-block:: js

    import { autoUpdater } from 'electron';
import updateElectronApp from 'update-electron-app';
import log from 'electron-log';

try {
  updateElectronApp({
    logger: log,
    notifyUser: false,
  });
} catch (err) {
  log.error(`Unable to enable updates: ${err}`);
}

// Replace the updateElectronApp handler with our own that updates immediately.
autoUpdater.on('update-downloaded', (...args) => {
  log.info('update-downloaded:', args);
  autoUpdater.quitAndInstall();
});


