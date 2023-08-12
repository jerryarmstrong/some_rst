screens/AuthenticationScreen.tsx
================================

Last edited: 2023-04-24 04:07:06

Contents:

.. code-block:: tsx

    import React, {useEffect} from 'react';
import {NativeModules, Platform, StyleSheet, View} from 'react-native';
import {Button, Divider, Text} from 'react-native-paper';
import {useWallet} from '../components/WalletProvider';

import FadeInView from './../components/FadeInView';

const SolanaMobileWalletAdapter =
  Platform.OS === 'android' && NativeModules.WalletLib
    ? NativeModules.WalletLib
    : new Proxy(
        {},
        {
          get() {
            throw new Error(
              Platform.OS !== 'android'
                ? 'The package `solana-mobile-wallet-adapter-protocol` is only compatible with React Native Android'
                : 'Failed to link the `solana-mobile-wallet-adapter-protocol` package. Please make sure the package is installed correctly and all dependencies are up to date.',
            );
          },
        },
      );

export default function AuthenticationScreen() {
  const [visible, setIsVisible] = React.useState(true);
  const {wallet} = useWallet();

  // Assert that wallet is not null
  if (!wallet) {
    throw new Error('Wallet is null or undefined');
  }

  // there has got to be a better way to reset the state,
  // so it alwyas shows on render. I am react n00b
  useEffect(() => {
    setIsVisible(true);
  });

  return (
    <FadeInView style={styles.container} shown={visible}>
      <Text variant="bodyLarge">Authorize The Things</Text>
      <Divider style={styles.spacer} />
      <View style={styles.buttonGroup}>
        <Button
          style={styles.actionButton}
          onPress={() => {
            SolanaMobileWalletAdapter.authorizeDapp(
              Array.from(wallet.publicKey.toBytes()),
            );
            setIsVisible(false);
          }}
          mode="contained">
          Authorize
        </Button>
        <Button style={styles.actionButton} mode="outlined">
          Decline
        </Button>
      </View>
    </FadeInView>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 16,
    backgroundColor: 'skyblue',
    justifyContent: 'space-between',
    borderTopLeftRadius: 15,
    borderTopRightRadius: 15,
  },
  shell: {
    height: '100%',
  },
  spacer: {
    marginVertical: 16,
    width: '100%',
  },
  buttonGroup: {
    display: 'flex',
    flexDirection: 'row',
    width: '100%',
  },
  actionButton: {
    flex: 1,
    marginEnd: 8,
  },
});


