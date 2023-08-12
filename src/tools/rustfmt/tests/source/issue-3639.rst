src/tools/rustfmt/tests/source/issue-3639.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo where {}
struct Bar where {}
struct Bax where;
struct Baz(String) where;
impl<> Foo<> for Bar<> where {}


