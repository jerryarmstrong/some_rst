src/stores/searchBarStore.ts
============================

Last edited: 2023-01-27 22:22:52

Contents:

.. code-block:: ts

    import { createStore } from "reusable";
import useSearchBar from "../hooks/useSearchBar";
import queryParamStore from "./queryParamsStore";

export default createStore(() => {
  const [query] = queryParamStore();

  return useSearchBar(query.schemaUrl || query.url);
});


