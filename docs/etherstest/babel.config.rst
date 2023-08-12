babel.config.js
===============

Last edited: 2023-07-23 17:13:40

Contents:

.. code-block:: js

    module.exports = function (api) {
  api.cache(true);
  return {
    presets: ["babel-preset-expo"],
    plugins: [
      // https://github.com/facebook/react-native/issues/36828#issuecomment-1589462227
      "@babel/plugin-transform-flow-strip-types",
      // needed for ethers6
      ["@babel/plugin-proposal-private-methods", { loose: true }],
      [
        "module-resolver",
        {
          alias: {
            crypto: "react-native-quick-crypto",
            stream: "stream-browserify",
            'bn.js': 'react-native-bignumber',
            buffer: "@craftzdog/react-native-buffer",
          },
        },
      ],
    ],
  };
};


