packages/secure-client/src/SecureUI/RequestHandlers/SignMessageRequest.tsx
==========================================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import {
  PrimaryButton,
  ProxyImage,
  SecondaryButton,
  Stack,
  StyledText,
  TextArea,
  TwoButtonFooter,
  XStack,
  YStack,
} from "@coral-xyz/tamagui";
import { decode } from "bs58";
import { useRecoilValue } from "recoil";

import type { QueuedRequest } from "../_atoms/clientAtoms";
import { userAtom } from "../_atoms/userAtom";
import { ApproveTransactionBottomSheet } from "../_sharedComponents/ApproveTransactionBottomSheet";
import { RequireUserUnlocked } from "../Guards/RequireUserUnlocked";
import { Presentation } from "../Presentation";

export function SignMessageRequest({
  currentRequest,
}: {
  currentRequest: QueuedRequest<"SECURE_SVM_SIGN_MESSAGE">;
}) {
  //@ts-ignore
  const msgBuffer = Buffer.from(decode(currentRequest.request.message! ?? ""));
  const message = msgBuffer.toString();

  return (
    <Presentation
      currentRequest={currentRequest}
      onClosed={() => currentRequest.error("Plugin Closed")}
    >
      {(currentRequest) => (
        <RequireUserUnlocked>
          <ApproveTransactionBottomSheet
            id={currentRequest.queueId}
            title="Approve Message"
            message={message}
            onApprove={() => currentRequest.respond({ confirmed: true })}
            onDeny={() => currentRequest.error("User Denied Approval")}
          />
        </RequireUserUnlocked>
      )}
    </Presentation>
  );
}


