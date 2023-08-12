src/tools/clippy/tests/ui/single_component_path_imports_nested_first.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::single_component_path_imports)]
#![allow(unused_imports)]

use regex;
use serde as edres;
pub use serde;

fn main() {
    regex::Regex::new(r"^\d{4}-\d{2}-\d{2}$").unwrap();
}

mod root_nested_use_mod {
    use {regex, serde};
    #[allow(dead_code)]
    fn root_nested_use_mod() {}
}


