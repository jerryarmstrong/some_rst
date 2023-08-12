packages/secure-background/src/store/extensionDB.ts
===================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { BrowserRuntimeCommon } from "@coral-xyz/common";

import type { SecureDB } from "./SecureStore";

export const extensionDB: SecureDB = {
  async get(key: string): Promise<any> {
    return await BrowserRuntimeCommon.getLocalStorage(key);
  },

  async set(key: string, value: any): Promise<void> {
    await BrowserRuntimeCommon.setLocalStorage(key, value);
  },

  async remove(key: string): Promise<void> {
    await BrowserRuntimeCommon.removeLocalStorage(key);
  },

  async reset(): Promise<void> {
    await BrowserRuntimeCommon.clearLocalStorage();
  },
};


