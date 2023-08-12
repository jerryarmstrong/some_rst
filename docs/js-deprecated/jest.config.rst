jest.config.ts
==============

Last edited: 2022-06-14 09:19:26

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


