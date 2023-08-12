packages/chat-sdk/src/MessagePluginRenderer.tsx
===============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useCustomTheme } from "@coral-xyz/themes";

import { BarterUi } from "./components/barter/BarterUi";
import { useChatContext } from "./components/ChatContext";

export const MessagePluginRenderer = () => {
  const { openPlugin } = useChatContext();
  const { roomId } = useChatContext();
  const theme = useCustomTheme();
  if (!openPlugin) {
    return <div />;
  }

  return (
    <>{openPlugin.type === "barter" ? <BarterUi roomId={roomId} /> : null}</>
  );
};


