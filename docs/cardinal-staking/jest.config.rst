jest.config.js
==============

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: js

    module.exports = {
  clearMocks: true,
  moduleFileExtensions: ["js", "ts"],
  testMatch: ["**/*.test.ts"],
  transform: {
    "^.+\\.ts$": "ts-jest",
  },
  testTimeout: 10000,
  verbose: true,
  reporters: [
    "default",
    ["jest-junit", { outputDirectory: "tests", outputName: "out.xml" }],
    "github-actions",
  ],
};


