tests/ui/opt-in-copy.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct CantCopyThis;

struct IWantToCopyThis {
    but_i_cant: CantCopyThis,
}

impl Copy for IWantToCopyThis {}
//~^ ERROR the trait `Copy` may not be implemented for this type

enum CantCopyThisEither {
    A,
    B,
}

enum IWantToCopyThisToo {
    ButICant(CantCopyThisEither),
}

impl Copy for IWantToCopyThisToo {}
//~^ ERROR the trait `Copy` may not be implemented for this type

fn main() {}


