src/tools/clippy/tests/ui/single_component_path_imports_self_after.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::single_component_path_imports)]
#![allow(unused_imports)]

use self::regex::{Regex as xeger, RegexSet as tesxeger};
pub use self::{
    regex::{Regex, RegexSet},
    some_mod::SomeType,
};
use regex;

mod some_mod {
    pub struct SomeType;
}

fn main() {}


