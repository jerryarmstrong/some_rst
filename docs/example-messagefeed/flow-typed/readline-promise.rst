flow-typed/readline-promise.js
==============================

Last edited: 2020-06-24 17:49:11

Contents:

.. code-block:: js

    declare module 'readline-promise' {

  declare class ReadLine {
    questionAsync(prompt: string): Promise<string>;
    write(text: string): void;
  }

  declare module.exports: {
    createInterface({
      input: Object,
      output: Object,
      terminal: boolean
    }): ReadLine;
  }
}


