packages/app-extension/src/components/Unlocked/Balances/TokensWidget/TokenBadge.tsx
===================================================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useCustomTheme } from "@coral-xyz/themes";

export const TokenBadge = ({
  onClick,
  label,
  overwriteBackground,
  overwriteColor,
  fontSize,
  style,
}: {
  onClick: any;
  label: string;
  overwriteBackground?: string;
  overwriteColor?: string;
  fontSize?: number;
  style?: any;
}) => {
  const theme = useCustomTheme();
  return (
    <div
      style={{
        userSelect: "none",
        cursor: "pointer",
        background: overwriteBackground || theme.custom.colors.background,
        color: overwriteColor || theme.custom.colors.fontColor,
        padding: "4px 8px",
        borderRadius: 4,
        display: "inline-flex",
        fontSize,
        ...style,
      }}
      onClick={onClick}
    >
      {label}
    </div>
  );
};


