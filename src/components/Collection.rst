src/components/Collection.tsx
=============================

Last edited: 2023-03-12 23:06:11

Contents:

.. code-block:: tsx

    /* eslint-disable @next/next/no-img-element */
// Next, React
import { FC, useEffect, useState } from 'react';

// Wallet
import { useWallet, useConnection } from '@solana/wallet-adapter-react';

// Components
import pkg from '../../package.json';
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import ImageListItemBar from '@mui/material/ImageListItemBar';
// import ListSubheader from '@mui/material/ListSubheader';

// Store
import useUserSOLBalanceStore from '../stores/useUserSOLBalanceStore';
import useUserNFTsStore from '../stores/useUserNFTsStore';
import { NftWithToken, SftWithToken } from '@metaplex-foundation/js';
import { Trifle } from '@metaplex-foundation/mpl-trifle';

export class CollectionProps {
    setSelection: (nfts: (NftWithToken | SftWithToken)[]) => void;
    filter: (nft: NftWithToken | SftWithToken, props: any) => boolean;
    filterProps: any;
}

export const Collection: FC<CollectionProps> = ({ setSelection, filter, filterProps }) => {
    const [selectedNft, setSelectedNft] = useState<NftWithToken | SftWithToken>(null);

    const wallet = useWallet();
    const { connection } = useConnection();

    const nftList = useUserNFTsStore((s) => s.nftList).sort((nft0, nft1) => {
        if (nft0.name < nft1.name) return -1;
        if (nft0.name > nft1.name) return 1;
        return 0;
    });


    let filteredList = [];
    for (const nft of nftList) {
        if (filter(nft, filterProps)) {
            filteredList.push(nft);
        }
    }
    // console.log(filteredList);

    const { getUserNFTs } = useUserNFTsStore()

    useEffect(() => {
        if (wallet.publicKey) {
            // console.log(wallet.publicKey.toBase58())
            getUserNFTs(wallet.publicKey, connection)
            console.log("Num NFTS: ", nftList.length);
        }
    }, [wallet.publicKey, connection, getUserNFTs])

    useEffect(() => {
        setSelection([selectedNft]);
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [selectedNft])

    return (
        <ImageList sx={{ width: "100%", height: "100%", justifySelf: "center" }} cols={4}>
            {filteredList.map((nft) => (
                <ImageListItem key={nft.mint.address.toString()}>
                    <img
                        src={`${nft.json?.image}?w=248&fit=crop&auto=format`}
                        srcSet={`${nft.json?.image}?w=248&fit=crop&auto=format&dpr=2 2x`}
                        alt={nft.name}
                        loading="lazy"
                        onClick={() => {
                            if (selectedNft && selectedNft.address === nft.address) {
                                console.log("deselected");
                                setSelectedNft(null);
                            }
                            else {
                                setSelectedNft(nft);
                            }
                        }}
                        style={{ cursor: "pointer", border: selectedNft === nft ? "10px solid #0F0" : "none" }}
                    />
                    <ImageListItemBar
                        title={nft.name}
                        subtitle={nft.symbol}
                    />
                </ImageListItem>
            ))}
        </ImageList>
    );
};


