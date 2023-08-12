packages/react-common/src/components/base/UserIcon.tsx
======================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useCustomTheme } from "@coral-xyz/themes";

import { LocalImage } from "./LocalImage";

export function UserIcon({ image, size, marginRight }: any) {
  // TODO(mui)
  const theme = useCustomTheme();
  return (
    <LocalImage
      size={size || 44}
      src={image}
      style={{
        width: size || 44,
        height: size || 44,
        borderRadius: (size || 44) / 2,
        marginRight: marginRight || "8px",
        color: theme.custom.colors.positive,
      }}
    />
  );
}


