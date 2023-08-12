app/src/emotion-cache.ts
========================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: ts

    import createCache from "@emotion/cache";

// prepend: true moves MUI styles to the top of the <head> so they're loaded first.
// It allows developers to easily override MUI styles with other styling solutions, like CSS modules.
export default function createEmotionCache() {
  return createCache({ key: "css", prepend: true });
}


