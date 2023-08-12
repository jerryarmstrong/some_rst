packages/app-extension/src/spotlight/useSearchedContacts.tsx
============================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { useContacts } from "@coral-xyz/db";
import { useUser } from "@coral-xyz/recoil";

export const useSearchedContacts = (searchFilter: string) => {
  const { uuid } = useUser();
  const contacts = useContacts(uuid);

  return contacts
    .filter((x) =>
      x.remoteUsername?.toLowerCase().includes(searchFilter?.toLowerCase())
    )
    .map((x) => ({
      username: x.remoteUsername,
      image: x.remoteUserImage,
      uuid: x.remoteUserId,
    }));
};


