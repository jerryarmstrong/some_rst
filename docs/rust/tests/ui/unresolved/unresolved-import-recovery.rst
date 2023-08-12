tests/ui/unresolved/unresolved-import-recovery.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that unresolved imports do not create additional errors and ICEs

mod m {
    pub use unresolved; //~ ERROR unresolved import `unresolved`

    fn f() {
        let unresolved = 0; // OK
    }
}

fn main() {
    match 0u8 {
        m::unresolved => {} // OK
        m::unresolved(..) => {} // OK
        m::unresolved{..} => {} // OK
    }
}


