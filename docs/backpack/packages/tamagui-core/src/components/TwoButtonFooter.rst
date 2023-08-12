packages/tamagui-core/src/components/TwoButtonFooter.tsx
========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { StyleSheet, View } from "react-native";

export function TwoButtonFooter({
  leftButton,
  rightButton,
}: {
  leftButton: JSX.Element;
  rightButton: JSX.Element;
}): JSX.Element {
  return (
    <View style={twoButtonFooterStyles.container}>
      <View style={{ flex: 1, marginRight: 8 }}>{leftButton}</View>
      <View style={{ flex: 1, marginLeft: 8 }}>{rightButton}</View>
    </View>
  );
}

const twoButtonFooterStyles = StyleSheet.create({
  container: {
    flexDirection: "row",
    alignItems: "center",
  },
});


