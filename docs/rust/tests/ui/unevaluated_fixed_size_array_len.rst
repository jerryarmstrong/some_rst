tests/ui/unevaluated_fixed_size_array_len.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // https://github.com/rust-lang/rust/issues/49208

trait Foo {
    fn foo();
}

impl Foo for [(); 1] {
    fn foo() {}
}

fn main() {
    <[(); 0] as Foo>::foo() //~ ERROR E0277
}


