src/views/fusion/index.tsx
==========================

Last edited: 2023-03-12 23:06:11

Contents:

.. code-block:: tsx

    /* eslint-disable @next/next/no-img-element */
// Next, React
import { FC, useEffect, useState } from 'react';
import Link from 'next/link';

// Wallet
import { useWallet, useConnection } from '@solana/wallet-adapter-react';

// Components
import Stack from '@mui/material/Stack';

// Store
import useUserSOLBalanceStore from '../../stores/useUserSOLBalanceStore';
import useUserNFTsStore from '../../stores/useUserNFTsStore';
import { findTriflePda, createTrifleAccount, getConstraintModel, fuseTraits, getTrifleNfts, defuseTraits } from '../../utils/trifle';
import { Collection } from 'components/Collection';
import { Nft, NftWithToken, PublicKey, Sft, SftWithToken } from '@metaplex-foundation/js';
import { EscrowConstraintModel, Trifle } from '@metaplex-foundation/mpl-trifle';
import { Button, Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle } from '@mui/material';
import { Preview } from 'components/Preview';
import { useInterval } from 'usehooks-ts';
import { FusedTraits } from 'components/FusedTraits';

function filterByParentCollection(nft: Nft | Sft, props: any) {
  return (nft.collection?.address && (nft.collection?.address.toString() === process.env.NEXT_PUBLIC_PARENT_COLLECTION_MINT));
}

function filterByTraitCollections(nft: Nft | Sft, props: any) {
  const traitCollections = process.env.NEXT_PUBLIC_TRAIT_COLLECTION_MINTS.split(',');
  for (const traitCollection of traitCollections) {
    if (nft.collection?.address && (nft.collection?.address.toString() === props.collection)) {
      return true;
    }
  }
  return false;
}

