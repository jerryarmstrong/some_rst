tests/ui/derives/clone-debug-dead-code-in-the-same-struct.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![forbid(dead_code)]

#[derive(Debug)]
pub struct Whatever {
    pub field0: (),
    field1: (), //~ ERROR fields `field1`, `field2`, `field3`, and `field4` are never read
    field2: (),
    field3: (),
    field4: (),
}

fn main() {}


