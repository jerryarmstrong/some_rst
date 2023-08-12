src/index.ts
============

Last edited: 2023-03-28 15:16:55

Contents:

.. code-block:: ts

    import { NativeModulesProxy, EventEmitter, Subscription } from 'expo-modules-core';

// Import the native module. On web, it will be resolved to ExpoMobileWalletAdapter.web.ts
// and on native platforms to ExpoMobileWalletAdapter.ts
import ExpoMobileWalletAdapterModule from './ExpoMobileWalletAdapterModule';
import ExpoMobileWalletAdapterView from './ExpoMobileWalletAdapterView';
import { ChangeEventPayload, ExpoMobileWalletAdapterViewProps } from './ExpoMobileWalletAdapter.types';

// Get the native constant value.
export const PI = ExpoMobileWalletAdapterModule.PI;

export function hello(): string {
  return ExpoMobileWalletAdapterModule.hello();
}

export async function setValueAsync(value: string) {
  return await ExpoMobileWalletAdapterModule.setValueAsync(value);
}

const emitter = new EventEmitter(ExpoMobileWalletAdapterModule ?? NativeModulesProxy.ExpoMobileWalletAdapter);

export function addChangeListener(listener: (event: ChangeEventPayload) => void): Subscription {
  return emitter.addListener<ChangeEventPayload>('onChange', listener);
}

export { ExpoMobileWalletAdapterView, ExpoMobileWalletAdapterViewProps, ChangeEventPayload };


