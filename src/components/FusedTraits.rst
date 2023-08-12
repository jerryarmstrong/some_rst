src/components/FusedTraits.tsx
==============================

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

// Store
import useUserSOLBalanceStore from '../stores/useUserSOLBalanceStore';
import useUserNFTsStore from '../stores/useUserNFTsStore';
import { NftWithToken, SftWithToken } from '@metaplex-foundation/js';
import { Trifle } from '@metaplex-foundation/mpl-trifle';

export class FusedTraitsProps {
    setSelection: (nfts: (NftWithToken | SftWithToken)[]) => void;
    trifleNfts: (NftWithToken | SftWithToken)[];
}

export const FusedTraits: FC<FusedTraitsProps> = ({ setSelection, trifleNfts }) => {
    const [selectedNfts, setSelectedNfts] = useState<(NftWithToken | SftWithToken)[]>(trifleNfts);

    const wallet = useWallet();
    const { connection } = useConnection();

    const nftList = trifleNfts.sort((nft0, nft1) => {
        if (nft0.name < nft1.name) return -1;
        if (nft0.name > nft1.name) return 1;
        return 0;
    });

    useEffect(() => {
        console.log("selectedNft", selectedNfts);
        setSelection(selectedNfts);
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [selectedNfts])

    return (
        <ImageList sx={{ width: "auto", height: "auto", justifySelf: "center" }} cols={3}>
            {nftList.map((nft) => (
                <ImageListItem key={nft.mint.address.toString()}>
                    <img
                        src={`${nft.json?.image}?w=248&fit=crop&auto=format`}
                        srcSet={`${nft.json?.image}?w=248&fit=crop&auto=format&dpr=2 2x`}
                        alt={nft.name}
                        loading="lazy"
                        onClick={() => {
                            for (const selectedNft of selectedNfts) {
                                if (selectedNft.address === nft.address) {
                                    console.log("deselected");
                                    setSelectedNfts(selectedNfts.filter((nft) => nft.address !== selectedNft.address));
                                    return;
                                }
                            }
                            setSelectedNfts(selectedNfts.concat([nft]));
                            
                        }}
                    style={{ cursor: "pointer", border: isSelected(selectedNfts, nft) ? "10px solid #0F0" : "none" }}
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

function isSelected(selectedNfts: (NftWithToken | SftWithToken)[], nft: NftWithToken | SftWithToken) {
    for (const selectedNft of selectedNfts) {
        if (selectedNft.address === nft.address) {
            return true;
        }
    }
    return false;
}

