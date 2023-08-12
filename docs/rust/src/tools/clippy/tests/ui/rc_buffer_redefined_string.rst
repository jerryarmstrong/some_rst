src/tools/clippy/tests/ui/rc_buffer_redefined_string.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::rc_buffer)]

use std::rc::Rc;

struct String;

struct S {
    // does not trigger lint
    good1: Rc<String>,
}

fn main() {}


