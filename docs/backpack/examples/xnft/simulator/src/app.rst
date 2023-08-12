examples/xnft/simulator/src/app.tsx
===================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import ReactXnft, { Text, View } from "react-xnft";

//
// On connection to the host environment, warm the cache.
//
ReactXnft.events.on("connect", () => {
  // no-op
});

export function App() {
  return (
    <View>
      <Text style={{ color: "blue" }}>Hello, World!</Text>
    </View>
  );
}


