src/stores/queryParamsStore.ts
==============================

Last edited: 2023-01-27 22:22:52

Contents:

.. code-block:: ts

    import { createStore } from "reusable";
import useQueryParams from "../hooks/useQueryParams";

export default createStore(() => {
  return useQueryParams();
});


