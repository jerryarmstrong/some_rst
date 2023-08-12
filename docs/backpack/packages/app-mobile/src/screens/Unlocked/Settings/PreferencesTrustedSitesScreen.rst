packages/app-mobile/src/screens/Unlocked/Settings/PreferencesTrustedSitesScreen.tsx
===================================================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { StyleSheet } from "react-native";

import { EmptyState, Screen } from "~components/index";
import { MaterialIcons } from "@expo/vector-icons";

export function PreferencesTrustedSitesScreen() {
  return (
    <Screen style={styles.container}>
      <EmptyState
        icon={(props: any) => (
          <MaterialIcons name="warning" size={32} {...props} />
        )}
        title="No trusted sites"
        subtitle="Trusted sites will be listed here"
      />
    </Screen>
  );
}

const styles = StyleSheet.create({
  container: {
    justifyContent: "center",
    alignItems: "center",
  },
});


