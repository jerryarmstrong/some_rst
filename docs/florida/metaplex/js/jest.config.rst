metaplex/js/jest.config.ts
==========================

Last edited: 2022-10-11 23:41:10

Contents:

.. code-block:: ts

    export default {
  preset: 'ts-jest',
  testEnvironment: 'node',
  testMatch: ['**/*.(spec|test).ts'],
  testPathIgnorePatterns: ['rust'],
  globals: {
    'ts-jest': {
      tsconfig: './tsconfig.json',
      diagnostics: false,
    },
  },
};


