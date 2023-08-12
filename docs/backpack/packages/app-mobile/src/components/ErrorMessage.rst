packages/app-mobile/src/components/ErrorMessage.tsx
===================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { StyledText } from "@coral-xyz/tamagui";

export function ErrorMessage(props: any) {
  if (props.for) {
    return (
      <StyledText fontWeight="400" size={8} color="$redText">
        {props.for.message}
      </StyledText>
    );
  }

  return null;
}


