packages/react-common/src/components/base/NegativeButton.tsx
============================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import type {
  CustomTheme} from "@coral-xyz/themes";
import {
  HOVER_OPACITY,
  styles,
  useCustomTheme,
} from "@coral-xyz/themes";

import { PrimaryButton } from "./PrimaryButton";

const useStyles = styles((theme: CustomTheme) => ({
  negativeButton: {
    "&:hover": {
      opacity: HOVER_OPACITY,
      background: `${theme.custom.colors.negative} !important`,
      backgroundColor: `${theme.custom.colors.negative} !important,`,
    },
  },
}));

export function NegativeButton({ label, onClick, ...buttonProps }: any) {
  const classes = useStyles();
  const theme = useCustomTheme();
  return (
    <PrimaryButton
      className={classes.negativeButton}
      label={label}
      onClick={onClick}
      style={{
        backgroundColor: theme.custom.colors.negative,
      }}
      buttonLabelStyle={{
        color: theme.custom.colors.negativeButtonTextColor,
      }}
      {...buttonProps}
    />
  );
}


