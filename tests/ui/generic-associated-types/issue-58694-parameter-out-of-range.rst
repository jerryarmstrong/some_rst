tests/ui/generic-associated-types/issue-58694-parameter-out-of-range.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

trait Cert {
    type PublicKey<'a>: From<&'a [u8]>;
}

fn main() {}


