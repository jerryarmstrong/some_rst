App.js
======

Last edited: 2023-07-23 17:13:40

Contents:

.. code-block:: js

    import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View, Alert } from "react-native";

import "react-native-get-random-values";
import "@ethersproject/shims";
import { ethers } from "ethers";

setTimeout(() => {
  const now = performance.now();
  const wallet = ethers.Wallet.createRandom();
  const end = performance.now();
  Alert.alert(
    `💰 New wallet created! Took ${end - now}ms, Phrase: ${
      wallet.mnemonic.phrase
    }`
  );
}, 5000);

export default function App() {
  return (
    <View style={styles.container}>
      <Text>Open up App.js to start working on your app!</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
});


