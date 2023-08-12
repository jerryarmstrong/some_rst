packages/tamagui-core/src/components/BottomSheet.tsx
====================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { Stack, StyledText } from "../";

type BottomSheetTitleProps = {
  title: string;
};
export function BottomSheetTitle({
  title,
}: BottomSheetTitleProps): JSX.Element {
  return (
    <StyledText fontSize="$lg" textAlign="center" mb={18}>
      {title}
    </StyledText>
  );
}

type BottomSheetContainerProps = {
  children: React.ReactNode;
};
export function BottomSheetContainer({
  children,
}: BottomSheetContainerProps): JSX.Element {
  return <Stack>{children}</Stack>;
}


