tests/ui/conditional-compilation/cfg_attr_path.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![deny(unused_attributes)] // c.f #35584

mod auxiliary {
    #[cfg_attr(any(), path = "nonexistent_file.rs")] pub mod namespaced_enums;
    #[cfg_attr(all(), path = "namespaced_enums.rs")] pub mod nonexistent_file;
}

fn main() {
    let _ = auxiliary::namespaced_enums::Foo::A;
    let _ = auxiliary::nonexistent_file::Foo::A;
}


