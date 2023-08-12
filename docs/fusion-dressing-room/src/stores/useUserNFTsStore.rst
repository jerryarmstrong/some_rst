src/stores/useUserNFTsStore.tsx
===============================

Last edited: 2023-03-12 23:06:11

Contents:

.. code-block:: tsx

    import create, { State } from 'zustand'
import { Connection, PublicKey, LAMPORTS_PER_SOL } from '@solana/web3.js'
import { Nft, Sft, Metadata, Metaplex, isNftWithToken, isSftWithToken, NftWithToken, SftWithToken } from '@metaplex-foundation/js'

interface UserNFTsStore extends State {
  nftList: (NftWithToken | SftWithToken)[];
  getUserNFTs: (publicKey: PublicKey, connection: Connection) => void
}

function isMetadata(arg: any): arg is Metadata {
  return true;
}

const useUserNFTsStore = create<UserNFTsStore>((set, _get) => ({
  nftList: [],
  getUserNFTs: async (publicKey, connection) => {
    const metaplex = new Metaplex(connection);
    const metadatas = await metaplex.nfts().findAllByOwner({
      owner: publicKey,
    });

    const nfts = await Promise.all(metadatas.map(async (metadata) => {
      if (isMetadata(metadata)) {
        const nft = await metaplex.nfts().load({ metadata, tokenOwner: publicKey });
        if (isNftWithToken || isSftWithToken) {
          return nft as (NftWithToken | SftWithToken);
        }
        else {
          console.log("Unexpected Error: " + nft);
          return null;
        }
      } else {
        return metadata as (NftWithToken | SftWithToken);
      }
    }));

    set((s) => {
      s.nftList = nfts;
      // console.log(`nftList updated, `, nfts);
    });
  },
}));

export default useUserNFTsStore;

