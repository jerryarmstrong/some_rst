packages/tamagui-core/src/components/Skeleton/Skeleton.native.tsx
=================================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import ContentLoader, { Rect } from "react-content-loader/native";

import { useCustomTheme } from "../../hooks";

import type { SkeletonProps } from "./types";

export function Skeleton({ height, radius, width }: SkeletonProps) {
  const theme = useCustomTheme();
  const h = height ?? "100%";
  const w = width ?? "100%";

  return (
    <ContentLoader
      speed={2}
      height={h}
      width={w}
      backgroundColor={theme.custom.colors.balanceSkeleton}
      foregroundColor={theme.custom.colors.balanceSkeletonForeground}
    >
      <Rect x="0" y="0" height={h} width={w} rx={radius} ry={radius} />
    </ContentLoader>
  );
}


