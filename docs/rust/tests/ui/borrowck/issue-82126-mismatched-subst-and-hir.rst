tests/ui/borrowck/issue-82126-mismatched-subst-and-hir.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #82126. Checks that mismatched lifetimes and types are
// properly handled.

// edition:2018

use std::sync::Mutex;

struct MarketMultiplier {}

impl MarketMultiplier {
    fn buy(&mut self) -> &mut usize {
        todo!()
    }
}

async fn buy_lock(generator: &Mutex<MarketMultiplier>) -> LockedMarket<'_> {
    //~^ ERROR this struct takes 0 lifetime arguments but 1 lifetime argument was supplied
    //~^^ ERROR this struct takes 1 generic argument but 0 generic arguments were supplied
    LockedMarket(generator.lock().unwrap().buy())
}

struct LockedMarket<T>(T);

fn main() {}


