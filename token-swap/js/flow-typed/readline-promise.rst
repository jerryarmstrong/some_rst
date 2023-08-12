token-swap/js/flow-typed/readline-promise.js
============================================

Last edited: 2020-08-26 08:56:56

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


