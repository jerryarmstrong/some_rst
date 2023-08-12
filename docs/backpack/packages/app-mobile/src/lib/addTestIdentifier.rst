packages/app-mobile/src/lib/addTestIdentifier.ts
================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { Platform } from "react-native";

export const addTestIdentifier = (id: string) => {
  const str = toPascalCase(id.replace(/[^a-z0-9 ]/gi, ""));
  return Platform.OS === "android"
    ? { accessibilityLabel: str }
    : { testID: str };
};

const toPascalCase = (str: string) =>
  str
    .split(" ")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join("");


