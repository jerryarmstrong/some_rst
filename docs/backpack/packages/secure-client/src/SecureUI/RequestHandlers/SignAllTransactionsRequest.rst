packages/secure-client/src/SecureUI/RequestHandlers/SignAllTransactionsRequest.tsx
==================================================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import type { QueuedRequest } from "../_atoms/clientAtoms";
import { ApproveTransactionBottomSheet } from "../_sharedComponents/ApproveTransactionBottomSheet";
import { RequireUserUnlocked } from "../Guards/RequireUserUnlocked";
import { Presentation } from "../Presentation";

export function SignAllTransactionsRequest({
  currentRequest,
}: {
  currentRequest: QueuedRequest<"SECURE_SVM_SIGN_ALL_TX">;
}) {
  return (
    <Presentation
      currentRequest={currentRequest}
      onClosed={() => currentRequest.error("Plugin Closed")}
    >
      {(currentRequest) => (
        <RequireUserUnlocked>
          <ApproveTransactionBottomSheet
            id={currentRequest.queueId}
            title="Sign All Transactions"
            message={JSON.stringify(currentRequest.request)}
            onApprove={() => currentRequest.respond({ confirmed: true })}
            onDeny={() => currentRequest.error("User Denied Approval")}
          />
        </RequireUserUnlocked>
      )}
    </Presentation>
  );
}


