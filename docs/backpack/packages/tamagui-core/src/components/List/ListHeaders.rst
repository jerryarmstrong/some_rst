packages/tamagui-core/src/components/List/ListHeaders.tsx
=========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { StyledText, type StyledTextProps } from "../StyledText";

export const ListHeaderCore = ({
  style,
  title,
}: {
  style?: Omit<StyledTextProps, "children">;
  title: string;
}) => (
  <StyledText
    fontSize="$base"
    color="$secondary"
    marginBottom={8}
    marginLeft={16}
    {...style}
  >
    {title}
  </StyledText>
);


