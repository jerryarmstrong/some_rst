src/tools/clippy/tests/ui-toml/large_include_file/large_include_file.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::large_include_file)]

// Good
const GOOD_INCLUDE_BYTES: &[u8; 581] = include_bytes!("large_include_file.rs");
const GOOD_INCLUDE_STR: &str = include_str!("large_include_file.rs");

#[allow(clippy::large_include_file)]
const ALLOWED_TOO_BIG_INCLUDE_BYTES: &[u8; 654] = include_bytes!("too_big.txt");
#[allow(clippy::large_include_file)]
const ALLOWED_TOO_BIG_INCLUDE_STR: &str = include_str!("too_big.txt");

// Bad
const TOO_BIG_INCLUDE_BYTES: &[u8; 654] = include_bytes!("too_big.txt");
const TOO_BIG_INCLUDE_STR: &str = include_str!("too_big.txt");

fn main() {}


