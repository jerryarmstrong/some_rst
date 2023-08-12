ui/src/pages/index.tsx
======================

Last edited: 2023-08-09 02:22:59

Contents:

.. code-block:: tsx

    import React, { useEffect } from "react";
import Router from "next/router";

const IndexPage = () => {
  useEffect(() => {
    const { pathname } = Router;
    if (pathname == "/") {
      Router.push("/trade");
    }
  });

  return <></>;
};

export default IndexPage;


