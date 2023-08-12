screens/SignAndSendTransactionsScreen.tsx
=========================================

Last edited: 2023-04-24 04:07:06

Contents:

.. code-block:: tsx

    import {Keypair} from '@solana/web3.js';
import React, {useState, useEffect} from 'react';
import {NativeModules, Platform, StyleSheet, View} from 'react-native';
import {Button, Divider, Text} from 'react-native-paper';
import {MobileWalletAdapterServiceEventType} from '../App';
import {SolanaSigningUseCase} from '../utils/SolanaSigningUseCase';
import {
  SendTransactionsUseCase,
  SendTransactionsError,
} from '../utils/SendTransactionsUseCase';
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

type SignAndSendTransactionsEvent = {
  type: MobileWalletAdapterServiceEventType.SignAndSendTransactions;
  payloads: number[][];
  minContextSlot: string;
};

type Props = Readonly<{
  event: SignAndSendTransactionsEvent;
}>;

const signAndSendTransactions = async (
  wallet: Keypair,
  event: SignAndSendTransactionsEvent,
) => {
  const valid: boolean[] = event.payloads.map(_ => {
    return true;
  });
  let signedTransactions = event.payloads.map((numArray, index) => {
    try {
      return SolanaSigningUseCase.signTransaction(
        new Uint8Array(numArray),
        wallet,
      );
    } catch (e) {
      NativeModules.WalletLib.log(
        `Transaction ${index} is not a valid Solana transaction`,
      );
      valid[index] = false;
      return new Uint8Array([]);
    }
  });
  // If invalid, then fail the request
  if (valid.includes(false)) {
    SolanaMobileWalletAdapter.completeWithInvalidSignatures(valid);
    return;
  }
  try {
    const signatures = await SendTransactionsUseCase.sendSignedTransactions(
      signedTransactions,
      event.minContextSlot ? Number(event.minContextSlot) : undefined,
    );
    SolanaMobileWalletAdapter.completeWithSignatures(signatures);
  } catch (error) {
    console.log(`Error during signAndSendTransactions: ${error}`);
    if (error instanceof SendTransactionsError) {
      SolanaMobileWalletAdapter.completeWithInvalidSignatures(error.valid);
    } else {
      throw error;
    }
  }
};

// this view is basically the same as AuthenticationScreen.
// Should either combine them or pull common code to base abstraction
export default function SignAndSendTransactionsScreen({event}: Props) {
  const [visible, setIsVisible] = useState(true);
  const {wallet} = useWallet();

  // Assert that wallet is not null
  if (!wallet) {
    throw new Error('Wallet is null or undefined');
  }

  useEffect(() => {
    setIsVisible(true);
  });

  return (
    <FadeInView style={styles.container} shown={visible}>
      <Text variant="bodyLarge">Sign and send transactions</Text>
      <Divider style={styles.spacer} />
      <View style={styles.buttonGroup}>
        <Button
          style={styles.actionButton}
          onPress={async () => {
            await signAndSendTransactions(wallet, event);
            console.log('viz false');
            setIsVisible(false);
          }}
          mode="contained">
          Sign
        </Button>
        <Button style={styles.actionButton} mode="outlined">
          Reject
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


