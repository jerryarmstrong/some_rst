packages/app-extension/src/components/Unlocked/Settings/Preferences/Ethereum/index.tsx
======================================================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useEffect } from "react";

import { useNavigation } from "../../../../common/Layout/NavStack";
import { SettingsList } from "../../../../common/Settings/List";

export const PreferencesEthereum = () => {
  const nav = useNavigation();
  const ethereumMenuItems = {
    "RPC Connection": {
      onClick: () => nav.push("preferences-ethereum-rpc-connection"),
    },
  };

  useEffect(() => {
    nav.setOptions({ headerTitle: "Ethereum" });
  }, [nav]);

  return <SettingsList menuItems={ethereumMenuItems} />;
};


