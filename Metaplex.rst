Metaplex.js
===========

Last edited: 2022-08-19 17:27:27

Contents:

.. code-block:: js

    import {NativeModules} from 'react-native';
const {Metaplex} = NativeModules;

class MetaplexBridge {
  constructor(environment, ownerPublicKey) {
    // environment -> devnet/mainnet/testnet | default -> mainnet
    // ownerPublicKey -> public key of owner wallet
    Metaplex.create(environment, ownerPublicKey);
  }

  findByMint(mintKey) {
    // finds nft for given mint key
    const promise = new Promise((resolve, reject) => {
      Metaplex.findByMint(mintKey, (data, error) => {
        if (error) {
          reject(error);
        }
        resolve(data);
      });
    });

    return promise;
  }

  findAllByOwner(ownerPublicKey) {
    // find all nfts by a given owner public key
    const promise = new Promise((resolve, reject) => {
      Metaplex.findAllByOwner(ownerPublicKey, (data, error) => {
        if (error) {
          reject(error);
        }
        resolve(data);
      });
    });

    return promise;
  }

  metadata(mintKey) {
    // finds nft metadata for given mint key
    const promise = new Promise((resolve, reject) => {
      Metaplex.metadata(mintKey, (data, error) => {
        if (error) {
          reject(error);
        }
        resolve(data);
      });
    });

    return promise;
  }
}

export default MetaplexBridge;


