app/src/hooks/use-trade-intervals.ts
====================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: ts

    import { useReducer } from "react";
import * as R from "../reducers/trade-intervals.reducer";

export default (initialData = undefined) => {
  const initialState = {
    data: initialData,
  };

  return useReducer(R.default, initialState);
};

export const { action } = R;


