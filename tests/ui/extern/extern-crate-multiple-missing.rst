tests/ui/extern/extern-crate-multiple-missing.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // If multiple `extern crate` resolutions fail each of them should produce an error
extern crate bar; //~ ERROR can't find crate for `bar`
extern crate foo; //~ ERROR can't find crate for `foo`

fn main() {
    // If the crate name introduced by `extern crate` failed to resolve then subsequent
    // derived paths do not emit additional errors
    foo::something();
    bar::something();
}


