tests/ui/use/use-crate-self.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::{self};
        //~^ ERROR crate root imports need to be explicitly named: `use crate as name;`

fn main() {}


