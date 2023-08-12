packages/chat-sdk/src/components/Barter.tsx
===========================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { BarterIcon } from "@coral-xyz/react-common";
import { styles, useCustomTheme } from "@coral-xyz/themes";
import { IconButton } from "@mui/material";

import { useChatContext } from "./ChatContext";

export const useStyles = styles((theme) => ({}));

export const Barter = ({ buttonStyle }: any) => {
  const theme = useCustomTheme();
  const { setOpenPlugin } = useChatContext();

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        flexDirection: "column",
      }}
    >
      <IconButton
        size="small"
        sx={{
          color: theme.custom.colors.icon,
          "&:hover": {
            background: `${theme.custom.colors.avatarIconBackground} !important`,
          },
        }}
        style={buttonStyle}
        onClick={(e) => {
          setOpenPlugin((p) =>
            p.type === "barter"
              ? { type: "", metadata: {} }
              : { type: "barter", metadata: {} }
          );
        }}
      >
        {" "}
        <BarterIcon fill={theme.custom.colors.icon} />{" "}
      </IconButton>
    </div>
  );
};


