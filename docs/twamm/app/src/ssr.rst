app/src/ssr.tsx
===============

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import type { ReactElement } from "react";

const isServer = () => typeof window === "undefined";

const BrowserOnly = ({ children }: { children: ReactElement }) =>
  isServer() ? null : children;

export default BrowserOnly;


