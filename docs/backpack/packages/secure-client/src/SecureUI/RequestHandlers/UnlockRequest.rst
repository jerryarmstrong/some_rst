packages/secure-client/src/SecureUI/RequestHandlers/UnlockRequest.tsx
=====================================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useEffect } from "react";

import type { QueuedRequest } from "../_atoms/clientAtoms";
import { RequireUserUnlocked } from "../Guards/RequireUserUnlocked";
import { Presentation } from "../Presentation";

export function UnlockRequest({
  currentRequest,
}: {
  currentRequest: QueuedRequest<"SECURE_USER_UNLOCK_KEYRING">;
}) {
  return (
    <Presentation
      currentRequest={currentRequest}
      onClosed={() => currentRequest.error("Plugin Closed")}
    >
      {(currentRequest) => (
        <RequireUserUnlocked force>
          <Confirmed
            onRender={() => currentRequest.respond({ unlocked: true })}
          />
        </RequireUserUnlocked>
      )}
    </Presentation>
  );
}

function Confirmed({ onRender }: { onRender: () => void }) {
  useEffect(onRender, [onRender]);
  return null;
}