export const FusionView: FC = ({ }) => {
  const wallet = useWallet();
  const { connection } = useConnection();

  const balance = useUserSOLBalanceStore((s) => s.balance)
  const { getUserSOLBalance } = useUserSOLBalanceStore()

  const nftList = useUserNFTsStore((s) => s.nftList).sort((nft0, nft1) => {
    if (nft0.name < nft1.name) return -1;
    if (nft0.name > nft1.name) return 1;
    return 0;
  })
  const { getUserNFTs } = useUserNFTsStore();
  const [selectedParent, setSelectedParent] = useState<NftWithToken | SftWithToken>(null);
  const [selectedTraitsMap, setSelectedTraitsMap] = useState<Map<string, (NftWithToken | SftWithToken)[]>>(new Map<string, (NftWithToken | SftWithToken)[]>());
  const [selectedTraits, setSelectedTraits] = useState<(NftWithToken | SftWithToken)[]>([]);
  const [fusedTraits, setFusedTraits] = useState<(NftWithToken | SftWithToken)[]>([]);
  const [trifleNfts, setTrifleNfts] = useState<(NftWithToken | SftWithToken)[]>([]);
  const [needsTrifle, setNeedsTrifle] = useState<boolean>(false);
  const [open, setOpen] = useState(false);
  const [constraintModel, setConstraintModel] = useState<EscrowConstraintModel>(null);
  const [schema, setSchema] = useState<any>(null);
  const [traitCollections, setTraitCollections] = useState(new Map<string, PublicKey>());
  const [delay, setDelay] = useState<number>(2000);
  // console.log(selectedParent);

  function setSelectionParent(nfts: (NftWithToken | SftWithToken)[]) {
    if (nfts.length > 0) {
      setSelectedParent(nfts[0]);
    }
  }

  function setSelectionTraits(key: string, nfts: (NftWithToken | SftWithToken)[]) {
    if (nfts && nfts.length > 0) {
      let nftsMap = selectedTraitsMap;
      nftsMap = nftsMap.set(key, nfts);
      setSelectedTraitsMap(nftsMap);
      setSelectedTraits(Array.from(nftsMap.values()).flat());
    }
    console.log(selectedTraitsMap);
    console.log(selectedTraits);
  }

  function setSelectionFusedTraits(nfts: (NftWithToken | SftWithToken)[]) {
    console.log("nfts", nfts);
    setFusedTraits(nfts);
    console.log(fusedTraits);
  }

  const handleClose = () => {
    console.log("handleClose");
    createTrifleAccount(connection, selectedParent as NftWithToken, wallet);
    setOpen(false);
  };

  const handleCancel = () => {
    console.log("handleCancel");
    setSelectedParent(null);
    setOpen(false);
  };

  useEffect(() => {
    if (wallet.publicKey) {
      // console.log(wallet.publicKey.toBase58())
      getUserNFTs(wallet.publicKey, connection)
    }
  }, [wallet.publicKey, connection, getUserNFTs])

  useEffect(() => {
    if (connection && selectedParent) {
      setDelay(2000);
    }
  }, [connection, selectedParent, open])

  useInterval(
    () => {
      async function check_trifle() {
        if (connection && selectedParent) {
          const auth_pubkey = new PublicKey(process.env.NEXT_PUBLIC_FUSION_AUTHORITY);
          const [triflePda] = findTriflePda(selectedParent.mint.address, auth_pubkey);
          const trifleAccount = await connection.getAccountInfo(triflePda);
          if (trifleAccount == null) {
            setNeedsTrifle(true);
            setOpen(true);
          }
          else {
            setNeedsTrifle(false);
            setOpen(false);
            setDelay(null);

            setTrifleNfts(await getTrifleNfts(connection, Trifle.fromAccountInfo(trifleAccount)[0]));
          }
        }
      }
      check_trifle();
    },
    delay
  )

  useEffect(() => {
    async function get_cm() {
      if (!connection) {
        return;
      }

      if (connection && !constraintModel) {
        setConstraintModel(await getConstraintModel(connection, new PublicKey(process.env.NEXT_PUBLIC_CONSTRAINT_MODEL_ADDRESS)));
      }

      if (constraintModel && constraintModel) {
        let traitCollections = new Map<string, PublicKey>();
        for (const entry of constraintModel?.constraints.entries()) {
          if (entry[1].constraintType.__kind === "Collection") {
            traitCollections.set(entry[0], entry[1].constraintType.fields[0]);
          }
        }

        setTraitCollections(traitCollections);
        console.log(traitCollections);

        console.log(constraintModel);

        let schema = await (await fetch(constraintModel.schemaUri)).json();
        console.log(schema);
        setSchema(schema);
      }
    }
    get_cm();
  }, [connection, constraintModel])


  if (selectedParent == null) {
    return (
      <Collection setSelection={setSelectionParent} filter={filterByParentCollection} filterProps={null} />
    );
  }
  else {
    return (
      <>
        <Stack
          direction="row"
          justifyContent="space-evenly"
          alignItems="stretch"
          spacing={1}
        >
          {/* <img
            src={`${selectedParent.json?.image}?w=248&fit=crop&auto=format`}
            srcSet={`${selectedParent.json?.image}?w=248&fit=crop&auto=format&dpr=2 2x`}
            alt={selectedParent.name}
            loading="lazy"
            style={{ width: "75%", objectFit: "contain" }}
          /> */}
          <Stack
            direction="column"
            // justifyContent="center"
            alignItems="stretch"
            spacing={2}
            width={"75%"}
          >
            <Preview
              parent={selectedParent as Nft}
              traits={selectedTraits.concat(trifleNfts)}
              fusedTraits={fusedTraits}
              schema={schema}
            />
            <FusedTraits setSelection={setSelectionFusedTraits} trifleNfts={trifleNfts} />
            <Button
              variant="contained"
              onClick={() => {
                defuseTraits(
                  connection,
                  wallet,
                  selectedParent as NftWithToken,
                  fusedTraits,
                  new PublicKey(process.env.NEXT_PUBLIC_FUSION_AUTHORITY)
                );
                // setDelay(5000);
              }}
              style={{ backgroundColor: "#f50057", color: "white", maxWidth: "100px", alignSelf: "center" }}
            >
              ⚛Defuse⚛
            </Button>
          </Stack>
          <Stack
            direction="column"
            justifyContent="space-evenly"
            alignItems="stretch"
            spacing={4}
            width={"100%"}
          >
            {[...traitCollections].map(([key, value]) => (
              <div key={key}>
                <h2>{key}</h2>
                <Collection setSelection={(nfts) => { setSelectionTraits(key, nfts) }} filter={filterByTraitCollections} filterProps={{ collection: value.toString() }} />
              </div>
            ))
            }
            <Button
              variant="contained"
              onClick={() => {
                fuseTraits(
                  connection,
                  wallet,
                  selectedParent as NftWithToken,
                  selectedTraits,
                  new PublicKey(process.env.NEXT_PUBLIC_FUSION_AUTHORITY)
                );
                // setDelay(5000);
              }}
              style={{ backgroundColor: "#f50057", color: "white", maxWidth: "100px", alignSelf: "center" }}
            >
              ⚛Fuse⚛
            </Button>
          </Stack>
        </Stack >
        <Dialog open={open} onClose={handleCancel}>
          <DialogTitle>Enable Fusion</DialogTitle>
          <DialogContent>
            <DialogContentText>
              This NFT does not have Fusion enabled. Enable now?
            </DialogContentText>
          </DialogContent>
          <DialogActions>
            <Button onClick={handleCancel}>Cancel</Button>
            <Button onClick={handleClose}>Enable</Button>
          </DialogActions>
        </Dialog>
      </>
    );
  }
};


