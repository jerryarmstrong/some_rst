tests/ui/extern/not-in-block.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

extern fn none_fn(x: bool) -> i32;
//~^ ERROR free function without a body
extern "C" fn c_fn(x: bool) -> i32;
//~^ ERROR free function without a body


