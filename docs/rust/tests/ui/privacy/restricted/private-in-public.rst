tests/ui/privacy/restricted/private-in-public.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo {
    struct Priv;
    mod bar {
        use foo::Priv;
        pub(super) fn f(_: Priv) {}
        pub(crate) fn g(_: Priv) {} //~ ERROR E0446
        pub(crate) fn h(_: Priv) {} //~ ERROR E0446
    }
}

fn main() { }


