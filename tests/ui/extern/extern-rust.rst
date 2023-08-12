tests/ui/extern/extern-rust.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

#[repr(C)]
pub struct Foo(u32);

// ICE trigger, bad handling of differing types between rust and external ABIs
pub extern "C" fn bar() -> Foo {
    Foo(0)
}

fn main() {}


