packages/app-extension/src/spotlight/useSearchedGroups.tsx
==========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useGroupCollections, useUser } from "@coral-xyz/recoil";

export const useSearchedGroupsCollections = (searchFilter: string) => {
  const { uuid } = useUser();
  const collections = useGroupCollections({ uuid });

  return collections
    .filter((x) => x.name?.toLowerCase()?.includes(searchFilter.toLowerCase()))
    .map((x) => ({
      name: x.name || "",
      image: x.image || "",
      collectionId: x.collectionId || "",
    }));
};


