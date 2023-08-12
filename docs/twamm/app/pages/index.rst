app/pages/index.tsx
===================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import type { NextPage } from "next";
import Head from "next/head";
import IndexPage from "../src/pages/index-page";

const Home: NextPage = () => (
  <>
    <Head>
      <meta
        name="viewport"
        content="initial-scale=1,user-scalable=no,maximum-scale=1,width=device-width"
      />
      <title>Twamm</title>
    </Head>
    <IndexPage />
  </>
);

export default Home;


