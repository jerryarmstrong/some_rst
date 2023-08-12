packages/app-mobile/src/screens/NotFoundScreen.tsx
==================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { StyleSheet, Text, View } from "react-native";

export function NotFoundScreen() {
  return (
    <View style={styles.container}>
      <Text>
        Not found. Something must have went wrong with your keystore. Please
        reset the app and try again.
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
});


