ui/src/pages/trade/index.tsx
============================

Last edited: 2023-08-09 02:22:59

Contents:

.. code-block:: tsx

    import React, { useEffect } from "react";
import Router from "next/router";

const IndexPage = () => {
  useEffect(() => {
    const { pathname } = Router;
    if (pathname == "/trade") {
      Router.push("/trade/SOL-USD");
    }
  });

  return <></>;
};

export default IndexPage;


