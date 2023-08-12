packages/chat-sdk/src/utils/open.ts
===================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    export const openWindow = (url: string, target: string) => {
  const newWindow = window.open(url, target);
  if (newWindow) {
    newWindow.opener = null;
  }
};


