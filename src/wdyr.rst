src/wdyr.ts
===========

Last edited: 2021-03-16 20:45:52

Contents:

.. code-block:: ts

    import React from "react";

if (process.env.NODE_ENV === "development") {
  const whyDidYouRender = require("@welldone-software/why-did-you-render");
  whyDidYouRender(React, {
    trackAllPureComponents: true,
  });
}


