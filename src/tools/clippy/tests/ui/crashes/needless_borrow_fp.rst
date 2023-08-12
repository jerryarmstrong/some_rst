src/tools/clippy/tests/ui/crashes/needless_borrow_fp.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[deny(clippy::all)]
#[derive(Debug)]
pub enum Error {
    Type(&'static str),
}

fn main() {}


