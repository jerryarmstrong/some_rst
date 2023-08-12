packages/app-mobile/src/components/CollectionAttributesList.tsx
===============================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { View } from "react-native";

import { toTitleCase } from "@coral-xyz/common";
import { StyledText, Stack } from "@coral-xyz/tamagui";

type Attribute = {
  trait: string;
  value: string;
};

function Pill({ trait, value }: Attribute): JSX.Element {
  return (
    <Stack
      backgroundColor="$card"
      px={8}
      py={8}
      borderRadius="$container"
      space={2}
    >
      <StyledText fontSize="$xs" color="$secondary">
        {toTitleCase(trait)}
      </StyledText>
      <StyledText fontSize="$sm" color="$fontColor">
        {value}
      </StyledText>
    </Stack>
  );
}

export function CollectionAttributes({
  attributes,
}: {
  attributes: Attribute[] | undefined;
}): JSX.Element | null {
  if (!attributes || attributes?.length === 0) {
    return null;
  }

  return (
    <>
      <StyledText color="$secondary" size="$base">
        Attributes
      </StyledText>
      <View
        style={{
          flexDirection: "row",
          flexWrap: "wrap",
          gap: 8,
          marginTop: 12,
          marginBottom: 18,
        }}
      >
        {attributes.map((attr: Attribute) => {
          return (
            <Pill key={attr.trait} trait={attr.trait} value={attr.value} />
          );
        })}
      </View>
    </>
  );
}


