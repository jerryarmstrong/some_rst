src/tools/clippy/tests/ui-toml/conf_deprecated_key/conf_deprecated_key.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(clippy::uninlined_format_args)]

fn main() {}

#[warn(clippy::cognitive_complexity)]
fn cognitive_complexity() {
    let x = vec![1, 2, 3];
    for i in x {
        if i == 1 {
            println!("{}", i);
        }
    }
}


