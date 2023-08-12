packages/app-mobile/src/screens/AccountSettingsScreen.tsx
=========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { Suspense } from "react";

import { ErrorBoundary } from "react-error-boundary";

import { SettingsList } from "~components/AccountSettingsBottomSheet";
import { Screen, ScreenError, ScreenLoading } from "~components/index";

function Container({ navigation }): JSX.Element {
  return (
    <Screen>
      <SettingsList navigation={navigation} />
    </Screen>
  );
}

export function AccountSettingsScreen({ navigation }): JSX.Element {
  return (
    <ErrorBoundary
      fallbackRender={({ error }) => <ScreenError error={error} />}
    >
      <Suspense fallback={<ScreenLoading />}>
        <Container navigation={navigation} />
      </Suspense>
    </ErrorBoundary>
  );
}


