src/pages/fusion.tsx
====================

Last edited: 2023-03-12 23:06:11

Contents:

.. code-block:: tsx

    import type { NextPage } from "next";
import Head from "next/head";
import { FusionView } from "../views";

const Fusion: NextPage = (props) => {
  return (
    <div>
      <Head>
        <title>Solana Scaffold</title>
        <meta
          name="description"
          content="Solana Scaffold"
        />
      </Head>
      <FusionView />
    </div>
  );
};

export default Fusion;


