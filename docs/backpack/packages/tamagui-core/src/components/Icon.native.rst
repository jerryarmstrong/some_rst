packages/tamagui-core/src/components/Icon.native.tsx
====================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { MaterialIcons } from "@expo/vector-icons";

import type { IconProps } from "./Icon.types";

export type MaterialIconName = React.ComponentProps<
  typeof MaterialIcons
>["name"];

export const IconKeyboardArrowRight = ({
  size = 24,
  color = "gray",
}: IconProps) => (
  <MaterialIcons name="keyboard-arrow-right" size={size} color={color} />
);

export function IconCheckmark({ size = 32, color }: IconProps): JSX.Element {
  return <MaterialIcons name="check" size={size} color={color} />;
}

export const getIcon = (name: MaterialIconName) => (
  <MaterialIcons name={name} size={28} color="gray" />
);


