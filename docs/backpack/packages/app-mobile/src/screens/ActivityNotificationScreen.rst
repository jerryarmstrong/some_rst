packages/app-mobile/src/screens/ActivityNotificationScreen.tsx
==============================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { Suspense } from "react";
import { Text, View } from "react-native";

import { NotificationsData } from "@coral-xyz/recoil";
import { ErrorBoundary } from "react-error-boundary";

import { FullScreenLoading } from "~components/index";

export function ActivityNotificationScreen({ navigation }): JSX.Element {
  return <ScreenWrapper />;
}

function ScreenWrapper() {
  return (
    <ErrorBoundary fallback={<View />}>
      <Suspense fallback={<FullScreenLoading />}>
        <NotificationsData>
          {({ groupedNotifications }: any) => (
            <View style={{ flex: 1, alignItems: "center", paddingTop: 40 }}>
              <Text>Notifications</Text>
              <Text>{JSON.stringify(groupedNotifications)}</Text>
            </View>
          )}
        </NotificationsData>
      </Suspense>
    </ErrorBoundary>
  );
}


