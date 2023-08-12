app/src/swr-cache.ts
====================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: ts

    import type { Cache } from "swr";

export function localStorageProvider(storage: Cache) {
  if (!globalThis.localStorage) return storage ?? new Map([]);

  const map = new Map<any, any>(
    JSON.parse(globalThis.localStorage?.getItem("app-cache") || "[]")
  );

  globalThis?.addEventListener("beforeunload", () => {
    const appCache = JSON.stringify(Array.from(map.entries()));
    globalThis.localStorage.setItem("app-cache", appCache);
  });

  return map;
}


