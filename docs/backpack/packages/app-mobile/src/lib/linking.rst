packages/app-mobile/src/lib/linking.ts
======================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import * as Linking from "expo-linking";

export function openSettings(): void {
  Linking.openSettings();
}

export function openUrl(url: string): void {
  Linking.openURL(url);
}


