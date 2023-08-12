examples/xnft/prices/src/App/Navigation.tsx
===========================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import React from "react";
import { Image, Stack, Text, View } from "react-xnft";

import TokenDetails from "./TokenDetails";
import TokenList from "./TokenList";

function Navigation() {
  return (
    <Stack.Navigator
      initialRoute={{ name: "list" }}
      options={({ route }) => {
        switch (route.name) {
          case "list":
            return {
              title: "Cryptoassets",
              props: {
                style: {
                  textAlign: "left",
                },
              },
            };
          case "details": {
            return {
              title: route.props?.token.name,
            };
          }
          default:
            throw new Error("unknown route");
        }
      }}
      style={{
        font: "Inter",
        fontSize: "20px",
        fontWeight: "700",
        height: "56px",
      }}
    >
      <Stack.Screen name="list" component={(props) => <TokenList />} />
      <Stack.Screen
        name="details"
        component={(props) => <TokenDetails {...props} />}
      />
    </Stack.Navigator>
  );
}

export default Navigation;


