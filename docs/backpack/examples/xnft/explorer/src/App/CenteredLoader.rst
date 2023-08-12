examples/xnft/explorer/src/App/CenteredLoader.tsx
=================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import React from "react";
import { Loading, View } from "react-xnft";

function CenteredLoader() {
  return (
    <View
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "100%",
      }}
    >
      <Loading />
    </View>
  );
}

export default CenteredLoader;


