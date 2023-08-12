packages/tamagui-core/src/components/UserAvatar.tsx
===================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { ProxyImage } from "./ProxyImage";
// NOT A GREAT IMPLEMENTATION FOR THE WEB

export function UserAvatar({
  uri,
  size = 32,
}: {
  uri: string;
  size: number;
}): JSX.Element {
  return (
    <ProxyImage
      src={uri}
      size={size}
      style={{
        width: size,
        height: size,
      }}
    />
  );
}


