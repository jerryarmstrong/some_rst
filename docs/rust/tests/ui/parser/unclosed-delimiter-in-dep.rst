tests/ui/parser/unclosed-delimiter-in-dep.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod unclosed_delim_mod;

fn main() {
    let _: usize = unclosed_delim_mod::new();
    //~^ ERROR mismatched types
}


