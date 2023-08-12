tests/ui/double-type-import.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo {
    pub use self::bar::X;
    use self::bar::X;
    //~^ ERROR the name `X` is defined multiple times

    mod bar {
        pub struct X;
    }
}

fn main() {
    let _ = foo::X;
}


