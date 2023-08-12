examples/xnft/explorer/src/index.tsx
====================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import React from "react";
import ReactXnft, { AnchorDom } from "react-xnft";
import { App } from "./App/App";
import { RecoilRoot } from "recoil";

ReactXnft.render(
  <AnchorDom>
    <RecoilRoot>
      <App />
    </RecoilRoot>
  </AnchorDom>
);


