app/utils/local-storage.ts
==========================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: ts

    let localStorageIsAvailableDecision: boolean | undefined;
export function localStorageIsAvailable() {
  if (localStorageIsAvailableDecision === undefined) {
    const test = 'test';
    try {
      localStorage.setItem(test, test);
      localStorage.removeItem(test);
      localStorageIsAvailableDecision = true;
    } catch (e) {
      localStorageIsAvailableDecision = false;
    }
  }
  return localStorageIsAvailableDecision;
}

