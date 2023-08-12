packages/react-common/src/components/base/DangerButton.tsx
==========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useCustomTheme } from "@coral-xyz/themes";
import type { Button } from "@mui/material";

import { NegativeButton } from "./NegativeButton";

export function DangerButton({
  buttonLabelStyle,
  label,
  ...buttonProps
}: {
  buttonLabelStyle?: React.CSSProperties;
  label?: string;
} & React.ComponentProps<typeof Button>) {
  const theme = useCustomTheme();
  const buttonStyle = Object.assign(
    {
      backgroundColor: theme.custom.colors.negative,
      color: "#fff",
    },
    buttonProps.style
  );
  return (
    <NegativeButton
      buttonLabelStyle={buttonLabelStyle}
      label={label}
      {...buttonProps}
      style={{
        ...(buttonProps.style || {}),
        ...buttonStyle,
      }}
    />
  );
}


