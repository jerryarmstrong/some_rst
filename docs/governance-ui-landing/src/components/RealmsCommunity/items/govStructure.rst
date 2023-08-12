src/components/RealmsCommunity/items/govStructure.tsx
=====================================================

Last edited: 2023-07-18 16:28:32

Contents:

.. code-block:: tsx

    import { Props } from '../Section';

const GOV_STRUCTURE: Omit<Props, 'alignment' | 'className' | 'index'> = {
  image: '/assets/backgrounds/gov-structure.png',
  text: 'Mint your own token, leverage an NFT collection, lock tokens via veTokens, or choose another structure.',
  title: (
    <>
      Choose your
      <br />
      governance structure
    </>
  ),
};

export default GOV_STRUCTURE;


