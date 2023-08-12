CHANGELOG.md
============

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: md

    # @metaplex-foundation/kinobi

## 0.12.3

### Patch Changes

- [`75269c2`](https://github.com/metaplex-foundation/kinobi/commit/75269c2a504f30c5382c9eb6428ad66f2c3f7684) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Fix missing second arg for getArgVar macro in template

## 0.12.2

### Patch Changes

- [#56](https://github.com/metaplex-foundation/kinobi/pull/56) [`f8f57ac`](https://github.com/metaplex-foundation/kinobi/commit/f8f57aca0f98e86528cb663941184796d1816d1d) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Fix bytes size when parsing from IDL

- [#55](https://github.com/metaplex-foundation/kinobi/pull/55) [`f669542`](https://github.com/metaplex-foundation/kinobi/commit/f669542899edc8d6dbdbf0d1309195c361fbb9a4) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Add support for remaining accounts resolution

## 0.12.1

### Patch Changes

- [`2cde914`](https://github.com/metaplex-foundation/kinobi/commit/2cde914ca7018c84ec76d12c15ff9fde84f847f0) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Support docs for account instruction IDLs

## 0.12.0

### Minor Changes

- [#52](https://github.com/metaplex-foundation/kinobi/pull/52) [`0221889`](https://github.com/metaplex-foundation/kinobi/commit/0221889142300e69cde17eed136a94d82598b715) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Default optional account strategy to program ID

## 0.11.1

### Patch Changes

- [`205cfad`](https://github.com/metaplex-foundation/kinobi/commit/205cfadc9f498d45c3c0a3b8a2dbdb3546b3eff4) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Fix unused serializer import for booleans

## 0.11.0

### Minor Changes

- [#49](https://github.com/metaplex-foundation/kinobi/pull/49) [`3f54670`](https://github.com/metaplex-foundation/kinobi/commit/3f546701d1c6b08d4237783e4e258e16d758fa2c) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Update Umi to v0.8.2

## 0.10.2

### Patch Changes

- [`a3a9987`](https://github.com/metaplex-foundation/kinobi/commit/a3a9987a8a8ef9609c131345add0d1fcd8c94253) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Add UnwrapTupleEnumWithSingleStructVisitor

## 0.10.1

### Patch Changes

- [`88939ca`](https://github.com/metaplex-foundation/kinobi/commit/88939cabecacd3f107e8579580e74b83a7ff0bea) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Pass unresolved raw accounts to resolvers

## 0.10.0

### Minor Changes

- [#45](https://github.com/metaplex-foundation/kinobi/pull/45) [`6210eeb`](https://github.com/metaplex-foundation/kinobi/commit/6210eebf5554f15877e5aad71417434fa44132e3) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Use PublicKeys as base58 strings. See `@metaplex-foundation/umi` changelog for more details.

## 0.9.0

### Minor Changes

- [`05b9c36`](https://github.com/metaplex-foundation/kinobi/commit/05b9c361623c2f41ed5923a9818817965afd5728) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Rename mpl-essentials to mpl-toolbox

## 0.8.5

### Patch Changes

- [`b94d32e`](https://github.com/metaplex-foundation/kinobi/commit/b94d32e90c27f1ecb9fbe7d117651d9fa7ff22f6) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Fix computation of Anchor account discriminators

## 0.8.4

### Patch Changes

- [#41](https://github.com/metaplex-foundation/kinobi/pull/41) [`c01c113`](https://github.com/metaplex-foundation/kinobi/commit/c01c113304377b7b1f3642a383aa718ce3b66c1a) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Fix account seeds with no variable seeds

## 0.8.3

### Patch Changes

- [`8b1d051`](https://github.com/metaplex-foundation/kinobi/commit/8b1d051bb304186c41097ce3601da4bf002138e4) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Fix recursive type imports

## 0.8.2

### Patch Changes

- [`69f2425`](https://github.com/metaplex-foundation/kinobi/commit/69f2425c62ddef5233c7febb90d235a2cb57f2c0) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Fix byte size calculation for custom sized enums

- [`07ffd93`](https://github.com/metaplex-foundation/kinobi/commit/07ffd93d1f39df6eda4249fb21d1c5743f1f1065) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Convert account to public key when used as an arg default

## 0.8.1

### Patch Changes

- [#36](https://github.com/metaplex-foundation/kinobi/pull/36) [`1f34c3a`](https://github.com/metaplex-foundation/kinobi/commit/1f34c3a218d034340e236f1a712d7c724ebc0435) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Support custom discriminator sizes for enums

- [`ff685c7`](https://github.com/metaplex-foundation/kinobi/commit/ff685c76bce46c838970af623ce6fcfd1707808b) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Don't throw too early in the GetByteSizeVisitor

## 0.8.0

### Minor Changes

- [`63f13ca`](https://github.com/metaplex-foundation/kinobi/commit/63f13caa1f11e7e120eed36e3be536e1c475467e) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Add renderParentInstructions option to JS renderer

- [`0105e0f`](https://github.com/metaplex-foundation/kinobi/commit/0105e0f28b8b2e1972945ba1d69a83f8e7e7b7db) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Broaden the literal seed type as a constant seed type

### Patch Changes

- [`2754272`](https://github.com/metaplex-foundation/kinobi/commit/2754272b81497443a8b8eee759763d48cd175dd0) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Fix intermediary type when mapping serializers

- [`15a869d`](https://github.com/metaplex-foundation/kinobi/commit/15a869dc9c51be0f7b81f8ee81207f46c131e57d) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Export fetchMyAccountFromSeeds helper functions

- [`fc7d12b`](https://github.com/metaplex-foundation/kinobi/commit/fc7d12be558828ee983aba78bf4b72fea14d390e) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Fix exported comment when error has no message

- [`d74770c`](https://github.com/metaplex-foundation/kinobi/commit/d74770c629094ff04dcb9280a369d2fad7452240) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Rely on the name of dataArgs and extraArgs when rendering JS code

## 0.7.3

### Patch Changes

- [`8466e9c`](https://github.com/metaplex-foundation/kinobi/commit/8466e9c0b35d2e0e4cc4298da64c9493a976543d) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Offer more default kinds for args

## 0.7.2

### Patch Changes

- [`6c66054`](https://github.com/metaplex-foundation/kinobi/commit/6c6605432ad35847c7be71fdc7692f74db03ba02) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Improve conditions on resolved variables

## 0.7.1

### Patch Changes

- [`1c798af`](https://github.com/metaplex-foundation/kinobi/commit/1c798af4dc2ea14704b018f345b87c8dce1f9309) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Improve create options

## 0.7.0

### Minor Changes

- [#30](https://github.com/metaplex-foundation/kinobi/pull/30) [`822eb4d`](https://github.com/metaplex-foundation/kinobi/commit/822eb4dc71b9ee8d21734c7c26fe9ec25842dfe0) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Add extra args, arg defaults and custom resolvers

## 0.6.0

### Minor Changes

- [`b372624`](https://github.com/metaplex-foundation/kinobi/commit/b372624f251e157eca452aedbfcac60dbbba6ee0) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Generate get program helpers

## 0.5.0

### Minor Changes

- [`3ed5f4c`](https://github.com/metaplex-foundation/kinobi/commit/3ed5f4c8bb93984e450c7543554129ac657f2119) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Update to Umi 0.6.0

- [`d651771`](https://github.com/metaplex-foundation/kinobi/commit/d65177190cb33709befdeaacb9ec80116838427c) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Refactor isOptionalSigner as "either" union

## 0.4.6

### Patch Changes

- [`3701cc4`](https://github.com/metaplex-foundation/kinobi/commit/3701cc494417a96746ed5cf5cef847e39253dd05) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Use programId as default for Anchor optional accounts

## 0.4.5

### Patch Changes

- [`db04505`](https://github.com/metaplex-foundation/kinobi/commit/db0450530da3706313c0a3d31f26d94e8388d7c8) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Fix unused dependency

## 0.4.4

### Patch Changes

- [`3f2014b`](https://github.com/metaplex-foundation/kinobi/commit/3f2014bbc22c351db52318065ff49317774cf387) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Add size to TypeDefinedLinkNode

## 0.4.3

### Patch Changes

- [`565a31b`](https://github.com/metaplex-foundation/kinobi/commit/565a31bc2588f00738c35644a35155db3b55d860) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Use getPublicKey with fallback from program repository

## 0.4.2

### Patch Changes

- [`901de71`](https://github.com/metaplex-foundation/kinobi/commit/901de71f4c47c643d7b85b7309ca7943e51c6f2a) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Remove unused exports when using custom serializers

## 0.4.1

### Patch Changes

- [`79aa49f`](https://github.com/metaplex-foundation/kinobi/commit/79aa49fcc682fa84e89a34877214cfaf81fedf13) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Fix class that should have been renamed

## 0.4.0

### Minor Changes

- [#17](https://github.com/metaplex-foundation/kinobi/pull/17) [`a4a7eb0`](https://github.com/metaplex-foundation/kinobi/commit/a4a7eb03098655bc84f0e4bc1fd7fc1c02e62098) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Add GPA fields and custom serializer visitors

## 0.3.3

### Patch Changes

- [`2dacc74`](https://github.com/metaplex-foundation/kinobi/commit/2dacc748c21f6167115b34e80724b23ecbcf2d6b) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Separate scalar and empty cases in Enum value

## 0.3.2

### Patch Changes

- [`485a697`](https://github.com/metaplex-foundation/kinobi/commit/485a69764fd64a193f32fd8c6f3c663a4746afb8) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Allow value seeds on account default values

## 0.3.1

### Patch Changes

- [`36497cb`](https://github.com/metaplex-foundation/kinobi/commit/36497cb309ee274941d6efed900cd7bb90263362) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Only export getAccountSize if size is not null

## 0.3.0

### Minor Changes

- [`9883739`](https://github.com/metaplex-foundation/kinobi/commit/9883739822c6a16ae544c03cc593fff7aa519833) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Upgrade Umi

## 0.2.3

### Patch Changes

- [`627afcb`](https://github.com/metaplex-foundation/kinobi/commit/627afcbd6fa84a79187f190395077608eeb034fe) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Add importStrategy to JSTypeManifestVisitor

## 0.2.2

### Patch Changes

- [`decf050`](https://github.com/metaplex-foundation/kinobi/commit/decf0508f4bcb40dd688df5f9ec6bd545bf986dd) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Add size to bytes node

## 0.2.1

### Patch Changes

- [`d19fd82`](https://github.com/metaplex-foundation/kinobi/commit/d19fd820b8e7fca54ee4b1a4899120ac5607037a) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Rename SetLeafWrapperVisitor

- [`39dff3e`](https://github.com/metaplex-foundation/kinobi/commit/39dff3e7acbb9f9d40dbcd46f4d78157c85ba4c8) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Support sizes and prefixes for some IDL types

## 0.2.0

### Minor Changes

- [#8](https://github.com/metaplex-foundation/kinobi/pull/8) [`4a3b3f1`](https://github.com/metaplex-foundation/kinobi/commit/4a3b3f19b290c727daea80c40683a298a3e401ab) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Allow account and instruction nodes to use defined links

### Patch Changes

- [#6](https://github.com/metaplex-foundation/kinobi/pull/6) [`8265b23`](https://github.com/metaplex-foundation/kinobi/commit/8265b23ed983740b73aef7dfbea58189074e7e6c) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Update serializers

- [#9](https://github.com/metaplex-foundation/kinobi/pull/9) [`06818b7`](https://github.com/metaplex-foundation/kinobi/commit/06818b7dde8f5ecd083488eed0277a1e15a351aa) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Link PDA instruction account with their bump argument

## 0.1.1

### Patch Changes

- [#4](https://github.com/metaplex-foundation/kinobi/pull/4) [`7c132e8`](https://github.com/metaplex-foundation/kinobi/commit/7c132e87a191f7dc89b0a134a9ea482d303d5adc) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Add support for variable strings

## 0.1.0

### Minor Changes

- [`4ab3b09`](https://github.com/metaplex-foundation/kinobi/commit/4ab3b09d0fc90eda328e89ea70dec6abd218da9a) Thanks [@lorisleiva](https://github.com/lorisleiva)! - Create first release


