src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0020_type_param_bounds.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct A<T>;
struct B<T:>;
struct C<T: 'a>;
struct D<T: 'a + >;
struct E<T: 'a + 'd >;
struct F<T: 'a + 'd + Clone>;
struct G<T: Clone + Copy>;
struct H<T: ::Foo + self::Bar + 'a>;
struct I<T:, U:,>;
struct K<'a: 'd, 'd: 'a + 'b, T: 'a + 'd + Clone>;

