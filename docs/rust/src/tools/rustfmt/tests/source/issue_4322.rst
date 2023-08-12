src/tools/rustfmt/tests/source/issue_4322.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Bar {
  type X<'a> where Self: 'a;
}


