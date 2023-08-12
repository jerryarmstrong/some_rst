packages/app-mobile/src/lib/splashScreen.ts
===========================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import * as SplashScreen from "expo-splash-screen";

// We need this so that we can hide any errors that may occur (e.g. unhandled promise rejection when FaceID is unlocking)
export function hideSplashScreen(): void {
  SplashScreen.hideAsync()
    .then(() => {
      // no-op
    })
    .catch(() => {
      // no-op
    });
}


