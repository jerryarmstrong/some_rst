tests/ui/issues/issue-7092.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Whatever {
}

fn foo(x: Whatever) {
    match x {
        Some(field) =>
//~^ ERROR mismatched types
//~| expected enum `Whatever`, found enum `Option`
//~| expected enum `Whatever`
//~| found enum `Option<_>`
            field.access(),
    }
}

fn main(){}


