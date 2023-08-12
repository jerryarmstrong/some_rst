packages/app-extension/src/components/Locked/Reset/index.tsx
============================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useEffect } from "react";

import { useDrawerContext } from "../../common/Layout/Drawer";
import { useNavigation } from "../../common/Layout/NavStack";

import { ResetWelcome } from "./ResetWelcome";

export function Reset() {
  const { close } = useDrawerContext();
  const nav = useNavigation();
  useEffect(() => {
    nav.setOptions({ headerTitle: "" });
  }, []);
  return <ResetWelcome onClose={close} />;
}


