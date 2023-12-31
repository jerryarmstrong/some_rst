app/src/hooks/use-navigator-online-status.ts
============================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: ts

    import { useCallback, useEffect, useState } from "react";

export default ({
  onOnline: handleOnline = () => {},
  onOffline: handleOffline = () => {},
} = {}) => {
  const [status, setStatus] = useState({
    onLine: globalThis.navigator?.onLine ?? false,
  });

  const onOnline = useCallback(() => {
    setStatus({ onLine: true });
    handleOnline();
  }, [handleOnline]);

  const onOffline = useCallback(() => {
    setStatus({ onLine: false });
    handleOffline();
  }, [handleOffline]);

  useEffect(() => {
    globalThis.addEventListener("online", onOnline);
    globalThis.addEventListener("offline", onOffline);

    return () => {
      globalThis.removeEventListener("online", onOnline);
      globalThis.removeEventListener("offline", onOffline);
    };
  }, [onOnline, onOffline]);

  return { onLine: status.onLine };
};


