tests/ui/proc-macro/raw-ident.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:raw-ident.rs

#[macro_use] extern crate raw_ident;

fn main() {
    make_struct!(fn);
    make_struct!(Foo);
    make_struct!(await);

    r#fn;
    r#Foo;
    Foo;
    r#await;

    make_bad_struct!(S); //~ ERROR expected one of
}


