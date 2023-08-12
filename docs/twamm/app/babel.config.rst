app/babel.config.js
===================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: js

    module.exports = function (api) {
  const isServer = api.caller((caller) => caller?.isServer);
  const isCallerDevelopment = api.caller((caller) => caller?.isDev);

  if (
    typeof isServer === "undefined" &&
    typeof isCallerDevelopment === "undefined"
  )
    return {};

  const whyDidYouRender = [
    "next/babel",
    {
      "preset-react": {
        importSource:
          !isServer && isCallerDevelopment
            ? "@welldone-software/why-did-you-render"
            : "react",
      },
    },
  ];

  const presets = [whyDidYouRender];

  return { presets };
};


