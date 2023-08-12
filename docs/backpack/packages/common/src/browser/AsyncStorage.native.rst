packages/common/src/browser/AsyncStorage.native.ts
==================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import RNAsyncStorage from "@react-native-async-storage/async-storage";

const AsyncStorage = {
  getItem: (key: string) => RNAsyncStorage.getItem(key),
  setItem: (key: string, value: any) => RNAsyncStorage.setItem(key, value),
  removeItem: (key: string) => RNAsyncStorage.removeItem(key),
  clear: () => RNAsyncStorage.clear(),
};

export default AsyncStorage;


