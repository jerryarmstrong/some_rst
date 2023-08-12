tests/ui/parser/extern-no-fn.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" {
    f(); //~ ERROR expected one of `!` or `::`, found `(`
}

fn main() {
}


