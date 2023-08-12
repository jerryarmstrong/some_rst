flow-typed/readline-promise.js
==============================

Last edited: 2020-07-29 22:45:43

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


