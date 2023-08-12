packages/app-mobile/src/screens/Helpers/RandomBackgroundScreen.tsx
==================================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { View } from "react-native";
function getRandomColor() {
  const letters = "0123456789ABCDEF";
  let color = "#";
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

export function RandomBackgroundScreen() {
  return <View style={{ flex: 1, backgroundColor: getRandomColor() }} />;
}


