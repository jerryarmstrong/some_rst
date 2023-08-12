packages/app-extension/jest.config.js
=====================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: js

    module.exports = {
  preset: "jest-puppeteer",
  moduleNameMapper: {
    "^react-native$": "react-native-web",
  },
  transform: {
    "^.+\\.[jt]sx?$": ["esbuild-jest"],
  },
  setupFilesAfterEnv: ["./jest.setup.js"],
  transformIgnorePatterns: ["node_modules/(?!uuid/)"],
};


