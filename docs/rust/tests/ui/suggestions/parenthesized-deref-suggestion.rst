tests/ui/suggestions/parenthesized-deref-suggestion.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Session {
    opts: u8,
}

fn main() {
    let sess: &Session = &Session { opts: 0 };
    (sess as *const Session).opts; //~ ERROR no field `opts` on type `*const Session`

    let x = [0u32];
    (x as [u32; 1]).0; //~ ERROR no field `0` on type `[u32; 1]`
}


