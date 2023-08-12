tests/rustdoc-ui/infinite-recursive-type-impl-trait-return.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// normalize-stderr-test: "`.*`" -> "`DEF_ID`"
// normalize-stdout-test: "`.*`" -> "`DEF_ID`"
// edition:2018

pub async fn f() -> impl std::fmt::Debug {
    // rustdoc doesn't care that this is infinitely sized
    #[derive(Debug)]
    enum E {
        This(E),
        Unit,
    }
    E::Unit
}

fn main() {}


