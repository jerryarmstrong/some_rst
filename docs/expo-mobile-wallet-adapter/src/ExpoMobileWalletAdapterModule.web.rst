src/ExpoMobileWalletAdapterModule.web.ts
========================================

Last edited: 2023-03-28 15:16:55

Contents:

.. code-block:: ts

    import { EventEmitter } from 'expo-modules-core';

const emitter = new EventEmitter({} as any);

export default {
  PI: Math.PI,
  async setValueAsync(value: string): Promise<void> {
    emitter.emit('onChange', { value });
  },
  hello() {
    return 'Hello world! 👋';
  },
};


