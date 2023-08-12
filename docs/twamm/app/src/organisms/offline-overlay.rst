app/src/organisms/offline-overlay.tsx
=====================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: tsx

    import type { ReactElement } from "react";

import BrowserOnly from "../ssr";
import Overlay from "../molecules/offline-overlay";
import useNavigatorOnlineStatus from "../hooks/use-navigator-online-status";
import { useSnackbar } from "../contexts/notification-context";

export type Props = {
  children?: ReactElement;
};

const OfflineOverlay = ({ children }: Props) => {
  const { enqueueSnackbar } = useSnackbar();
  const { onLine } = useNavigatorOnlineStatus({
    onOffline: () => enqueueSnackbar("Lost connection", { variant: "warning" }),
    onOnline: () =>
      enqueueSnackbar("Connected", {
        variant: "success",
        autoHideDuration: 1e3,
      }),
  });

  return (
    <>
      <BrowserOnly>
        <Overlay open={!onLine} />
      </BrowserOnly>
      {children}
    </>
  );
};

export default OfflineOverlay;


