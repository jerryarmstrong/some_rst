examples/xnft/prices/src/App/_actions/INITIALIZE_STATE.ts
=========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { createSimpleAction, Reducer } from "../_helpers/redux";
import { StateType } from "../../state";

export const INITIALIZE_STATE = createSimpleAction<
  {
    state: StateType | null;
  },
  "INITIALIZE_STATE"
>("INITIALIZE_STATE");

export const INITIALIZE_STATE_reducer: Reducer<
  StateType,
  ReturnType<typeof INITIALIZE_STATE>
> = (state, action) => {
  return {
    ...(action.state ? action.state : state),
    initialized: true,
  };
};


