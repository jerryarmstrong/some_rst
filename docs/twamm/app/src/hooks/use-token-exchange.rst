app/src/hooks/use-token-exchange.ts
===================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: ts

    import { useReducer } from "react";
import * as R from "../reducers/select-available-tokens.reducer";

export default (initialData = undefined) => {
  const initialState = {
    data: initialData,
  };

  return useReducer(R.default, initialState);
};

export const { action } = R;


