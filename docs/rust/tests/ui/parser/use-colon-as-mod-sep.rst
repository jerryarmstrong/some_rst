tests/ui/parser/use-colon-as-mod-sep.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Recover from using a colon as a path separator.

use std::process:Command;
//~^ ERROR expected `::`, found `:`
use std:fs::File;
//~^ ERROR expected `::`, found `:`
use std:collections:HashMap;
//~^ ERROR expected `::`, found `:`
//~| ERROR expected `::`, found `:`

fn main() { }


