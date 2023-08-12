src/pages/basics.tsx
====================

Last edited: 2023-06-24 05:42:55

Contents:

.. code-block:: tsx

    import type { NextPage } from "next";
import Head from "next/head";
import { BasicsView } from "../views";

const Basics: NextPage = (props) => {
  return (
    <div>
      <Head>
        <title>Solana Scaffold</title>
        <meta
          name="description"
          content="Basic Functionality"
        />
      </Head>
      <BasicsView />
    </div>
  );
};

export default Basics;


