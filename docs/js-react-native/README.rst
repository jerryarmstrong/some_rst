README.md
=========

Last edited: 2022-08-19 17:27:27

Contents:

.. code-block:: md

    # Metaplex React Native

Provides a bridge library of ios and android metaplex native sdks.

⚠️ Please note that this SDK has been implemented from scratch and is currently in alpha. This means some of the core API and interfaces might change from one version to another. Feel free to contact me about bugs, improvements and new use cases.

Currently bridge for following methods from Android SDK have been implemented:

- `findByMint`
- `findAllByOwner`
- `metadata`

## Usage

1. **Clone the repository**

   ```sh
   git clone https://github.com/metaplex-foundation/js-react-native
   ```

2. **Import Metaplex Class from Metaplex.js**

   ```js
   import Metaplex from './Metaplex.js';
   ```

3. **Initialize Metaplex**

   `constructor` method takes two arguments :

   - `environment` : It can take three values mainnet/testnet/devnet . Default value is mainnet

   - `ownerPublicKey` : It is the public key of owner wallet

   ```js
   const metaplex = new Metaplex(environment, ownerPublicKey);
   ```

   Once the Metaplex class is created, you can use the methods present in [Metaplex.js](./Metaplex.js) file

4. **Run the react native app**

   - Open the `android` folder in android studio and build the app.

   - Make sure android `emulator` is running with `android 12` (API 31)

   - Open a terminal in the root of the project and run the metro bundler by using following command.
     ```sh
     npm run start
     ```
   - Open another terminal in the root of the project and run the below command to run react-native app for android.
     ```sh
     npm run android
     ```

## Methods

Check out [`Metaplex.js`](./Metaplex.js) file for code samples of following methods

1. **findByMint**

   findByMint method takes one argument and returns a promise :

   - `mintKey` : It is the mint key for which nft is to be found

   ```js
   metaplex
   .findByMint(mintKey)
   .then(data => console.log(data))
   .catch(error => console.log(error));
   ```

2. **findAllByOwner**

   findAllByOwner method takes one argument and returns a promise :

   - `ownerPublicKey` : It is the public key of the owner for whom all NFTs are returned

   ```js
   metaplex
     .findAllByOwner(ownerPublicKey)
     .then(data => console.log(data))
     .catch(error => console.log(error));
   ```

3. **metadata**

   metadata method takes one argument and returns a promise :

   - `mintKey` : It is the mint key for which nft metadata is to be found

   ```js
   metaplex
     .metadata(mintKey)
     .then(data => console.log(data))
     .catch(error => console.log(error));
   ```

## Next Steps

As mentioned above, this SDK is still in very early stages. We plan to bridge the complete mobile SDK of Metaplex. Here’s a quick overview of what we plan to work on next.

- Bridge existing functionalities from android and ios native sdk


