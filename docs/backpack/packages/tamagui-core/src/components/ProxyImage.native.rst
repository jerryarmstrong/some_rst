packages/tamagui-core/src/components/ProxyImage.native.tsx
==========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { ErrorBoundary } from "react-error-boundary";
import { proxyImageUrl } from "@coral-xyz/common";
import type { ImageProps, ImageStyle } from "expo-image";
import { Image } from "expo-image";

import { StyledText } from "../";

export function ProxyImage({
  transition,
  placeholder,
  contentFit,
  src,
  size,
  style,
}: ImageProps & {
  src: string;
  size: number;
  style?: ImageStyle;
}): JSX.Element {
  const uri = proxyImageUrl(src, size);

  if (style?.width || style?.height) {
    throw new Error(
      "ProxyImage does not support width or height styles. Use size prop instead."
    );
  }

  if (style?.aspectRatio) {
    throw new Error("aspectRatio is already set to 1");
  }

  const styles = { width: size, height: size, aspectRatio: 1 };

  return (
    <ErrorBoundary
      fallbackRender={({ error }) => (
        <StyledText color="red">{error}</StyledText>
      )}
    >
      <Image
        source={uri}
        transition={transition}
        contentFit={contentFit}
        placeholder={placeholder}
        // React Native apps need to specify a width and height for remote images
        style={[styles, style as ImageStyle]}
      />
    </ErrorBoundary>
  );
}


