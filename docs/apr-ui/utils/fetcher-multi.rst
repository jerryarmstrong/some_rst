utils/fetcher-multi.js
======================

Last edited: 2022-09-30 13:07:41

Contents:

.. code-block:: js

    import fetch from "isomorphic-unfetch";

export default async function FetcherMulti(...args) {
  const res = await fetch(...args);
  const text = await res.text();

  console.log(json);
  return { text, json };
}


