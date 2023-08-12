packages/app-mobile/src/hooks/useAppStateTrigger.ts
===================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { useEffect, useRef } from "react";
import { AppState, AppStateStatus } from "react-native";

/** Invokes `callback` when app state goes from `from` to `to`. */
export function useAppStateTrigger(
  from: AppStateStatus,
  to: AppStateStatus,
  callback: () => void
): void {
  const appState = useRef(AppState.currentState);

  useEffect(() => {
    const subscription = AppState.addEventListener("change", (nextAppState) => {
      if (appState.current === from && nextAppState === to) {
        callback();
      }

      appState.current = nextAppState;
    });

    return () => {
      subscription.remove();
    };
  }, [from, callback, to]);
}


