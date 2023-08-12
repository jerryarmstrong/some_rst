utils/fetcher-md.js
===================

Last edited: 2022-09-30 13:07:41

Contents:

.. code-block:: js

    import fetch from "isomorphic-unfetch";

export default async function FetcherMD(...args) {
  const res = await fetch(...args);

  return res.text();
}


