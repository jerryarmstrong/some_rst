packages/message-sdk/src/components/EmptyRequests.tsx
=====================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { EmptyState } from "@coral-xyz/react-common";
import { useCustomTheme } from "@coral-xyz/themes";
import ChatBubbleIcon from "@mui/icons-material/ChatBubble";

import { ParentCommunicationManager } from "../ParentCommunicationManager";

export const EmptyRequests = () => {
  const theme = useCustomTheme();
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        flexDirection: "column",
        flexGrow: 1,
      }}
    >
      <EmptyState
        icon={(props: any) => <ChatBubbleIcon {...props} />}
        title={"No Requests"}
        subtitle={"You have no message requests"}
        buttonText={"Go Back"}
        onClick={() => ParentCommunicationManager.getInstance().pop()}
        contentStyle={{
          color: theme.custom.colors.secondary,
        }}
      />
    </div>
  );
};


