tests/ui/pub/pub-ident-fn-with-lifetime.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

pub   foo<'a>(_s: &'a usize) -> bool { true }
//~^ ERROR missing `fn` for function definition

fn main() {
    foo(&2);
}


