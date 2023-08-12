tests/ui/rust-2018/dyn-trait-compatibility.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

type A0 = dyn;
type A1 = dyn::dyn; //~ERROR expected identifier, found keyword `dyn`
type A2 = dyn<dyn, dyn>; //~ERROR expected identifier, found `<`
type A3 = dyn<<dyn as dyn>::dyn>;

fn main() {}


