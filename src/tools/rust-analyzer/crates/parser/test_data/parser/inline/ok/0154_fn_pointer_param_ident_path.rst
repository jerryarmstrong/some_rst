src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0154_fn_pointer_param_ident_path.rs
====================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type Foo = fn(Bar::Baz);
type Qux = fn(baz: Bar::Baz);


