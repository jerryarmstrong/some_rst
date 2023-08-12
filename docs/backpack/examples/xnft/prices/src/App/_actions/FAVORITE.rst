examples/xnft/prices/src/App/_actions/FAVORITE.ts
=================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { createSimpleAction, Reducer } from "../_helpers/redux";
import { StateType } from "../../state";

export const FAVORITE = createSimpleAction<
  {
    assetId: string;
    isFavorited: boolean;
  },
  "FAVORITE"
>("FAVORITE");

export const FAVORITE_reducer: Reducer<
  StateType,
  ReturnType<typeof FAVORITE>
> = (state, action) => {
  return {
    ...state,
    favorites: {
      ...state.favorites,
      [action.assetId]: action.isFavorited,
    },
  };
};


