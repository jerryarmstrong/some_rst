crates/credential/cargo-credential-gnome-secret/build.rs
========================================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    fn main() {
    pkg_config::probe_library("libsecret-1").unwrap();
}


