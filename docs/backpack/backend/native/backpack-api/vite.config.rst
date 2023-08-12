backend/native/backpack-api/vite.config.ts
==========================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    setupFiles: ["./src/routes/v1/__tests__/_setup.ts"],
    threads: false,
  },
});


