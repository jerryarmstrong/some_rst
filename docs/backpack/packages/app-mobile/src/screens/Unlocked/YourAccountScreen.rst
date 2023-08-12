packages/app-mobile/src/screens/Unlocked/YourAccountScreen.tsx
==============================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useKeyringHasMnemonic } from "@coral-xyz/recoil";

import { Screen } from "~components/index";
import { SettingsList } from "~screens/Unlocked/Settings/components/SettingsMenuList";

import { useOsBiometricAuthEnabled } from "~src/features/biometrics/hooks";

export function YourAccountScreen({ navigation }): JSX.Element {
  const hasMnemonic = useKeyringHasMnemonic();
  const isBiometricsEnabled = useOsBiometricAuthEnabled();

  const menuItems = {
    ...(!isBiometricsEnabled
      ? {
          "Change Password": {
            onPress: () => navigation.push("change-password"),
          },
        }
      : {}),
    ...(hasMnemonic
      ? {
          "Show Secret Recovery Phrase": {
            onPress: () => navigation.push("show-secret-phrase-warning"),
          },
        }
      : {}),
    "Log out": {
      onPress: () => navigation.push("reset-warning"),
    },
  };

  return (
    <Screen>
      <SettingsList menuItems={menuItems} />
    </Screen>
  );
}


