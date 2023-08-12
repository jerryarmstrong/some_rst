utils/fetcher.js
================

Last edited: 2022-09-30 13:07:41

Contents:

.. code-block:: js

    import fetch from "isomorphic-unfetch";

// eslint-disable-next-line
export default async function Fetcher(...args) {
  const res = await fetch(...args);
  return res.json();
}


