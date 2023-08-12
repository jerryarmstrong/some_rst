example/App.tsx
===============

Last edited: 2023-03-28 15:16:55

Contents:

.. code-block:: tsx

    import { StyleSheet, Text, View } from 'react-native';

import * as ExpoMobileWalletAdapter from 'expo-mobile-wallet-adapter';

export default function App() {
  return (
    <View style={styles.container}>
      <Text>{ExpoMobileWalletAdapter.hello()}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});


