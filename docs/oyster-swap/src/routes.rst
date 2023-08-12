src/routes.tsx
==============

Last edited: 2020-11-17 14:49:57

Contents:

.. code-block:: tsx

    import { HashRouter, Route } from "react-router-dom";
import React from "react";
import { ExchangeView } from "./components/exchange";

export function Routes() {
  // TODO: add simple view for sharing ...
  return (
    <>
      <HashRouter basename={"/"}>
        <Route exact path="/" component={ExchangeView} />
      </HashRouter>
    </>
  );
}


