tests/ui/unpretty/pretty-let-else.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zunpretty=hir
// check-pass



fn foo(x: Option<u32>) {
    let Some(_) = x else { panic!() };
}

fn main() {}


