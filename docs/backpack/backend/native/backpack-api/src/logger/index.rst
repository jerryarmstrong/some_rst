backend/native/backpack-api/src/logger/index.ts
===============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    class Logger {
  private constructor() {}

  static getInstance() {
    return new Logger();
  }

  log(message: string) {
    console.log(message);
  }

  error(message: string) {
    console.error(message);
  }

  warn(message: string) {
    console.warn(message);
  }
}

export const logger = Logger.getInstance();


