packages/app-extension/src/spotlight/GroupIdentifier.tsx
========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { PushDetail } from "@coral-xyz/react-common";
import { useCustomTheme } from "@coral-xyz/themes";

export const GroupIdentifier = ({ name }: { name: string }) => {
  const theme = useCustomTheme();

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        marginBottom: 4,
      }}
    >
      <div style={{ color: theme.custom.colors.icon }}>{name}</div>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
        }}
      >
        <PushDetail style={{ width: "22px" }} />
      </div>
    </div>
  );
};


