src/tools/clippy/tests/ui-toml/toml_disallow/conf_french_disallowed_name.rs
===========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]
#![allow(clippy::single_match)]
#![allow(unused_variables)]
#![warn(clippy::disallowed_names)]

fn test(toto: ()) {}

fn main() {
    let toto = 42;
    let tata = 42;
    let titi = 42;

    let tatab = 42;
    let tatatataic = 42;

    match (42, Some(1337), Some(0)) {
        (toto, Some(tata), titi @ Some(_)) => (),
        _ => (),
    }
}


