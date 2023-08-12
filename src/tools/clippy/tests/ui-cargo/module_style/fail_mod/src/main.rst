src/tools/clippy/tests/ui-cargo/module_style/fail_mod/src/main.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::self_named_module_files)]

mod bad;

fn main() {
    let _ = bad::Thing;
    let _ = bad::inner::stuff::Inner;
    let _ = bad::inner::stuff::most::Snarks;
}


