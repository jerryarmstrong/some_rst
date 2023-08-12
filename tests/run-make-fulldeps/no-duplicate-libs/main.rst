tests/run-make-fulldeps/no-duplicate-libs/main.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[link(name = "foo")] // linker should drop this library, no symbols used
#[link(name = "bar")] // symbol comes from this library
#[link(name = "foo")] // now linker picks up `foo` b/c `bar` library needs it
extern "C" {
    fn bar();
}

fn main() {
    unsafe { bar() }
}


