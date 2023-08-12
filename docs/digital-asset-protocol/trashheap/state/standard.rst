trashheap/state/standard.rs
===========================

Last edited: 2022-08-04 13:38:52

Contents:

.. code-block:: rs

    

#[derive(Clone)]
enum Standard {
    Unknown,
    NFTv1,
    NFT,
    NFTGroup,
    FungibleAsset,
}

struct Standard {
    name: String,
    modules: Vec
}

trait Standardized {

    fn modules() -> Ord<Mod>
}

