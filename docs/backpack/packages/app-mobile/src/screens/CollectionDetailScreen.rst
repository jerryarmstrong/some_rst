packages/app-mobile/src/screens/CollectionDetailScreen.tsx
==========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { Suspense, useCallback, useMemo } from "react";
import { Text } from "react-native";

import { useFragment } from "@apollo/client";
import { useActiveWallet } from "@coral-xyz/recoil";
import { ErrorBoundary } from "react-error-boundary";
import { useSafeAreaInsets } from "react-native-safe-area-context";

import { BaseListItem } from "~components/CollectionListItem";
import { FullScreenLoading } from "~components/index";

import { PaddedFlatList } from "~src/components/PaddedFlatList";
import { NftNodeFragment } from "~src/graphql/fragments";

function ListItem({ id, onPress }: { id: string; onPress: any }): JSX.Element {
  const { data } = useFragment({
    fragment: NftNodeFragment,
    fragmentName: "NftNodeFragment",
    from: {
      __typename: "Nft",
      id,
    },
  });

  const item = useMemo(
    () => ({
      id: data.id,
      name: data.name,
      images: [data.image],
      type: data.type,
    }),
    [data]
  );

  return <BaseListItem onPress={onPress} item={item} />;
}

function Container({ navigation, route }: any): JSX.Element {
  const insets = useSafeAreaInsets();
  const activeWallet = useActiveWallet();
  const { nftIds } = route.params;

  const handlePressItem = useCallback(
    (item) => {
      navigation.push("CollectionItemDetail", {
        id: item.id,
        title: item.name,
        blockchain: activeWallet.blockchain,
      });
    },
    [navigation, activeWallet.blockchain]
  );

  const keyExtractor = (item: string) => item;
  const renderItem = useCallback(
    ({ item }: { item: string }) => {
      return <ListItem id={item} onPress={handlePressItem} />;
    },
    [handlePressItem]
  );

  const gap = 12;

  return (
    <PaddedFlatList
      data={nftIds}
      numColumns={2}
      keyExtractor={keyExtractor}
      renderItem={renderItem}
      columnWrapperStyle={{ gap }}
      contentContainerStyle={{
        gap,
        paddingBottom: insets.bottom + 32,
      }}
    />
  );
}

export function CollectionDetailScreen({
  navigation,
  route,
}: any): JSX.Element {
  return (
    <ErrorBoundary fallbackRender={({ error }) => <Text>{error.message}</Text>}>
      <Suspense fallback={<FullScreenLoading />}>
        <Container navigation={navigation} route={route} />
      </Suspense>
    </ErrorBoundary>
  );
}


